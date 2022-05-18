#!/usr/bin/env python3
import sqlite3
import cgi
import main

db_file = 'dbTest.db'
conn = sqlite3.connect(db_file)
cursor_database = conn.cursor()
orders = main.select_all_orders(cursor_database)

print("Content-type: text/html\n")
print("""<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Вывод результат</title>
    </head>
    <body>
        <style>
            table {
                width: 100%;
                border: none;
                margin-bottom: 20px;
            }
            table th {
                font-weight: bold;
                text-align: left;
                border: none;
                padding: 10px 15px;
                background: #d8d8d8;
                font-size: 14px;
            }
            table tr th:first-child {
                border-radius: 8px 0 0 8px;
            }
            table tr th:last-child {
                border-radius: 0 8px 8px 0;
            }
            table td {
                text-align: left;
                border: none;
                padding: 10px 15px;
                font-size: 14px;
                vertical-align: top;
            }
            table tr:nth-child(even){
                background: #f3f3f3;
            }
            table tr td:first-child {
                border-radius: 8px 0 0 8px;
            }
            table tr td:last-child {
                border-radius: 0 8px 8px 0;
            }
            * {
                box-sizing: border-box;
            }
            body {
                background: #f69a73;
            }
            .decor {
                position: relative;
                max-width: 50%;
                margin: 50px auto 0;
                background: white;
                border-radius: 30px;
            }
            .form-left-decoration,
            .form-right-decoration {
                content: "";
                position: absolute;
                width: 50px;
                height: 20px;
                background: #f69a73;
                border-radius: 20px;
            }
            .form-left-decoration {
                bottom: 60px;
                left: -30px;
            }
            .form-right-decoration {
                top: 60px;
                right: -30px;
            }
            .form-left-decoration:before,
            .form-left-decoration:after,
            .form-right-decoration:before,
            .form-right-decoration:after {
                content: "";
                position: absolute;
                width: 50px;
                height: 20px;
                border-radius: 30px;
                background: white;
            }
            .form-left-decoration:before {
                top: -20px;
            }
            .form-left-decoration:after {
                top: 20px;
                left: 10px;
            }
            .form-right-decoration:before {
                top: -20px;
                right: 0;
            }
            .form-right-decoration:after {
                top: 20px;
                right: 10px;
            }
            .circle {
                position: absolute;
                bottom: 80px;
                left: -55px;
                width: 20px;
                height: 20px;
                border-radius: 50%;
                background: white;
            }
            .form-inner {
                padding: 50px;
            }
            .form-inner input,
            .form-inner select,
            .form-inner select option,
            .form-inner textarea {
                display: block;
                width: 100%;
                padding: 0 20px;
                margin-bottom: 10px;
                background: #e9eff6;
                line-height: 40px;
                border-width: 0;
                border-radius: 20px;
                font-family: "Roboto", sans-serif;
            }
            .form-inner select {
                padding: 12px;
            }
            .form-inner .but {
                margin-top: 30px;
                width: 100%;
            }
            .form-inner input[type="submit"],
            .form-inner .but a {
                margin-top: 30px;
                background: #f69a73;
                border-bottom: 4px solid #d87d56;
                color: white;
                padding: 10px;
                font-size: 14px;
                font-family: "Roboto", sans-serif;
                font-weight: 500;
                text-decoration: none;
                border-radius: 13px;
                margin: 30px auto;
                text-align: center;
            }
            .form-inner textarea {
                resize: none;
            }
            .form-inner h3 {
                margin-top: 0;
                font-family: "Roboto", sans-serif;
                font-weight: 500;
                font-size: 24px;
                color: #707981;
            }

            .form-inner p {
                margin-top: 0;
                font-family: "Roboto", sans-serif;
                font-weight: 500;
                color: #707981;
            }
        </style>
        <div class="decor">
            <div class="form-left-decoration"></div>
            <div class="form-right-decoration"></div>
            <div class="circle"></div>
            <div class="form-inner">
""")
print("<h3>Все заказы:</h3>")
print("<table>")
print("<tr><th>ID</th><th>ФИО</th><th>email</th><th>ID продукта</th><th>ID услуги</th></tr>")
for i in range(len(orders)):
    print("<tr>")
    print("<td>{}</td>".format(str(orders[i][0])))
    print("<td>{}</td>".format(str(orders[i][1])))
    print("<td>{}</td>".format(str(orders[i][2])))
    print("<td>{}</td>".format(str(orders[i][3])))
    print("<td>{}</td>".format(str(orders[i][4])))
    print("</tr>")
print("</table>")
print("""
            <form class="decor" action="/cgi-bin/xmlOutputFile.py">
                <div class="form-left-decoration"></div>
                <div class="form-right-decoration"></div>
                <div class="circle"></div>
                <div class="form-inner">
                    <h3>Получить данные в ввиде xml файла</h3>
                    <input type="file" name="xmlFile" />
                    <input type="submit" value="Заполнить выбранный файл данными" />
                </div>
            </form>
            <div class='but'><a href='http://127.0.0.1:8000/'>Вернуться к форме</a></div>
            </div>
        </div>
    </body>
</html>
""")