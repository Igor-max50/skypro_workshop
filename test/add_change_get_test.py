import requests

def test_add_change_get():
    body = {"title": "My task","completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json = body)
    id = response.json()["id"]
    
    print("получили id")
    print(id)

    body = {"completed": True}
    path = "https://todo-app-sky.herokuapp.com/{id}".format(id = id, json = body)

    print("путь")
    print(path)

    response = requests.patch("https://todo-app-sky.herokuapp.com/{id}".format(id = id, json = body))

    response = requests.get("https://todo-app-sky.herokuapp.com/{id}".format(id = id))
    completed = response.json()["completed"]

    print("получили ответ")
    print(completed)

    assert response['completed'] == True