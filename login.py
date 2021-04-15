import time

username = "Tara"
password = "123"

input_username = input('username: ')
input_password = input('password: ')

if input_username == username and input_password == password:
    print("....Loading....")
    time.sleep(5)
    print("Access Granted")
elif input_username != username and input_password == password:
    print("Please Try Again")
elif input_username == username and input_password != password:
    print("Please Try Again2")
