import re
n = input("Enter pls 8-16 symbol password with numbers, _!#? symbols and latters in registers\n")
reg = re.match(r'^[0-9A-Za-z_!#?]{8,16}$', n)
if reg:
    print("password is correct")
else:
    print("password is incorrect")