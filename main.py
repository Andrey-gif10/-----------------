import random
alfavit =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
n = int(input("Введите длину пароля "))
while n < 8:
    print("Пароль должен быть больше 8 символов")
    n = int(input("Введите длину пароля "))
password = ""
for i in range(n):
    password += random.choice(alfavit)
print("Ваш пароль:")
print(password)   