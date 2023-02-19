import sqlite3
import time

db = sqlite3.connect("Dataset_keys")
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS data(
        user text, key integer
    )""")


# array_keys = [1515, 1623, 1823, 1293, 1515]
admin_key = ["admin_k", 1515]


def add_user_in_db(us_name, user_key):
    c.execute(f"INSERT INTO data VALUES ('{us_name}', '{user_key}')")
    db.commit()
    time.sleep(1)


def delete_user_in_db(user_key):
    c.execute(f"DELETE FROM data WHERE key = '{user_key}' ")
    db.commit()
    time.sleep(1)


def rewrite_users():
    s = 1
    while True:
        keys = read_key()
        # keys = read_key(s)
        # s += 1
        all_data = c.execute(f"SELECT * FROM data").fetchall()
        for i in all_data:
            if ((keys == i[1]) and (i[0]=="user")):
                delete_user_in_db(keys)
                break
            elif ((i[1] == keys) and (admin_key[0]==i[0])):
                return
        else:
            add_user_in_db("user", keys)



def open_door():
    print("Door is opened")


def close_door():
    print("Door is closed")


def check(check_key):
    c.execute(f"SELECT * FROM data")
    for item in c.fetchall():
        if ((check_key == admin_key[1]) and (item[0] == admin_key[0])):
            rewrite_users()
            break
        elif ((check_key == item[1]) and (item[0] != admin_key[0])):
            open_door()
        else:
            close_door()


# def read_key(a):
#     return array_keys[a]


def read_key():

    return


def main():
    # add_user_in_db(admin_key[0], admin_key[1])
    for i in range(1):
        key = read_key()
        # key = read_key(0)
        check(key)
        # c.execute(f"SELECT * FROM data")
        # print(c.fetchall())
        db.close()


if __name__ == "__main__":
    main()