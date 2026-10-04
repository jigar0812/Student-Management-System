import re
from database.database import get_database_connection
EMAIL_PATTERN=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')

def validate_student(data):
    for field,label in [('name','Name'),('roll_no','Roll number'),('email','Email'),('course','Course')]:
        if not data.get(field,'').strip(): return f'{label} is required.'
    if not EMAIL_PATTERN.match(data['email'].strip()): return 'Please enter a valid email address.'
    return None

def student_exists(roll_no, exclude_id=None):
    c=get_database_connection()
    try:
        q='SELECT 1 FROM students WHERE roll_no=?' if exclude_id is None else 'SELECT 1 FROM students WHERE roll_no=? AND id!=?'
        args=(roll_no,) if exclude_id is None else (roll_no,exclude_id)
        return c.execute(q,args).fetchone() is not None
    finally: c.close()

def add_student(d):
    c=get_database_connection()
    try:
        x=c.execute('INSERT INTO students(name,roll_no,email,course) VALUES(?,?,?,?)',(d['name'],d['roll_no'],d['email'],d['course'])); c.commit(); return x.lastrowid
    finally: c.close()

def get_all_students():
    c=get_database_connection()
    try: return c.execute('SELECT * FROM students ORDER BY id DESC').fetchall()
    finally: c.close()

def get_student(i):
    c=get_database_connection()
    try: return c.execute('SELECT * FROM students WHERE id=?',(i,)).fetchone()
    finally: c.close()

def update_student(i,d):
    c=get_database_connection()
    try:
        x=c.execute('UPDATE students SET name=?,roll_no=?,email=?,course=? WHERE id=?',(d['name'],d['roll_no'],d['email'],d['course'],i)); c.commit(); return x.rowcount>0
    finally: c.close()

def delete_student(i):
    c=get_database_connection()
    try:
        x=c.execute('DELETE FROM students WHERE id=?',(i,)); c.commit(); return x.rowcount>0
    finally: c.close()

def search_students(q):
    if not q: return get_all_students()
    c=get_database_connection(); p=f'%{q}%'
    try: return c.execute('SELECT * FROM students WHERE name LIKE ? OR roll_no LIKE ? OR email LIKE ? OR course LIKE ? ORDER BY id DESC',(p,p,p,p)).fetchall()
    finally: c.close()
