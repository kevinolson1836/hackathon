DATABASE_URL = "postgresql://kevin:Ilcc1MSUkmZTTxs0hOD3hg@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dcalmer-sprite-5779"

DATABASE_URL = "postgresql://kevin:Ilcc1MSUkmZTTxs0hOD3hg@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dcalmer-sprite-5779"
import os
import psycopg2



# def add_word_to_db(word):
conn = psycopg2.connect(DATABASE_URL, sslrootcert = 'root.crt',)

with conn.cursor() as cur:
    cur.execute("CREATE TABLE testWord (data varchar);")
    # cur.execute(f"INSERT into testWord(data) values ('piiza')")
    # DB = cur.execute(""" SELECT *  from testWord; """)

    records = cur.fetchall()
    print(records)
    cur.close()
# return(DB)

# add_word_to_db("pizza")