import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    HOST=config.get("DWH","DWH_HOST")
    DB_NAME=config.get("DWH","DWH_DB")
    DB_USER=config.get("DWH","DWH_DB_USER")
    DB_PASSWORD=config.get("DWH","DWH_DB_PASSWORD")
    DB_PORT=config.get("DWH","DWH_PORT")
    
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=HOST, port =DB_PORT)
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()