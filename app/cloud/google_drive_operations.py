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


def download_file_from_drive(drive, file_id, local_file_path):
    file_drive = drive.CreateFile({'id': file_id})
    file_drive.GetContentFile(local_file_path)


def list_files_in_drive(drive, folder):
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder['id'])}).GetList()
    for index, file_drive in enumerate(file_list, 1):
        print('{} Имя файла: {}, ID: {}'.format(index, file_drive["title"], file_drive["id"]))
    return file_list
