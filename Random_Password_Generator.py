import string
import random
chara='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./;:<=>?@'
numb_of_pass=int(input("Enter Number Of Passwords:"))
pass_len=int(input("Enter Password Length:"))
print("Password:\n")
for pwd in range(numb_of_pass):
    final_pass=''
    for numb_chara in range(pass_len):
        final_pass +=random.choice(chara)
    print(final_pass)
print("\n")
