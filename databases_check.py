'''checks existence of dbs, tables or creates them'''

import sqlite3

def check(database):
    cursor = database.cursor()
    #suppliers

    #invoices

    #cathegories

    return

def create_suppliers(conn):
    '''crea el template de los suppliers, si no existe'''
    
    if exists_table(conn, "PROVEEDORES"):
        return
    else:
        conn.execute("create table PROVEEDORES (ID integer primary key autoincrement, RUC integer(13), NOMBRE text(255))")
    return

def create_invoices(conn):
    '''crea el template de las facturas, si no existe'''
    if exists_table(conn, "FACTURAS"):
        return
    else:
        conn.execute("create table FACTURAS (ID integer primary key autoincrement, NUMERO text, PROVEEDOR integer, foreign key (PROVEEDOR) references PROVEEDORES(ID))")
    return

def create_cathegories(conn):
    '''crea la tabla de categorias, si no existe'''
    if exists_table(conn, "CATEGORIAS"):
        return
    else:
        conn.execute("create table CATEGORIAS(ID integer primary key autoincrement, CATEGORIA text, unique(CATEGORIA))")
    #crea el template de la categoria de expense
    return

def exists_table(conn, t_name):
    cursor = conn.cursor()
    # table_count = cursor.execute("select count(*) from sqlite_master where type = 'table' and name = {tn}"\
    #                              .format(tn = t_name))

    table_count = cursor.execute("select count(*) from sqlite_master where name = :t_name and type= 'table'", {"t_name":t_name})
    return table_count.fetchone()[0]


if __name__ == '__main__':
    required_tables = ["PROVEEDORES", "FACTURAS", "CATEGORIAS"]
    existing_tables = []
    conn = sqlite3.connect("test.db")
    #print cursor.execute("")
    if exists_table(conn, "PROVEEDORES"):
        existing_tables.append("Proveedores")
    else:
        print "no exite"
        print "creando"
        create_suppliers(conn)

    if exists_table(conn, "FACTURAS"):
        print "tabla de facturas existe!"
    else:
       create_invoices(conn) 
