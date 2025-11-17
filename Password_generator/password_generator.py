
import random ; import string

def password_generator(length = 15):
    characters =  string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#print(len(password_generator(15)))
print(password_generator())
