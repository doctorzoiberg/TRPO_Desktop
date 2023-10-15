from .Styles import styles


def create_sheet(work_book, platform):
    work_sheet = work_book.active
    work_sheet.title = platform
    return work_sheet


def set_size(work_sheet):
    work_sheet.row_dimensions[1].height = 30
    work_sheet.row_dimensions[2].height = 20

    work_sheet.column_dimensions['A'].width = 10
    work_sheet.column_dimensions['B'].width = 40
    work_sheet.column_dimensions['C'].width = 15
    work_sheet.column_dimensions['D'].width = 15
    work_sheet.column_dimensions['E'].width = 15
    work_sheet.column_dimensions['F'].width = 15
    work_sheet.column_dimensions['G'].width = 25


def set_titles(work_sheet, platform):
    work_sheet.merge_cells('A1:G1')
    work_sheet['A1'] = platform

    work_sheet['A2'] = '№'
    work_sheet['B2'] = 'Device'
    work_sheet['C2'] = 'CPU'
    work_sheet['D2'] = 'GPU'
    work_sheet['E2'] = 'MEM'
    work_sheet['F2'] = 'UX'
    work_sheet['G2'] = 'Total Score'


def set_data(work_sheet, data):
    for key in data:
        work_sheet[f'A{int(key) + 2}'] = int(key)
        work_sheet[f'B{int(key) + 2}'] = data[key][0]
        work_sheet[f'C{int(key) + 2}'] = int(data[key][1])
        work_sheet[f'D{int(key) + 2}'] = int(data[key][2])
        work_sheet[f'E{int(key) + 2}'] = int(data[key][3])
        work_sheet[f'F{int(key) + 2}'] = int(data[key][4])
        work_sheet[f'G{int(key) + 2}'] = int(data[key][5])


def set_styles(work_sheet, data):
    for key in range(1, len(data)+3):
        align = styles.alignment()
        work_sheet[f'A{key}'].alignment = align
        work_sheet[f'B{key}'].alignment = align
        work_sheet[f'C{key}'].alignment = align
        work_sheet[f'D{key}'].alignment = align
        work_sheet[f'E{key}'].alignment = align
        work_sheet[f'F{key}'].alignment = align
        work_sheet[f'G{key}'].alignment = align

    title_font = styles.title_font()
    work_sheet['A1'].font = title_font
    work_sheet['A2'].font = title_font
    work_sheet['B2'].font = title_font
    work_sheet['C2'].font = title_font
    work_sheet['D2'].font = title_font
    work_sheet['E2'].font = title_font
    work_sheet['F2'].font = title_font
    work_sheet['G2'].font = title_font

    border = styles.border('bottom')
    work_sheet['A1'].border = border
    work_sheet['B1'].border = border
    work_sheet['C1'].border = border
    work_sheet['D1'].border = border
    work_sheet['E1'].border = border
    work_sheet['F1'].border = border
    work_sheet[f'A{len(data)+2}'].border = border
    work_sheet[f'B{len(data) + 2}'].border = border
    work_sheet[f'C{len(data) + 2}'].border = border
    work_sheet[f'D{len(data) + 2}'].border = border
    work_sheet[f'E{len(data) + 2}'].border = border
    work_sheet[f'F{len(data) + 2}'].border = border

    for key in range(2, len(data)+2):
        border = styles.border('right')
        work_sheet[f'G{key}'].border = border

    border = styles.border('bottom-right')
    work_sheet['G1'].border = border
    work_sheet[f'G{len(data) + 2}'].border = border

    border = styles.border('left-bottom-right')
    work_sheet['A2'].border = border
    work_sheet['B2'].border = border
    work_sheet['C2'].border = border
    work_sheet['D2'].border = border
    work_sheet['E2'].border = border
    work_sheet['F2'].border = border

    border = styles.border('all')
    work_sheet['G2'].border = border
