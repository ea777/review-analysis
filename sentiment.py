import requests
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
            print(response.text)

            # responseSrr += "\n" + response.text  #combining json objects



        except:
            print("")

            workbook = xlsxwriter.Workbook(r'C:\Users\eyob\PycharmProjects\test.xlsx', 'w')
            worksheet = workbook.add_worksheet()
            row = 0
            col = 0
            for comments in rows():
                worksheet.write(row, col, str(comments[0]))
                worksheet.write(row, col + 1, str(comments[1]))
                row += 1
            workbook.close()

    # return responseSrr


