import string
import random

characters=list(string.ascii_letters+string.digits+"!@#$%^&*")


def password_generator():
    password_len=int(input("How long your password : "))

    random.shuffle(characters)

    password = [] 

    for i in range(password_len):
        password.append(random.choice(characters))

    random.shuffle(password)

    print(type(password))

    password = "".join(password)

    print(type(password))
    
    print(password)


password_generator()




