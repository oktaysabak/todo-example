# Todo Application
Create, Update, Delete, List todos. Each user can CRUD own todos.

Tech Stack:
- Django
- Django Rest Framework
- Jquery
- Bootstrap

# Setup
Create environment
```bash
python3 -m virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver
```
Default *username: admin, password: 12345678*

## REST API
<details>
<summary>Click to read!</summary>

### Obtain Token
```bash
curl --location --request POST 'localhost:8000/api/token-auth' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "12345678"
}'
```
```json
{
    "token": "18bea1824e361bb23a3be447fe97964c03cdd59d"
}
```

### Get list of todos
```bash
curl --location --request GET 'http://localhost:8000/api/todos/' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d'
```
```json
HTTP/1.1 200 OK
[
    {
        "id": 2,
        "content": "Todo 2",
        "done": true
    },
    {
        "id": 1,
        "content": "Todo 1",
        "done": false
    }
]
```

### Retrieve detail of todo item
```bash
curl --location --request GET 'http://localhost:8000/api/todos/1/' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d'
```
```json
HTTP/1.1 200 OK
{
    "id": 1,
    "content": "Todo 1",
    "done": false
}

```

### Create a todo item
```bash
curl --location --request POST 'http://localhost:8000/api/todos/' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d' \
--header 'Content-Type: application/json' \
--data-raw '{
    "content": "Todo 3",
    "done": false
}'
```
```json
HTTP/1.1 201 CREATED
{
    "content": "Todo 3",
    "done": false
}
```

### Update existing todo item
```bash
curl --location --request PUT 'http://localhost:8000/api/todos/3/' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d' \
--header 'Content-Type: application/json' \
--data-raw '{
    "content": "Todo 3",
    "done": true
}'
```
```json
HTTP/1.1 200 OK
{
    "id": 3,
    "content": "Todo 3",
    "done": true
}
```
### Delete existing todo item
```bash
curl --location --request DELETE 'http://localhost:8000/api/todos/3/' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d'
```
```json
HTTP/1.1 204 NO CONTENT
{
    "id": null,
    "content": "Todo 3",
    "done": true
}
```
### Filtering todo items by `content`
 ```bash
 curl --location --request GET 'http://localhost:8000/api/todos/?search=todo' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d'
 ```
```json
[
    {
        "id": 3,
        "content": "Todo 3",
        "done": true
    },
    {
        "id": 2,
        "content": "Todo 2",
        "done": false
    }
]
```
### Filtering  todo items by `status`
 ```bash
curl --location --request GET 'http://localhost:8000/api/todos/?done=false' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d'
 ```
```json
[
    {
        "id": 2,
        "content": "Todo 2",
        "done": false
    }
]
```

### Filtering todo items  `content` and `status`
 ```bash
curl --location --request GET 'http://localhost:8000/api/todos/?seacrh=todo&done=true' \
--header 'Authorization: Token 18bea1824e361bb23a3be447fe97964c03cdd59d'
 ```
```json
[
    {
        "id": 3,
        "content": "Todo 3",
        "done": true
    }
]
```
</details>

## User Interface
<details>
<summary>Click to read!</summary>

### Login
Default *username: admin, password: 12345678*
Login via django admin [login url](http://localhost:8000/admin/login/) than go to [index page](http://localhost:8000/)

Use interface to CRUD todo items. 

Functions:
- Click `Add` to create todo item with status `Not Completed`
- Click item detail to go item detail.
- Click `Update` to update existing todo content or status.
- Click `Delete` to delete existing item.
- Fill `Search` input, select todo `status`  and click `Search` to filter todo items on home page. 
</details>