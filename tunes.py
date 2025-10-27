# os is a module that lets us access the file system

import os 
import sqlite3
# sqlite for connecting to sqlite embedded database

# An example of how to create a table, insert data
# and run a select query
def do_databasse_stuff():

    conn = sqlite3.connect('tunes.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)')

    # Insert data
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('John', 30))

    # Save changes
    conn.commit()

    cursor.execute('SELECT * FROM users')

    # Get all results
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close
    conn.close()


books_dir = "abc_books"

def process_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    # list comprehension to strip the \n's
    lines = [line.strip() for line in lines]

    # just print the files for now
    for line in lines:
        # print(line)
        pass


do_databasse_stuff()

# Iterate over directories in abc_books
for item in os.listdir(books_dir):
    # item is the dir name, this makes it into a path
    item_path = os.path.join(books_dir, item)
    
    # Check if it's a directory and has a numeric name
    if os.path.isdir(item_path) and item.isdigit():
        print(f"Found numbered directory: {item}")
        
        # Iterate over files in the numbered directory
        for file in os.listdir(item_path):
            # Check if file has .abc extension
            if file.endswith('.abc'):
                file_path = os.path.join(item_path, file)
                print(f"  Found abc file: {file}")
                process_file(file_path)