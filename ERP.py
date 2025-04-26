import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('school_erp.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    class TEXT NOT NULL,
                    age INTEGER NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    phone TEXT
                )''')

conn.commit()

# Functions
def register_student():
    name = input("Enter student name: ")
    std_class = input("Enter class: ")
    age = int(input("Enter age: "))
    cursor.execute("INSERT INTO students (name, class, age) VALUES (?, ?, ?)", (name, std_class, age))
    conn.commit()
    print("Student registered successfully.")

def register_teacher():
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")
    phone = input("Enter phone number: ")
    cursor.execute("INSERT INTO teachers (name, subject, phone) VALUES (?, ?, ?)", (name, subject, phone))
    conn.commit()
    print("Teacher registered successfully.")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def view_teachers():
    cursor.execute("SELECT * FROM teachers")
    for row in cursor.fetchall():
        print(row)

# Menu
def main():
    while True:
        print("\nSCHOOL ERP SYSTEM")
        print("1. Register Student")
        print("2. Register Teacher")
        print("3. View Students")
        print("4. View Teachers")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == '1':
            register_student()
        elif choice == '2':
            register_teacher()
        elif choice == '3':
            view_students()
        elif choice == '4':
            view_teachers()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main()
conn.close()
