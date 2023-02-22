# Mini-projet avec CherryPy
CherryPy est un framework minimaliste orientée objet en python. Dans ce miniprojet, on a construit un `todolist`
## Le code : 
```python
import cherrypy

class TodoList(object):
    def __init__(self):
        self.tasks = []
    
    @cherrypy.expose
    def index(self):
        # Afficher la liste des tâches
        html = "<h1>Todolist</h1>"
        html += "<ul>"
        for i, task in enumerate(self.tasks):
            html += f"<li>{task} <a href='/remove_task?task_id={i}'>Supprimer</a></li>"
        html += "</ul>"
        html += "<form method='post' action='/add_task'>"
        html += "<input type='text' name='task' />"
        html += "<input type='submit' value='Ajouter' />"
        html += "</form>"
        return html
    
    @cherrypy.expose
    def add_task(self, task):
        # Ajouter une nouvelle tâche
        self.tasks.append(task)
        raise cherrypy.HTTPRedirect('/')
    
    @cherrypy.expose
    def remove_task(self, task_id):
        # Supprimer une tâche
        task_id = int(task_id)
        if task_id >= 0 and task_id < len(self.tasks):
            del self.tasks[task_id]
        raise cherrypy.HTTPRedirect('/')
    
if __name__ == '__main__':
    cherrypy.quickstart(TodoList())
```

Pour tester l'application: 
exécutez le script Python `app.py` et en ouvrez votre navigateur à l'adresse `http://localhost:8080`.
