import sqlite3
from users import user_list

print(user_list)
conn = sqlite3.connect("Y:\\ITHub\\SoftServe\\Lessons\\HW12_SQLite\\"
                       "db1.db")
c = conn.cursor()
c.execute('''CREATE TABLE users(id int auto_increment primary key,
            name varchar, password varchar)''')
c.execute('''INSERT INTO users VALUES(1, 'John', '1323456789')''')
conn.commit()
c.close()
conn.close()

# c.executemany("insert into users values (?, ?, ?)", user_list)
