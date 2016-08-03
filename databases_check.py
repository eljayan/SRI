#checks existence of dbs or creates them
import sqlite3

def check(database):
    cursor = database.cursor()
    #suppliers

    #invoices

    #cathegories

    return

def create_suppliers(cursor):
    #crea el template de los suppliers
    return

def create_invoices(cursor):
    #crea el template de las facturas
    return

def create_cathegories(cursor):
    #crea el template de la categoria de expense
    return

def exists_table(db, t_name):
    cursor = db.cursor()
    table_count = cursor.execute("SELECT count(*) FROM {dbn} WHERE type = 'table' AND name = {tn}"\
                                 .format(dbn = db, tn = t_name))
    return table_count

if __name__ == '__main__':
    conn = sqlite3.Connection("test.db")
    cursor = conn.cursor()
    #print cursor.execute("")
    print exists_table(conn, "PROVEEDORES")