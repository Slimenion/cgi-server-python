import sqlite3


def create_tables(cursor_database):
    # создаем таблицу products
    cursor_database.execute("""CREATE TABLE IF NOT EXISTS products
    (id_product INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT NOT NULL,
    price_product REAL NOT NULL);
    """)

    cursor_database.execute("""CREATE TABLE IF NOT EXISTS services
    (id_service INTEGER PRIMARY KEY AUTOINCREMENT,
    name_service TEXT NOT NULL,
    price_service REAL NOT NULL);
    """)

    cursor_database.execute("""CREATE TABLE IF NOT EXISTS orders
    (id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    customers_name TEXT NOT NULL,
    email TEXT,
    product INTEGER,
    service INTEGER,
    FOREIGN KEY(product) REFERENCES products(id_product),
    FOREIGN KEY(service) REFERENCES services(id_service));
    """)


def insert_values_products(cursor_database, product_list):
    # записываем в нее данные
    for i in range(len(product_list)):
        cursor_database.execute("""INSERT INTO products(name_product, price_product)
            VALUES('""" + product_list[i][0] + """',""" + str(product_list[i][1]) + """ );""")


def insert_values_services(cursor_database, services_list):
    # записываем в нее данные
    for i in range(len(services_list)):
        cursor_database.execute("""INSERT INTO services(name_service, price_service)
                VALUES('""" + services_list[i][0] + """',""" + str(services_list[i][1]) + """ );""")


def insert_values_orders(cursor_database, orders_list):
    # записываем в нее данные
    for i in range(len(orders_list)):
        cursor_database.execute("""INSERT INTO orders(customers_name, email, product, service)
                    VALUES('""" + str(orders_list[i][0]) + """','""" + str(orders_list[i][1]) + """',""" +
                                str(orders_list[i][2]) + """,""" + str(orders_list[i][3]) +
                                """);""")


def select_all(cursor_database):
    cursor_database.execute("SELECT * FROM products;")
    print(cursor_database.fetchall())
    cursor_database.execute("SELECT * FROM services;")
    print(cursor_database.fetchall())
    cursor_database.execute("SELECT * FROM orders;")
    print(cursor_database.fetchall())

def select_all_orders(cursor_database):
    cursor_database.execute("SELECT * FROM orders;")
    return cursor_database.fetchall()


def select_chose_price_by_last_name(cursor_database, last_name):
    cursor_database.execute("""SELECT orders.customers_name, products.name_product, services.name_service, 
    (products.price_product + services.price_service) as itog_sum
    FROM orders, products, services  WHERE customers_name = '""" + str(last_name)+"""' AND id_product = orders.product 
    AND id_service = orders.service""")
    print(cursor_database.fetchall())


if __name__ == '__main__':
    # подключаемся к бд
    db_file = 'dbTest.db'
    conn = sqlite3.connect(db_file)
    cursor_database = conn.cursor()
    # создаем переменные для вставки в бд
    products_list = [["Windows 10", 17000], ["Kaspersky", 3000], ["Nord 32", 4000], ["Word 2020", 5000]]
    services_list = [["Install software", 1000], ["Install os", 5000]]
    orders_list = [["Ivanov", 1, 2], ["Sidorov", 2, 1]]
    # create_tables(cursor_database)
    # insert_values_products(cursor_database, products_list)
    # insert_values_services(cursor_database, services_list)
    # insert_values_orders(cursor_database, orders_list)
    # cursor_database.execute("DROP TABLE products;")
    # cursor_database.execute("DROP TABLE orders;")
    # cursor_database.execute("DROP TABLE services;")
    # cursor_database.execute("COMMIT;")
    # print(select_all_orders(cursor_database))
    select_all(cursor_database)
    # select_chose_price_by_last_name(cursor_database, 'Ivanov')
    cursor_database.close()
    conn.close()
