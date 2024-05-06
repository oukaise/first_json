import openpyxl
from work_with_json import coin_data

def example():
    """
    Создание xlsx файла и запись в него
    """

    book = openpyxl.Workbook()

    book.remove(book.active)

    sheet_1 = book.create_sheet('Монеты')

    data = coin_data()

    headers = ['Currency', 'ID', 'Numcode', 'Charcode', 'Nominal', 'Name', 'Value', 'Previous']
    sheet_1.append(headers)

    for sheet in book.worksheets:
        for row in data:
            sheet.append(row)

    book.save("test.xlsx")

example()
