# 🛡️ Shield-Auth

[![PyPI version](https://img.shields.io/pypi/v/shield-auth.svg)](https://pypi.org/project/shield-auth/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/shield-auth.svg)](https://pypi.org/project/shield-auth/)
[![Downloads](https://img.shields.io/pypi/dm/shield-auth)](https://pypi.org/project/shield-auth/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/yourusername/shield-auth/actions/workflows/tests.yml/badge.svg)](https://github.com/yourusername/shield-auth/actions)
[![Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen)](https://github.com/yourusername/shield-auth)

**Shield-Auth** — профессиональная Python-библиотека для создания легковесных систем регистрации и авторизации. Идеальное решение для проектов, где важна безопасность, но нет необходимости в тяжелых базах данных. Все данные надежно защищены и хранятся в простом текстовом файле.

## ✨ Особенности

- 🔐 **Надежное хеширование** с использованием bcrypt
- 🧂 **Уникальная соль** для каждого пароля
- 📁 **Работа с текстовым файлом** — не требуется СУБД
- 🚀 **Простой API** — всего 2 основных метода
- 🛡️ **Защита от атак** — перебора и словарных атак
- 🐍 **Python 3.8+** — поддержка современных версий Python
- 📊 **Встроенная валидация** — проверка сложности пароля
- 🔄 **Атомарные операции** — гарантия целостности данных
- 📝 **Подробное логирование** — для отладки и аудита

## 📦 Установка

```bash
pip install shield-auth
Или для последней разработческой версии:

bash
pip install git+https://github.com/yourusername/shield-auth.git
🚀 Быстрый старт
python
from shield_auth import PasswordManager

# Инициализация системы (файл создается автоматически)
auth = PasswordManager(db_file="users.txt")

# Регистрация нового пользователя
result = auth.register_user("alice", "SecurePass123!")
print(result["message"])

# Авторизация пользователя
if auth.check_user("alice", "SecurePass123!"):
    print("✅ Авторизация успешна!")
else:
    print("❌ Неверные учетные данные")
📚 Полная документация
1. Подключение и инициализация
Класс PasswordManager — это основная точка входа. При создании объекта библиотека проверяет наличие файла базы данных и, если его нет, создает его автоматически.

python
from shield_auth import PasswordManager

# Аргумент db_file: путь к вашему .txt файлу с аккаунтами
db = PasswordManager(db_file="accounts.txt")
Дополнительные параметры:

python
db = PasswordManager(
    db_file="accounts.txt",
    min_password_length=8,      # Минимальная длина пароля
    require_special_chars=True, # Требовать спецсимволы
    hash_rounds=12              # Количество раундов bcrypt
)
2. Регистрация пользователя: register_user(login, password)
Метод для создания новой учетной записи. Использует алгоритм bcrypt с адаптивной солью.

Параметры:

login (string): Уникальное имя пользователя

password (string): Пароль в открытом виде

Возвращаемое значение (dict):

json
{
    "status": "success", 
    "message": "User registered successfully"
}
или

json
{
    "status": "error", 
    "message": "Username already exists"
}
Пример использования:

python
res = db.register_user("admin_user", "my_secure_password_2026")
if res["status"] == "success":
    print(f"✅ {res['message']}")
else:
    print(f"❌ {res['message']}")
3. Авторизация: check_user(login, password)
Метод для проверки введенных данных при входе. Сравнивает присланный пароль с зашифрованным хешем в базе.

Параметры:

login (string): Логин пользователя

password (string): Пароль для проверки

Возвращаемое значение (bool):

True: Логин существует и пароль верен

False: Ошибка в логине или пароле

Пример:

python
if db.check_user("admin_user", "my_secure_password_2026"):
    print("🔓 Доступ открыт!")
else:
    print("🔒 Неверные данные.")
4. Дополнительные методы
python
# Проверка существования пользователя
if db.user_exists("alice"):
    print("Пользователь существует")

# Получение информации о пользователе
user_info = db.get_user_info("alice")

# Удаление пользователя (требует подтверждения пароля)
result = db.delete_user("alice", "password")
🔒 Безопасность
Библиотека разработана с учетом современных требований к кибербезопасности:

🏰 Технологии защиты
Технология	Назначение	Уровень защиты
Bcrypt	Хеширование паролей	12 раундов вычислений
Unique Salt	Защита от Rainbow Tables	128-бит случайная соль
Timing-safe	Защита от timing attacks	Постоянное время сравнения
Input Validation	Предотвращение инъекций	Строгая валидация ввода
📊 Сравнение безопасности
python
# Стандартное хеширование (НЕ БЕЗОПАСНО)
hash("password")  # Легко взломать

# Shield-Auth (БЕЗОПАСНО)
bcrypt.hashpw(password + unique_salt, bcrypt.gensalt(rounds=12))
🚫 Защита от атак
Брутфорс атаки — bcrypt замедляет перебор до 100 попыток/сек

Rainbow Tables — уникальная соль для каждого пароля

Timing Attacks — постоянное время проверки хешей

Инъекции — строгая валидация всех входных данных

🌐 Пример использования с Flask (Backend)
python
from flask import Flask, request, jsonify, session
from shield_auth import PasswordManager
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
auth_system = PasswordManager("database.txt")

# Декоратор для защиты маршрутов
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['POST'])
def register():
    """Регистрация нового пользователя"""
    data = request.json
    user = data.get('username')
    pwd = data.get('password')
    email = data.get('email', '')
    
    if not user or not pwd:
        return jsonify({"error": "Missing credentials"}), 400
    
    result = auth_system.register_user(user, pwd)
    return jsonify(result)

@app.route('/login', methods=['POST'])
def login():
    """Авторизация пользователя"""
    data = request.json
    user = data.get('username')
    pwd = data.get('password')
    
    if auth_system.check_user(user, pwd):
        session['user_id'] = user
        session['logged_in'] = True
        return jsonify({
            "status": "success", 
            "user": user,
            "message": "Login successful"
        })
    
    return jsonify({
        "status": "error", 
        "message": "Invalid credentials"
    }), 401

@app.route('/profile', methods=['GET'])
@login_required
def profile():
    """Защищенный маршрут"""
    return jsonify({
        "user": session['user_id'],
        "message": "Welcome to your profile!"
    })

@app.route('/logout', methods=['POST'])
def logout():
    """Выход из системы"""
    session.clear()
    return jsonify({"message": "Logged out successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
🎯 Пример использования с FastAPI
python
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from shield_auth import PasswordManager

app = FastAPI(title="Shield-Auth API")
security = HTTPBasic()
auth_system = PasswordManager("fastapi_users.txt")

class UserRegistration(BaseModel):
    username: str
    password: str
    email: str = None

@app.post("/register")
async def register(user_data: UserRegistration):
    """Регистрация нового пользователя"""
    result = auth_system.register_user(
        user_data.username, 
        user_data.password
    )
    
    if result["status"] == "error":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["message"]
        )
    
    return {"message": "Registration successful"}

@app.get("/protected")
async def protected_route(
    credentials: HTTPBasicCredentials = Depends(security)
):
    """Защищенный маршрут с базовой аутентификацией"""
    if auth_system.check_user(credentials.username, credentials.password):
        return {
            "message": f"Welcome {credentials.username}!",
            "access": "granted"
        }
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"}
    )
📁 Структура файла базы данных
text
# Формат: username:hash:salt:created_at
alice:$2b$12$...:a1b2c3d4e5f6:2024-01-15 10:30:00
bob:$2b$12$...:f6e5d4c3b2a1:2024-01-15 11:45:00
🔧 Расширенные возможности
Кастомные валидаторы паролей
python
from shield_auth import PasswordManager

class CustomPasswordManager(PasswordManager):
    def validate_password(self, password):
        """Расширенная валидация пароля"""
        errors = []
        
        if len(password) < self.min_password_length:
            errors.append(f"Password must be at least {self.min_password_length} characters")
        
        if not any(c.isupper() for c in password):
            errors.append("Password must contain at least one uppercase letter")
        
        if not any(c.isdigit() for c in password):
            errors.append("Password must contain at least one digit")
        
        return errors

auth = CustomPasswordManager("users.txt")
Миграция из других систем
python
def migrate_from_json(json_file, target_file):
    """Миграция пользователей из JSON в Shield-Auth"""
    import json
    from shield_auth import PasswordManager
    
    auth = PasswordManager(target_file)
    
    with open(json_file, 'r') as f:
        users = json.load(f)
    
    for user in users:
        auth.register_user(user['login'], user['password'])
    
    print(f"Migrated {len(users)} users successfully")
📊 Бенчмарки
text
Регистрация пользователя: ~250ms (12 раундов bcrypt)
Авторизация пользователя: ~250ms
Потребление памяти: < 10MB
Размер файла: ~150 байт на пользователя
🐛 Отладка и логирование
python
import logging

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("shield_auth")

# Включение отладочного режима
auth = PasswordManager("users.txt", debug=True)
🤝 Вклад в проект
Мы приветствуем вклад в развитие Shield-Auth!

Форкните репозиторий

Создайте ветку для фичи (git checkout -b feature/amazing-feature)

Закоммитьте изменения (git commit -m 'Add amazing feature')

Запушьте ветку (git push origin feature/amazing-feature)

Откройте Pull Request