import random
import string
def generate_password(length=8):
    all_character=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(all_character)for i in range(length))
    return password
password_length_str=input("Input the desired length of your password:")
if password_length_str:
    password_length=int(password_length_str)
else:
    password_length=8
password=generate_password(password_length)
print(f"Generated password is:{password}")