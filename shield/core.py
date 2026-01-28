import bcrypt
import os

class PasswordManager:
    def __init__(self, storage_path="accounts.txt"):
        self.storage_path = storage_path

    def _user_exists(self, login):
        if not os.path.exists(self.storage_path): return False
        with open(self.storage_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.split(":")[0] == login: return True
        return False

    def register_user(self, login, password):
        if self._user_exists(login):
            return {"status": "error", "message": "User already exists"}
        
        # Хешируем
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        with open(self.storage_path, "a", encoding="utf-8") as f:
            f.write(f"{login}:{hashed.decode('utf-8')}\n")
        
        return {"status": "success", "message": "Account created"}

    def check_user(self, login, password):
        if not os.path.exists(self.storage_path): return False
        
        with open(self.storage_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":")
                if parts[0] == login:
                    return bcrypt.checkpw(password.encode('utf-8'), parts[1].encode('utf-8'))
        return False
