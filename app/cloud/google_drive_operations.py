from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def connect_to_google_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

def connect_to_folder(drive, folder_id):
    folder = drive.CreateFile({'id': folder_id})
    return folder

def upload_file_to_drive(drive, local_file_path, folder):
    file_drive = drive.CreateFile({'title': os.path.basename(local_file_path), 'parents': [{'id': folder['id']}]})
    file_drive.Upload()
    return file_drive['id']

def download_all_files_from_drive(drive, local_folder_path, folder):
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder['id'])}).GetList()
    for file_drive in file_list:
        local_file_path = os.path.join(local_folder_path, file_drive['title'])
        if 'exportLinks' in file_drive:
            export_link = file_drive['exportLinks']['application/pdf']
            response, content = drive.auth.service._http.request(export_link)
            with open(local_file_path, "wb") as f:
                f.write(content)
        else:
            file_drive.GetContentFile(local_file_path)

def download_file_from_drive(drive, file_id, local_file_path):
    file_drive = drive.CreateFile({'id': file_id})
    file_drive.GetContentFile(local_file_path)

def list_files_in_drive(drive, folder):
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder['id'])}).GetList()
    for index, file_drive in enumerate(file_list, 1):
        print('{} Имя файла: {}, ID: {}'.format(index, file_drive["title"], file_drive["id"]))
    return file_list

def main():
    drive = connect_to_google_drive()
    folder_id = "1l7VjkDNUYJ28TbQ96Hhlx3dtE-XwAq2d"
    folder = connect_to_folder(drive, folder_id)
    file_list = list_files_in_drive(drive, folder)

    while True:
        print("\nВыберите действие:")
        print("Загрузить файл(ы) на Google Диск - введите 'w'" )
        print("Скачать все файлы с Google Диска - введите 'a'")

        try:
            action = input("Введите символ, или порядковый номер файла из списка, чтобы скачать его: ").strip().lower()

            if action == 'w':
                upload_option = input("Укажите путь к файлу или папке для загрузки: ").strip()

                if os.path.exists(upload_option):
                    if os.path.isfile(upload_option):
                        file_id = upload_file_to_drive(drive, upload_option, folder)
                        print("Файл '{}' успешно загружен. ID файла на Google Диске: {}".format(os.path.basename(upload_option), file_id))
                    elif os.path.isdir(upload_option):
                        for root, dirs, files in os.walk(upload_option):
                            for file_name in files:
                                local_file_path = os.path.join(root, file_name)
                                print("Загружается файл '{}'...".format(file_name))
                                file_id = upload_file_to_drive(drive, local_file_path, folder)
                                print("Файл '{}' успешно загружен. ID файла на Google Диске: {}".format(file_name, file_id))
                    else:
                        print("Указанный путь не является ни файлом, ни папкой.")
                else:
                    print("Указанный путь не существует.")

            elif action == 'a':
                local_folder_path = os.path.join(os.getcwd(), 'download')
                download_all_files_from_drive(drive, local_folder_path, folder)
                print("Все файлы успешно скачаны.")

            elif action.isdigit():
                download_option = int(action)
                if 1 <= download_option <= len(file_list):
                    file_id = file_list[download_option - 1]['id']
                    local_file_path = os.path.join(os.getcwd(), 'download', file_list[download_option - 1]['title'])
                    download_file_from_drive(drive, file_id, local_file_path)
                    print("Файл успешно скачан.")
                else:
                    print("Неверный номер файла.")

            else:
                print("Неверная команда. Пожалуйста, введите правильный символ.")

        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break

if __name__ == "__main__":
    main()
