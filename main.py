import random
alfavit =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
n = int(input("Введите длину пароля "))
password = ""
for i in range(n):
    password += random.choice(alfavit)
print("Ваш пароль:")
print(password)   