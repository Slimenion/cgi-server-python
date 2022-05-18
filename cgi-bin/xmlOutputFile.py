#!/usr/bin/env python3
import sqlite3
import cgi
import main
import xmlOutput

form = cgi.FieldStorage()
filename = form.getfirst("xmlFile", "")

db_file = 'dbTest.db'
conn = sqlite3.connect(db_file)
cursor_database = conn.cursor()
xmlOutput.createxmlFile(main.select_all_orders(cursor_database), filename)


print("Content-type: text/html\n")
print("""<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Вывод результат</title>
        <link rel="stylesheet" href="style.css" />
    </head>
    <body>
        <style>
            * {
                box-sizing: border-box;
            }
            body {
                background: #f69a73;
            }
            .decor {
                position: relative;
                max-width: 400px;
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
            .form-inner input[type="submit"],
            .form-inner a {
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
print("<h3>Ваши данные успешно записаны в файл!</h3>")
print("<a href='http://127.0.0.1:8000/cgi-bin/orders.py'>Вернуться к таблице</a>")
print("""
            </div>
        </div>
    </body>
</html>
""")