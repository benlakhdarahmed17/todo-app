from flask import Flask, redirect, render_template, request, url_for, abort
from todo_repository import TodoRepository

app = Flask(__name__)
todos_repository = TodoRepository()


@app.route("/")
def index():
    todos = todos_repository.get_todos()
    return render_template("home.html", todos=todos)


@app.route("/addtodo", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        todoname = request.form['todoname']
        urgency = request.form['urgency']
        todos_repository.add_todo(todoname, urgency)
        return redirect(url_for('index'))

    return render_template("Add_todo.html")


@app.route("/<int:id>", methods=['GET', 'POST'])
def details(id):
    todo = todos_repository.get_todo_by_id(id)
    if todo is None:
        abort(404)

    if request.method == 'POST':
        todo.completed = True

    return render_template("todo_details.html", todo=todo)
