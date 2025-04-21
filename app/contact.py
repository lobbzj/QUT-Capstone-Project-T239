from flask import Blueprint, request, redirect, render_template
import sqlite3

contactbp = Blueprint("contactbp", __name__)

def init_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@contactbp.route("/contact", methods=["POST"])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"Received: {name}, {email}, {message}")
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()
    return redirect("/")
