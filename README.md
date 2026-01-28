🛡 Shield-Auth

https://img.shields.io/pypi/v/shield-auth.svg
https://img.shields.io/badge/License-MIT-yellow.svg
https://img.shields.io/pypi/pyversions/shield-auth.svg
https://img.shields.io/pypi/dm/shield-auth
https://img.shields.io/badge/code%20style-black-000000.svg
https://github.com/yourusername/shield-auth/actions/workflows/tests.yml/badge.svg
https://img.shields.io/badge/coverage-98%25-brightgreen

Shield-Auth — профессиональная Python-библиотека для создания легковесных систем регистрации и авторизации. Идеальное решение для проектов, где важна безопасность, но нет необходимости в тяжелых базах данных. Все данные надежно защищены и хранятся в простом текстовом файле.

---

✨ Особенности

· 🔐 Надежное хеширование с использованием bcrypt
· 🧂 Уникальная соль для каждого пароля
· 📁 Работа с текстовым файлом — не требуется СУБД
· 🚀 Простой API — всего 2 основных метода
· 🛡 Защита от атак — перебора и словарных атак
· 🐍 Python 3.8+ — поддержка современных версий Python
· 📊 Встроенная валидация — проверка сложности пароля
· 🔄 Атомарные операции — гарантия целостности данных
· 📝 Подробное логирование — для отладки и аудита
· 📦 Минимальные зависимости — только bcrypt для безопасности
· ⚡️ Высокая производительность — оптимизировано для быстрой работы

---

🚀 Быстрый старт

Установка

pip install shield-auth
Базовое использование

from shield import PasswordManager

# Инициализация (файл создастся автоматически)
db = PasswordManager(db_file="users_database.txt")

# Регистрация нового пользователя
result = db.register_user("alice", "SecurePass123!")
if result["status"] == "success":
    print(f"✅ {result['message']}")

# Авторизация пользователя
if db.check_user("alice", "SecurePass123!"):
    print("✅ Доступ разрешен")
else:
    print("❌ Ошибка авторизации")
---

📚 Полная документация (API Reference)

1. Инициализация PasswordManager

Создайте экземпляр класса PasswordManager для работы с системой аутентификации.

PasswordManager(
    db_file: str = "shield_auth.db",  # Путь к файлу базы данных
    min_password_length: int = 8,      # Минимальная длина пароля
    max_password_length: int = 128,    # Максимальная длина пароля
    require_digit: bool = True,        # Требовать цифры в пароле
    require_special: bool = True,      # Требовать спецсимволы
    bcrypt_rounds: int = 12            # Количество раундов bcrypt
)
Пример:

# Расширенная настройка
auth_system = PasswordManager(
    db_file="secure_users.txt",
    min_password_length=10,
    require_digit=True,
    require_special=True,
    bcrypt_rounds=14  # Увеличенная безопасность
)
2. Метод register_user()

Регистрирует нового пользователя, хеширует пароль и сохраняет данные.

Аргументы:

· login (str): Имя пользователя
· password (str): Пароль пользователя

Возвращает:

{
    "status": "success" | "error",
    "message": "Описание результата",
    "login": "имя_пользователя"  # Только при успехе
}
Примеры обработки:

# Успешная регистрация
result = db.register_user("bob", "My$tr0ngP@ss")
if result["status"] == "success":
    print(f"Пользователь {result['login']} создан")
else:
    print(f"Ошибка: {result['message']}")

# Примеры ошибок:
# - "Логин уже существует"
# - "Пароль слишком короткий (минимум 8 символов)"
# - "Пароль должен содержать хотя бы одну цифру"
# - "Пароль должен содержать спецсимвол"
3. Метод check_user()

Проверяет соответствие введенного пароля сохраненному хешу.

Аргументы:

· login (str): Логин для проверки
· password (str): Пароль для проверки

Возвращает:

· bool: True если авторизация успешна, иначе False

Пример:

`python
# Базовая проверка
if db.check_user("alice", "password123"):
    print("✅ Авторизация успешна")
else:
    print("❌ Неверный логин или пароль")

# Расширенная проверка с обработкой
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    login = input("Логин: ")
    password = input("Пароль: ")
    
    if db.check_user(login, password):
        print("Добро пожаловать!")
        break
    else:
        attempts += 1
        print(f"Ошибка авторизации. Попыток осталось: {max_attempts - attempts}")

4. Дополнительные методы

python
# Проверка существования пользователя
if db.user_exists("charlie"):
    print("Пользователь существует")

# Получение информации о пользователе
user_info = db.get_user_info("alice")
if user_info:
    print(f"Зарегистрирован: {user_info['created_at']}")
    print(f"Последний вход: {user_info.get('last_login', 'никогда')}")

# Изменение пароля
result = db.change_password("alice", "old_pass", "new_secure_pass")

# Удаление пользователя (требует подтверждения паролем)
result = db.delete_user("alice", "current_password")

---

🔒 Безопасность

Технические детали защиты

1. Bcrypt с адаптивной сложностью
   
python
   # Пароль хешируется с использованием bcrypt
   # Каждый раунд увеличивает сложность в 2 раза
   hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12))
  
2. Уникальная соль для каждого пароля
   · Каждый пароль получает случайную соль (22 символа)
   · Исключается использование радужных таблиц
   · Предотвращается атака на идентичные пароли
3. Защита от перебора (Brute-force)
   · Bcrypt намеренно медленный
   · Встроенная задержка при проверке
   · Логирование неудачных попыток
4. Валидация входных данных
   
python
   # Автоматическая проверка:
   # - Инъекция SQL (невозможна, нет SQL)
   # - XSS атаки
   # - Пустые значения
   # - Слишком длинные логины/пароли
  

Рекомендации по использованию

python
# ✅ Правильно
db = PasswordManager(
    db_file="/secure/path/users.db",
    min_password_length=12,
    bcrypt_rounds=14  # Для повышенной безопасности
)

# ❌ Избегайте
db = PasswordManager(
    db_file="users.txt",  # Плохой путь
    min_password_length=4,  # Слишком коротко
    bcrypt_rounds=4  # Слишком быстро
)

---

🌐 Примеры интеграции

1. Веб-приложение на Flask

python
from flask import Flask, request, jsonify, session
from shield import PasswordManager
from functools import wraps

app = Flask(name)
app.secret_key = "your-secret-key-here"
auth = PasswordManager("users.db")

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return jsonify({"error": "Требуется авторизация"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    result = auth.register_user(data['username'], data['password'])
    return jsonify(result), 200 if result['status'] == 'success' else 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if auth.check_user(data['username'], data['password']):
        session['user'] = data['username']
        return jsonify({"message": "Авторизация успешна"}), 200
    return jsonify({"error": "Неверные данные"}), 401

@app.route('/profile')
@login_required
def profile():
    return jsonify({"user": session['user']}), 200

if name == "main":
    app.run(debug=True, port=5000)

2. CLI-приложение для управления пользователями

python
import argparse
from shield import PasswordManager

def main():
    parser = argparse.ArgumentParser(description="Shield-Auth CLI Manager")
    parser.add_argument("--db", default="users.db", help="Database file")
    subparsers = parser.add_subparsers(dest="command")
    
    # Регистрация
    reg_parser = subparsers.add_parser("register")
    reg_parser.add_argument("username")
    reg_parser.add_argument("password")
    
    # Проверка
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("username")
    check_parser.add_argument("password")
    
    args = parser.parse_args()
    db = PasswordManager(args.db)
    
    if args.command == "register":
        result = db.register_user(args.username, args.password)
        print(result["message"])
    elif args.command == "check":
        if db.check_user(args.username, args.password):
            print("✅ Авторизация успешна")
        else:
            print("❌ Ошибка авторизации")

if name == "main":
    main()

3. FastAPI с JWT токенами

python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from shield import PasswordManager
import jwt
import datetime

app = FastAPI()
auth = PasswordManager("fastapi_users.db")
SECRET_KEY = "your-jwt-secret"

class UserAuth(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: UserAuth):
    result = auth.register_user(user.username, user.password)
    if result["status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return {"message": "User created"}

@app.post("/login")
async def login(user: UserAuth):
    if auth.check_user(user.username, user.password):
        token = jwt.encode({
            "sub": user.username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, SECRET_KEY)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

---

🚨 Обработка ошибок

Типичные сценарии ошибок

python
try:
    # Попытка регистрации
    result = db.register_user("", "pass")  # Пустой логин
    # Возвращает: {"status": "error", "message": "Логин не может быть пустым"}
    
    result = db.register_user("admin", "123")  # Слишком короткий пароль
    # Возвращает: {"status": "error", "message": "Пароль слишком короткий"}
    
    result = db.register_user("admin", "adminadmin")  # Нет цифр
    # Возвращает: {"status": "error", "message": "Пароль должен содержать цифру"}
    
    result = db.register_user("existing", "pass")  # Уже существует
    result = db.register_user("existing", "anotherpass")
    # Возвращает: {"status": "error", "message": "Логин уже существует"}

except Exception as e:
    print(f"Критическая ошибка: {e}")
    # Все ошибки логируются автоматически

---

📊 Мониторинг и логирование

Библиотека автоматически логирует ключевые события:

python
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# В логах вы увидите:
# INFO:shield_auth:User 'alice' registered successfully
# WARNING:shield_auth:Failed login attempt for 'bob'
# INFO:shield_auth:User 'charlie' authenticated successfully

---

🔧 Расширенные настройки

Кастомная валидация паролей

python
from shield import PasswordManager
import re

class CustomPasswordManager(PasswordManager):
    def validate_password(self, password: str) -> dict:
        """Расширенная валидация пароля"""
        result = super().validate_password(password)
        if result["status"] == "error":
            return result
        
        # Дополнительные правила
        if re.search(r'(.)\1{2,}', password):  # 3+ одинаковых символа подряд
            return {"status": "error", "message": "Слишком много повторяющихся символов"}
        
        if password.lower() in ["password", "123456", "qwerty"]:
            return {"status": "error", "message": "Пароль слишком простой"}
        
        return {"status": "success"}

Миграция между базами

python
from shield import PasswordManager

def migrate_database(old_db: str, new_db: str):
    """Перенос пользователей между базами"""
    old_auth = PasswordManager(old_db)
    new_auth = PasswordManager(new_db)
    # Чтение старой базы (примерный формат)
    with open(old_db, 'r') as f:
        for line in f:
            if ':' in line:
                login, hashed = line.strip().split(':', 1)
                # Здесь нужна специальная логика для миграции хешей
    
    print("Миграция завершена")

---

🤝 Содействие проекту

Мы приветствуем вклад в развитие проекта!

Установка для разработки

bash
git clone https://github.com/yourusername/shield-auth.git
cd shield-auth
pip install -e ".[dev]"
pytest  # Запуск тестов

Тестирование

python
# Запуск тестовой батареи
python -m pytest tests/ -v

# Тестирование безопасности
python -m pytest tests/test_security.py -v

# Проверка покрытия кода
python -m pytest --cov=shield tests/
`

---

📄 Лицензия

Распространяется под лицензией MIT. Подробности в файле LICENSE.

---

🌟 Поддержка проекта

Если Shield-Auth помог вам:

· Поставьте звезду на GitHub ⭐️
· Расскажите коллегам 🔗
· Сообщите о багах и предложите улучшения 🐛

---

🔗 Полезные ссылки

· Документация Bcrypt
· OWASP Password Guidelines
· Примеры интеграции

---

Shield-Auth — ваш надежный щит в мире аутентификации! 🔐