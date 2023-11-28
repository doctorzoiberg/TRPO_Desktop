import sys
import os
from PyQt5 import QtWidgets
from Frontend.app import Ui_MainWindow
from Frontend.windown1 import Ui_MainWindow as Ui_MainWindow_win_1
from Frontend.windown2 import Ui_MainWindow as Ui_MainWindow_win_2
from Parser import parser
from Excel import book
from cloud import google_drive_operations as drive


url_android = 'https://www.antutu.com/en/ranking/rank1.htm'
url_ios = 'https://www.antutu.com/en/ranking/ios1.htm'
url_ai = 'https://www.antutu.com/en/ranking/ai1.htm'


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_BtnAlfandega_2.clicked.connect(lambda: self.create_book('Android', url_android))
        self.ui.pushButton_BtnAlfandega_7.clicked.connect(lambda: self.create_book('IOS', url_ios))
        self.ui.pushButton_BtnAlfandega_10.clicked.connect(lambda: self.create_book('AI', url_ai))
        self.ui.pushButton_Android.clicked.connect(lambda: self.set_page(1))
        self.ui.pushButton_IOS.clicked.connect(lambda: self.set_page(2))
        self.ui.pushButton_AI.clicked.connect(lambda: self.set_page(3))

        self.ui.pushButton_BtnAlfandega_3.clicked.connect(lambda: self.open_win_1())
        self.ui.pushButton_BtnAlfandega_8.clicked.connect(lambda: self.open_win_1())
        self.ui.pushButton_BtnAlfandega_12.clicked.connect(lambda: self.open_win_1())

    def create_book(self, platform, url):
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,
                                                             "Сохранить файл",
                                                             ".",
                                                             "Xlsx Files (*.xlsx)")

        data = parser.get_data(parser.parse_text(url), platform)
        book.main(data, filename)

    def set_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def open_win_1(self):
        try:
            g_drive = drive.connect_to_google_drive()
        except Exception:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Невозможно пройти аутентификацию!")
            return
        self.win_1 = Win1(g_drive)
        self.win_1.show()


class Win1(QtWidgets.QMainWindow):
    def __init__(self, g_drive):
        self.g_drive = g_drive
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_win_1()
        self.ui.setupUi(self)
        self.ui.pushButton_BtnAlfandega_3.clicked.connect(lambda: self.open_win_2())

    def open_win_2(self):
        url = self.ui.lineEdit.text()
        try:
            folder_id = self.parse_url(url)
            g_folder = drive.connect_to_folder(self.g_drive, folder_id)
            self.win_2 = Win2(self.g_drive, g_folder)
        except Exception:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите ссылку на папку!")
            return
        self.win_2.show()
        self.close()

    def parse_url(self, url):
        splitted_url = url.split('/')
        return splitted_url[len(splitted_url) - 1]


class Win2(QtWidgets.QMainWindow):
    def __init__(self, g_drive, g_folder):
        self.g_drive = g_drive
        self.g_folder = g_folder
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow_win_2()
        self.ui.setupUi(self)

        file_list = drive.list_files_in_drive(g_drive, g_folder)
        text = ''
        for index, file_drive in enumerate(file_list, 1):
            text += '{}. {}\n'.format(index, file_drive["title"])
        self.ui.textEdit.setText(text)

        self.ui.pushButton_BtnAlfandega_3.clicked.connect(lambda: self.download_file(file_list))
        self.ui.pushButton_BtnAlfandega_4.clicked.connect(lambda: self.upload_file())
        self.ui.pushButton_BtnAlfandega_5.clicked.connect(lambda: self.open_win_1())

    def download_file(self, file_list):
        path_to_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if path_to_folder == '':
            return
        local_file_path = os.path.join(path_to_folder, file_list[2]['title'])
        drive.download_file_from_drive(self.g_drive, file_list[2]['id'], local_file_path)

    def upload_file(self):
        filename, ok = QtWidgets.QFileDialog.getOpenFileName(self,
                                                             "Выберите файл",
                                                             ".",
                                                             "Xlsx Files (*.xlsx)")
        if filename == '':
            return
        drive.upload_file_to_drive(self.g_drive, filename, self.g_folder)

    def open_win_1(self):
        self.win_1 = Win1(self.g_drive)
        self.win_1.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
