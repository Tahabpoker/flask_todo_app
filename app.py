from flask import Flask, render_template, url_for, redirect, flash
from flask import request as req
from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
app.secret_key = "oemhdomcpesfjwspfer"

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    data_created = db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self):
        return '<Task %r>' % self.id 


@app.route('/',methods=['GET','POST'])
def index():
    if req.method == "POST":
        task_content = req.form['content']
        if not task_content:
            return " enter valid task "
        
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            flash("Task added Successfully","success")
            return redirect('/')
        except:
            flash("error adding task", " error")
            return redirect('/')
        
    else:
        tasks = Todo.query.order_by(Todo.data_created).all()
        return render_template('index.html',tasks = tasks)
        

@app.route('/delete/<int:id>')
def delete_task(id:int):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        flash("Task deleted", "success")
        return redirect('/')
    except:
        flash("error deleteing task", "error")
        return redirect('/')


@app.route('/update/<int:id>',methods=['GET','POST'])
def update_task(id:int):
    task = Todo.query.get_or_404(id)
    if req.method == "POST":
        task_content = req.form['content']
        if not task_content:
            flash("Task cannot be empty","error")
        try:
            task.content = task_content
            db.session.commit()
            flash("Task updated", "success")
            return redirect('/')
        except:
            flash("error updating task","error")
            return redirect('/')

    else:
        return render_template('update.html',task = task)


if __name__ == '__main__':
    app.run(debug=True)

#31:00
