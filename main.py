import sqlite3


con = sqlite3.connect(r"test_task/test.db")
cursor = con.cursor()
partner = None
state = u'NULL'
bs = 0
factor = [(1,), (2,)]
cursor.execute("""SELECT * FROM testidprod where bs=?, factor=?""", (bs, factor,))
print(cursor.fetchall())
