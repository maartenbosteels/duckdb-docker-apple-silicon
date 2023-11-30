

print("started")

from time import sleep
import duckdb

print("imported duckdb")

db = duckdb.connect()

print("new db started")

df = db.sql("select 1, 'abc'").fetchall()

print(f"test_query: {df}")

df_ext = db.sql('from duckdb_extensions()').fetchall()

# print(f"duckdb_extensions:\n {df_ext}")

db.sql("INSTALL postgres")
db.sql("LOAD postgres")

print(f"postgres extension loaded")

print("sleep 5s to give postgres time to start ...")
sleep(5)

conn_string = "host=db port=5432  user=my_user password=my_password"

regs = db.sql(f"SELECT * FROM postgres_scan('{conn_string}', 'public', 'students') limit 5").fetchall()

print("duckdb found these rows in the postgres database:")
print(regs)


