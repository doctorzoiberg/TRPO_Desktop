from openpyxl import Workbook as book
from .Sheets import phones


def create_book():
    return book()


def save_book(work_book, path):
    work_book.save(path)


def create_phone_sheet(work_book, platform, data):
    work_sheet = phones.create_sheet(work_book, platform)
    phones.set_size(work_sheet)
    phones.set_titles(work_sheet, platform)
    phones.set_data(work_sheet, data)
    phones.set_styles(work_sheet, data)


def main(data, platform, path):
    work_book = create_book()
    create_phone_sheet(work_book, platform, data)
    save_book(work_book, path)
