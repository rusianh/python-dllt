# importing random
from random import *

# mật khẩu của hệ thống cần crack
system_pass = input("Enter your password: ")

# lữ trữ ký tự bảng chữ cái để sử dụng chúng crack mật khẩu
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]

# initializing chuỗi rỗng
guess = ""


# sử dụng vòng lặp while để tạo mật khẩu đến khi
# một trong số chúng khớp với mk hệ thống
while (guess != system_pass):
    guess = ""
    # tạo mật khẩu ngẫu nhiên bằng vòng lặp for
    for letter in range(len(system_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    # in các mật khẩu đã thử
    print(guess)
    
# in mật khẩu đúng!
print("Your password is",guess)