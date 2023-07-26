import sqlite3
#Создание базы данных hw.db в SQLite:
def create_database():
    conn = sqlite3.connect('hw.db')
    conn.close()
    print("База данных hw.db создана.")


#Создание таблицы products:
def create_table():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL,
            price NUMERIC(10, 2) DEFAULT 0.0 NOT NULL,
            quantity INTEGER DEFAULT 0 NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Таблица products создана.")
def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products_list = [
        ("фанта 1", 100.50, 10),
        ("йогурт2", 50.25, 5),
        ("сыр 3", 75.80, 20),
        ("банан 4", 85.80, 40),
        ("сэндвич 5", 115.80, 50),
        ("Смартфон iPhone 13 Pro 6", 99900, 20),
        ("Телевизор Samsung QLED Q80A 7", 129999, 5),
        ("Наушники Sony WH-1000XM4 8", 24999, 15),
        ("Кофемашина DeLonghi ECAM 9", 35000, 8),
        ("Фитнес-трекер Xiaomi Mi Band 6___10", 3500, 50),
        ("Игровая консоль PlayStation 5___11", 44990, 3),
        ("Пылесос Dyson V11___12", 52000, 12),
        ("Планшет Samsung Galaxy Tab S7___13", 58990, 7),
        ("Камера Sony Alpha A7 III___14", 139990, 6),
        ("Автомобиль Bently-2019___15",500.000,100)

    ]
    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products_list)

    conn.commit()
    conn.close()
    print("Товары добавлены в таблицу products.")
#Функция, которая меняет количество товара по id

def update_quantity_by_id(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()
    conn.close()
    print(f"Количество товара с id={product_id} обновлено.")

    # Функция, которая меняет цену товара по id:


def update_price_by_id(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))

    conn.commit()
    conn.close()
    print(f"Цена товара с id={product_id} обновлена.")

    # Функция, которая удаляет товар по id:


def delete_product_by_id(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()
    print(f"Товар с id={product_id} удален из таблицы products.")

    #Функция, которая выбирает все товары из БД и распечатывает их в консоли:
def select_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    all_products = cursor.fetchall()

    conn.close()

    print("Все товары в таблице products:")
    for product in all_products:
        print(product)


#Функция, которая выбирает из БД товары, которые дешевле 100 сомов и количество которых больше чем 5:
def select_products_less_than_100_and_quantity_over_5():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE price < 100 AND quantity > 5')
    selected_products = cursor.fetchall()

    conn.close()

    print("Товары дешевле 100 сомов и с количеством больше 5:")
    for product in selected_products:
        print(product)


#Функция, которая ищет в БД товары по названию:
def search_products_by_title(title):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%'+title+'%',))
    searched_products = cursor.fetchall()

    conn.close()

    print(f"Товары с названием, содержащим '{title}':")
    for product in searched_products:
        print(product)


#Тестирование каждой написанной функции:
def test_all_functions():
    create_database()
    create_table()
    add_products()

    select_all_products()

    update_quantity_by_id(1, 20)
    update_price_by_id(2, 60.50)

    select_products_less_than_100_and_quantity_over_5()

    search_products_by_title("мыло")

    delete_product_by_id(3)
    select_all_products()

if __name__ == "__main__":
    test_all_functions()





