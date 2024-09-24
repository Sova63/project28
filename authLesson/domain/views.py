from cryptography.fernet import Fernet
from authLesson.settings import SECRET_KEY



'''def encrypt_password(password:str):
	fernet = Fernet(SECRET_KEY)
	return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password):
	fernet = Fernet(SECRET_KEY)
	return fernet.decrypt(encrypted_password).decode()
# Create your views here.'''


def encrypt_password(password: str):
    fernet = Fernet(SECRET_KEY)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password


def decrypt_password(encrypted_password):
    print(encrypted_password)
    fernet = Fernet(SECRET_KEY)
    return fernet.decrypt(encrypted_password.encode()).decode()