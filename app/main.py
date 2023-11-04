import sys
from PyQt5 import QtWidgets
from Frontend.app import Ui_MainWindow
from Parser import parser
from Excel import book


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
        # self.ui.pushButton_BtnAlfandega_11.clicked.connect(lambda: self.create_book('AI', url_ai))
        self.ui.pushButton_Android.clicked.connect(lambda: self.set_page(1))
        self.ui.pushButton_IOS.clicked.connect(lambda: self.set_page(2))
        self.ui.pushButton_AI.clicked.connect(lambda: self.set_page(3))

    def create_book(self, platform, url):
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,
                                                             "Сохранить файл",
                                                             ".",
                                                             "Xlsx Files (*.xlsx)")
        if filename == '':
            return
        data = parser.get_phones_data(parser.parse_text(url))
        book.main(data, platform, filename)

    def set_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
