from flask import Flask, render_template, request
import datetime
import json

app = Flask(__name__)

DB_FILE = "./data/db.json"  # Путь к файлу с сообщениями
db = open(DB_FILE, "rb")  # Открываем файл для чтения
data = json.load(db)  # Загрузить все файлы в формате JSON из файла
messages = data["messages"]  # Из полученных данных берём поле messeges

# Функция для сохранения всех сообщений(Messages) в файл
def save_messages_to_file():
    db = open(DB_FILE, "w")  # Открываем файл для записи
    data = {  # Созадём структуру для записи в файл
        "messages": messages
    }
    json.dump(data, db)  # Записываем стуктуру в файл


def add_message(name, text):  # Обьявим функцию, которая добавит сообщение в список
    now = datetime.datetime.now()
    new_message = {
        "name": name,
        "text": text,
        "time": now.strftime("%H:%M")
    }
    while True:
        if len(name) < 3 or len(name) > 100:
            print("ERROR")
            return (False)
        else:
            break
    while True:
        if len(text) < 1 or len(text) > 3000:
            print("ERROR")
            return (False)
        else:
            break
    messages.append(new_message)  # Добавляем новое сообщение в список
    save_messages_to_file()


def print_message(message):  # обьявляем функцию, которая печатает сообщение в список
    print(f"[{message['name']}] : {message['text']} / {message['time']}")

# Главная страница


@app.route("/")
def index_page():
    return "Здравствуйте, вас приветсвует СкиллЧат2022"

# Показать все сообщения в формате JSON


@app.route("/get_messages")
def get_messages():
    return {"messages": messages}

# Показать форму чата


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/send_message")
def send_message():
    # Получить имя и текст от пользователя
    text = request.args["text"]
    name = request.args["name"]
    # Вызвать функцию add_message
    add_message(name, text)
    return "OK"


app.run()  # Запускаем веб приложение
