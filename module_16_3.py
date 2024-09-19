# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Цель: выработать навык работы с CRUD запросами.

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_dict():
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age")]):
    user_id = str(int(max(users, key=int)) + 1) # Генерируем новый ID пользователя, увеличивая максимальный
    # существующий ID на 1.
    users[user_id] = f"Имя: {username}, возраст: {age}" # Добавляем нового пользователя в словарь users
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path()],
                      username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age")]):
    users[user_id] = f"Имя: {username}, возраст: {age}" # обновляются данные существующего пользователя
    # по указанному user_id
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[str, Path()]):
    del users[user_id]
    return f"User {user_id} has been deleted"

