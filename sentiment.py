import requests
import pandas as pd
from pandas.io.json import json_normalize
import json
import xlsxwriter


def analyse_comments(rows):
    print("")

    headers = {
        'Content-Type': 'application/json',
    }

    params = (
        ('version', '2019-07-12'),
    )
    # responseSrr = ""

    for comment in rows:

        try:
            comment = str(comment.encode('utf-8'))

            data = ' {\n  "text": "' + comment + '",' \
                                                 '\n  "features": {\n    "sentiment": {\n     \n},\n    ' \
                                                 '"keywords": {\n      "emotion": true\n    }\n  }\n}'

            response = requests.post(
                'https://gateway-lon.watsonplatform.net/natural-language-understanding/api/v1/analyze',
                headers=headers, params=params, data=data,
                auth=('apikey', 'BaaDAfn3qpjkCo2Hsm173CLmCKqD-Bv2OIYpnxX4LetC'))
            print(json.dumps(response.text))

            workbook = xlsxwriter.Workbook(r"C:\Users\eyob\PycharmProjects\bunsen_reviews_c.xlsx")
            worksheet = workbook.add_worksheet()

            # Start from the first cell.
            # Rows and columns are zero indexed.
            row = 0
            column = 0

            content = json.dumps(response.text)

            # iterating through content list
            for item in content:
                # write operation perform
                worksheet.write(column, row, item)

                # incrementing the value of row by one
                # with each iteratons.
                column += 1
                workbook.close()

          # responseSrr += "\n" + response.text  #combining json objects

        except Exception as error:
         print(error)
            # return responseSrr


