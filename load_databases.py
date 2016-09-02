
def load_databases(connection):

    #create suppliers table
    connection.execute(
        "create table if not exists PROVEEDORES (ID integer primary key autoincrement, RUC text(13) unique not null, NOMBRE text(255) not null)")

    #create cathegories table
    connection.execute(
        "create table if not exists CATEGORIAS(ID integer primary key autoincrement, CATEGORIA text(255) unique not null)")

    #create invoices table
    connection.execute(
        "create table if not exists FACTURAS "
        "(ID integer primary key autoincrement, "
        "FECHA text(20) not null,  "
        "NUMERO text not null, "
        "PROVEEDOR integer not null, "
        "BASE double not null,"
        "CATEGORIA integer not null,"
        "foreign key (PROVEEDOR) references PROVEEDORES(ID),"
        "foreign key (CATEGORIA) references CATEGORIAS(ID))")

