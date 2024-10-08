from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def is_overdue(self):
        return datetime.now() > self.due_date and not self.completed

@app.route('/')
def index():
    tasks = Task.query.all()
    now = datetime.now()
    return render_template('index.html', tasks=tasks, now=now)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    due_date = request.form['due_date']
    due_date = datetime.strptime(due_date, '%Y-%m-%dT%H:%M')
    new_task = Task(title=title, due_date=due_date)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure the database and tables are created
    app.run(debug=True)