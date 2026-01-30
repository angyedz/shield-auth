from passlib.context import CryptContext
import os

# Инициализируем контекст для хеширования паролей
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

class PasswordManager:
    def __init__(self, storage_path="accounts.txt"):
        self.storage_path = storage_path

    def _user_exists(self, login):
        if not os.path.exists(self.storage_path): 
            return False
        with open(self.storage_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.split(":")[0] == login: 
                    return True
        return False

    def register_user(self, login, password):
        if self._user_exists(login):
            return {"status": "error", "message": "User already exists"}
        
        # Хешируем через passlib
        hashed = pwd_context.hash(password)
        
        with open(self.storage_path, "a", encoding="utf-8") as f:
            f.write(f"{login}:{hashed}\n")
        
        return {"status": "success", "message": "Account created"}

    def check_user(self, login, password):
        if not os.path.exists(self.storage_path): 
            return False
        
        with open(self.storage_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":", 1)  # Split только на первый ':'
                if parts[0] == login:
                    try:
                        return pwd_context.verify(password, parts[1])
                    except:
                        return False
        return False
