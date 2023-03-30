import requests

def test_add_change_get():
    body = {"title": "My task","completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json = body)
    id = response.json()["id"]

    body = {"completed": True}
    path = "https://todo-app-sky.herokuapp.com/{id}".format(id = id, json = body)

    response = requests.patch(path, json = body)

    response = requests.get(path.format(id = id))
    completed = response.json()["completed"]

    assert response.json()['completed'] == True