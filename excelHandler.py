import json

import openpyxl as xl


def proccess_workbook(filename, sheetname):
    wb = xl.load_workbook(filename)
    sheet = wb[sheetname]

    list_items = []
    for row in range(2, sheet.max_row + 1):
        item = {}
        for col in range(1, sheet.max_column):
            # create key value bears
            key = sheet.cell(1, col).value.lower().replace(' ', '_')
            value = sheet.cell(row, col).value

            item[key] = value

        # append rows
        list_items.append(item)

    for item in list_items:
        # remove unwanted keys
        del item['us']
        del item['serial_number']
        # del item['Manufacturer']
        del item['cpu_gen']
        del item['المكان']
        del item['السعر']
        del item['خصم']

        # merge properties related, such as ram, ram type, etc
        try:
            item['ram'] = str(item['ram']) + '-GB/' + item['ram-type']
            item['hdd'] = str(item['hdd']) + '-GB/' + item['hdd1_type']

            item['screen_size'] = str(item['screen_size']) + '/Inch'
        except TypeError:
            print('Ram or HDD sizes maybe are not set...')

        del item['hdd1_type']
        del item['ram-type']

    # Create a copy to remove the note field, to get the number of occurrences of each element
    list_items_copy = list_items.copy()
    # for item in list_items_copy:
    #     del item['note']

    # uniques
    uniques_list_items = []
    for item in list_items_copy:
        if item in uniques_list_items:
            continue
        uniques_list_items.append(item)

    # set counts for each item in uniques list
    # for item in uniques_list_items:
    #     item['count'] = list_items_copy.count(item)

    models = []
    for i in uniques_list_items:
        models.append([i['manufacturer'], i['model'], i['cpu']])

    print(models)


proccess_workbook('op.xlsx', 'الشيت القديم')

# from pathlib import Path

# path = Path('fds')

# path.rmdir()
