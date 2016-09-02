#this is a program that records my invoices from sri
import sqlite3
from load_databases import load_databases

def main():
    #create a connection to db or create it

    connection = sqlite3.Connection("sri.db")

    #load or create databases
    load_databases(connection)

    #load gui

    #perform operations

if __name__ == "__main__":
    main()
