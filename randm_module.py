import random
import string

def random_number():
    print("Generate the random float value using random :")
    print(random.random())

    print("Generate the random integer value using randint :")
    print(random.randint(1, 9))
    
    print("=================================")


def random_list():
    my_list = []

    for i in range(5):
        my_list.append(random.randint(1, 50))

    print("Random List:", my_list)
    print("=============================================")


def random_pwd():
    pwd_length = int(input("Enter the Password length:"))
    

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    password = ''.join(random.choices(chars, k=pwd_length))

    print("Your password is:", password)
    print("=============================================")


def random_otp():
    OTP = random.randint(100000, 999999)

    print("The OTP is :", OTP)
    print("====================================")