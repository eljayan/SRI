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
    # table_count = cursor.execute("select count(*) from sqlite_master where type = 'table' and name = {tn}"\
    #                              .format(tn = t_name))

    table_count = cursor.execute("select count(*) from sqlite_master where name = :t_name and type= 'table'", {"t_name":t_name})
    return table_count.fetchone()[0]


if __name__ == '__main__':
    conn = sqlite3.Connection("test.db")
    cursor = conn.cursor()
    #print cursor.execute("")
    if exists_table(conn, "PROVEEDORE"):
        print "si existe!"
    else:
        print "no exite"