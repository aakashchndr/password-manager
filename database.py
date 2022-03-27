import sqlite3
from cryptography.fernet import Fernet

# Connecting to DataBase and creating a cursor
conn = sqlite3.connect('test_records.db')
c = conn.cursor()

# Create a Table
# c.execute("""CREATE TABLE records(
#         username test,
#         website text,
#         pwd text,
#         key text
#     )""")

# c.execute("SELECT rowid, username, website, pwd, key FROM records")
# items = c.fetchall()
# row_count = len(items)
# print('Row ID       ', 'Username        ', 'Website     ', 'Password')
# print('-------------------------------------------------------------')
# # for item in items:
# #     print(item)
# i = 0
# while(i < row_count):
#     obtained_key = Fernet(items[i][4])
#     dec_pwd = obtained_key.decrypt(items[i][3])
#     # print(dec_pwd.decode())
#     print(items[i][0], ' '*(16-len(items[i])), items[i][1], ' ' *
#           (16-len(items[i][1])), items[i][2], ' '*(16-len(items[i][2])), dec_pwd.decode(), ' '*(16-len(items[i][3])))
#     i = i + 1

# Commit our command and close connection
conn.commit()
conn.close()


def show_all():
    # Connect to database and create a cursor
    conn = sqlite3.connect('test_records.db')
    c = conn.cursor()
    c.execute("SELECT rowid, username, website, pwd, key FROM records")
    items = c.fetchall()
    row_count = len(items)
    print('\nRow ID       ', 'Username        ', 'Website     ', 'Password')
    print('-------------------------------------------------------------\n')
    
    i = 0
    while(i < row_count):
        obtained_key = Fernet(items[i][4])
        # print(f'From DB: {items[i][3]}')
        dec_pwd = obtained_key.decrypt(items[i][3])
        # print(dec_pwd.decode())
        print(items[i][0], ' '*(16-len(items[i])), items[i][1], ' ' *
              (16-len(items[i][1])), items[i][2], ' '*(16-len(items[i][2])), dec_pwd.decode(), ' '*(16-len(items[i][3])))
        i = i + 1

    # Commit our command and close connection
    conn.commit()
    conn.close()


def add_one(username, website, pwd):
    # Connect to database and create a cursor
    conn = sqlite3.connect('test_records.db')
    c = conn.cursor()

    # Encryption and key
    key = Fernet.generate_key()
    # f = Fernet(key)

    # Storing the key
    file = open('key.key', 'wb')  # Open the file as wb to write bytes
    file.write(key)  # The key is type bytes still
    file.close()

    f = Fernet(key)

    pwd = pwd.encode()
    # print(pwd)
    enc_pwd = f.encrypt(pwd)
    # print(key)
    # print(token)

    # dec_pwd = f.decrypt(enc_pwd)
    # print(dec_pwd.decode())

    c.execute("INSERT INTO records VALUES (?, ?, ?, ?)",
              (username, website, enc_pwd, key))

    # Commit our command and close connection
    conn.commit()
    conn.close()


def delete_one(website):
    # Connect to database and create a cursor
    conn = sqlite3.connect('test_records.db')
    c = conn.cursor()

    c.execute("DELETE FROM records WHERE website = (?)", (website,))
    print('\nEntry deleted!\n')
    # Commit our command and close connection
    conn.commit()
    conn.close()


def update_one(new_pwd, website):
    # Connect to database and create a cursor
    conn = sqlite3.connect('test_records.db')
    c = conn.cursor()

    # Encryption and key
    key = Fernet.generate_key()
    # f = Fernet(key)

    # Storing the key
    file = open('key.key', 'wb')  # Open the file as wb to write bytes
    file.write(key)  # The key is type bytes still
    file.close()

    f = Fernet(key)

    new_pwd = new_pwd.encode()
    # print(pwd)
    new_enc_pwd = f.encrypt(new_pwd)

    c.execute("UPDATE records SET pwd = (?), key = (?) WHERE website = (?)",
              (new_enc_pwd, key, website))

    print('\nUpdated!\n')
    # Commit our command and close connection
    conn.commit()
    conn.close()


def search(website):
    # Connect to database and create a cursor
    conn = sqlite3.connect('test_records.db')
    c = conn.cursor()

    c.execute("SELECT * FROM records WHERE website = (?)", (website,))
    items = c.fetchall()
    # print(items)
    # print('\n', data, '\n')

    # print('Row ID       ', 'Username        ', 'Website     ', 'Password')
    print('Username        ', 'Website     ', 'Password')
    print('----------------------------------------------\n')

    obtained_key = Fernet(items[0][3])
    dec_pwd = obtained_key.decrypt(items[0][2])
    # print(dec_pwd.decode())
    # print(items[0][0], ' '*(16-len(items[0])), items[0][1], ' ' *
    #       (16-len(items[0][1])), items[0][2], ' '*(16-len(items[0][2])), dec_pwd.decode(), ' '*(16-len(items[0][3])))
    print(f"{items[0][0]}         {items[0][1]}         {dec_pwd.decode()}")

    # # row_count = len(items)
    # print('Row ID       ', 'Username        ', 'Website     ', 'Password')
    # print('-------------------------------------------------------------\n')
    # # for item in items:
    # #     print(item)

    # # i = 1
    # # while(i == row_count):
    # for item in items:
    #     obtained_key = Fernet(items[i][4])
    #     dec_pwd = obtained_key.decrypt(items[i][3])
    #     # print(dec_pwd.decode())
    #     print(items[i][0], ' '*(16-len(items[i])), items[i][1], ' ' *
    #           (16-len(items[i][1])), items[i][2], ' '*(16-len(items[i][2])), dec_pwd.decode(), ' '*(16-len(items[i][3])))
    #     i = i + 1

    # Commit our command and close connection
    conn.commit()
    conn.close()
