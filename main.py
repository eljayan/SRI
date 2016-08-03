#this is a program that records my invoices from sri
import sqlite3
from databases_check import check

def main():
    #create a connection to db or create it
    connection = sqlite3.Connection("sri.db")

    #test if the tables exist, if not create them
    check(connection)

    #load gui

    #perform operations
