#! /usr/bin/env python3                                                            
import sqlite3

def get_database():
    return sqlite3.connect('output/emscharts.sqlite3')

def get_cursor():
    cursor = get_database().cursor

def setup_database():
    conn = get_database()
    cursor = conn.cursor()

    # Setup chart table
    cursor.execute("""
    create table charts (
        id int,
        prid text,
        dispatch_id text
    )
    """)
    conn.commit()


    # Setup member and member_call tables
    cursor.execute("create table members (id int, name text)")
    conn.commit()

    cursor.execute("create table member_charts (call_id int, member_id)")
    conn.commit()

    conn.close()
    
