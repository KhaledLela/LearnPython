# Code: https://www.py4e.com/code3/db1.py
# https://www.py4e.com/html3/15-database

import sqlite3

# conn = sqlite3.connect('farm.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS users')
# cur.execute('CREATE TABLE users (name TEXT, email TEXT, mobile INTEGER)')
#
# conn.close()

# Use a context manager to ensure proper handling of the connection
with sqlite3.connect('farm.sqlite') as conn:
    cur = conn.cursor()
    # DDL
    # cur.execute('DROP TABLE IF EXISTS users')
    # cur.execute('CREATE TABLE users (name TEXT, email TEXT, age INTEGER)')

    # DML
    # CRUD (create/INSERT, Read/SELECT, Update, DELETE).
    # cur.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
    #             ('Khaled Lela', 'eng.khaled.lela@gmail.com', 37))
    #
    # cur.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
    #             ('Abdelrahman khaled', 'abdo_kl@gmail.com', 8))
    #
    # cur.execute('INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
    #             ('Sara khaled', 'sara_kl@gmail.com', 6))
    #
    # conn.commit()

    # print('Track:')
    # cur.execute('SELECT * FROM users')
    # cur.execute('SELECT name, email, age FROM users')

    # cur.execute("UPDATE users SET name = 'Sara' WHERE age = 6")
    # cur.execute('DELETE FROM users WHERE age = 6')
    #
    # cur.execute('SELECT name FROM users')
    # for row in cur:
    #     print(row)
    # #

    cur.execute('DROP TABLE IF EXISTS courses')
    cur.execute('CREATE TABLE courses (Id INTEGER, name TEXT, teacher TEXT)')
    cur.execute("INSERT INTO courses (Id,name,teacher) VALUES (?,?,?)", (1, 'MATH', 'Dr: Watson'))
    cur.execute("INSERT INTO courses (Id,name,teacher) VALUES (?,?,?)", (2, 'English', 'Dr: Watson'))
    cur.execute("INSERT INTO courses (Id,name,teacher) VALUES (?,?,?)", (3, 'Arabic', 'Dr: Mohammed'))

    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute('CREATE TABLE users (name TEXT, course_id INTEGER)')

    cur.execute("INSERT INTO users (name,course_id) VALUES (?,?)", ('Ahmed', 1))
    cur.execute("INSERT INTO users (name,course_id) VALUES (?,?)", ('Ibrahim', 2))
    cur.execute("INSERT INTO users (name,course_id) VALUES (?,?)", ('Aly', 3))
    # conn.commit()

    cur.execute('SELECT u.name, c.name FROM users u '
                'JOIN courses c ON u.course_id = c.id')

    for row in cur:
        print(row)
