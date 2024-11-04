#%%
import sqlite3
### create a db
conn = sqlite3.connect("database.db")
print("opened db with sucess")
## create a table
conn.execute("CREATE TABLE login (username TEXT, pwd TEXT)")
print("table created sucessfully")

conn.close()
# %%
