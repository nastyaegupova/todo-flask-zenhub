from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    html = """
    <h1>Todo App</h1>

    <form action="/add" method="post">
        <input type="text" name="task">
        <button type="submit">Add</button>
    </form>

    <ul>
    """

    for i, task in enumerate(tasks):
        html += f"""
        <li>
            {task}
            <a href="/delete/{i}">Delete</a>
        </li>
        """

    html += "</ul>"

    return html

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task and task.strip() != "":
        tasks.append(task)
        return redirect("/")

    return """
    <script>
        alert('Task cannot be empty!');
        window.location.href = '/';
    </script>
    """

@app.route("/delete/<int:index>")
def delete_task(index):
    tasks.pop(index)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)