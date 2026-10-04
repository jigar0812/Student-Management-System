from flask import Flask, render_template, request, redirect, url_for, flash
from services.student_service import *
from database.database import initialize_database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'student-management-demo-key'

@app.route('/')
def index():
    return render_template('index.html', students=get_all_students())

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        data = {k: request.form.get(k,'').strip() for k in ('name','roll_no','email','course')}
        error = validate_student(data)
        if error or student_exists(data['roll_no']):
            flash(error or 'Roll number already exists.', 'danger')
            return render_template('add_student.html', student=data)
        add_student(data); flash('Student added successfully.','success'); return redirect(url_for('index'))
    return render_template('add_student.html', student={})

@app.route('/edit/<int:student_id>', methods=['GET','POST'])
def edit(student_id):
    student = get_student(student_id)
    if not student: flash('Student not found.','danger'); return redirect(url_for('index'))
    if request.method == 'POST':
        data = {k: request.form.get(k,'').strip() for k in ('name','roll_no','email','course')}
        error = validate_student(data)
        if error or student_exists(data['roll_no'], student_id):
            flash(error or 'Roll number already exists.','danger'); data['id']=student_id
            return render_template('edit_student.html', student=data)
        update_student(student_id,data); flash('Student updated successfully.','success'); return redirect(url_for('index'))
    return render_template('edit_student.html', student=student)

@app.post('/delete/<int:student_id>')
def delete(student_id):
    flash('Student deleted successfully.' if delete_student(student_id) else 'Student not found.', 'success')
    return redirect(url_for('index'))

@app.route('/search')
def search():
    q=request.args.get('q','').strip()
    return render_template('index.html', students=search_students(q), search_query=q)

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
