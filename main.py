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
    description = db.Column(db.Text, default='')
    completed = db.Column(db.Boolean, default=False)

    def is_overdue(self):
        return datetime.now() > self.due_date and not self.completed
    
    def status(self):
        if self.completed:
            return 'completed'
        elif self.is_overdue():
            return 'overdue'
        else:
            return 'pending'

@app.route('/')
def index():
    status_filter = request.args.get('status', 'all')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    query = Task.query
    
    # Filter by status
    if status_filter == 'completed':
        query = query.filter_by(completed=True)
    elif status_filter == 'pending':
        query = query.filter_by(completed=False)
        query = query.filter(Task.due_date >= datetime.now())
    elif status_filter == 'overdue':
        query = query.filter_by(completed=False)
        query = query.filter(Task.due_date < datetime.now())
    
    # Filter by date range
    if start_date:
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        query = query.filter(Task.due_date >= start_dt)
    if end_date:
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
        end_dt = end_dt.replace(hour=23, minute=59, second=59)
        query = query.filter(Task.due_date <= end_dt)
    
    tasks = query.all()
    now = datetime.now()
    return render_template('index.html', tasks=tasks, now=now, status_filter=status_filter, start_date=start_date, end_date=end_date)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    due_date = request.form['due_date']
    description = request.form.get('description', '')
    due_date = datetime.strptime(due_date, '%Y-%m-%dT%H:%M')
    new_task = Task(title=title, due_date=due_date, description=description)
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

@app.route('/edit_task/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.title = request.form['title']
        task.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%dT%H:%M')
        task.description = request.form.get('description', '')
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure the database and tables are created
    app.run(debug=True)