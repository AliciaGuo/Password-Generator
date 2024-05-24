import random

special_chars = ['_', '!', ';', ':', ',']
numeral_chars = [chr(i) for i in range(48, 58)]
uppercase_chars = [chr(i) for i in range(65, 91)]
lowercase_chars = [chr(i) for i in range(97, 123)]

def password_generator_length(length):
    password=list()
    num_onefourth=n//4
    for i in range(0,num_onefourth):
        password.append(random.choice(special_chars))
        password.append(random.choice(numeral_chars))
        password.append(random.choice(uppercase_chars))
        i+=1
    for i in range((n//4)+(n%4)):
        password.append(random.choice(lowercase_chars))
        i+=1
    passwordstr="".join(password)
    return passwordstr
n=int(input("random pswd length? (>8)"))
if n<8:
    print("pswd short")
else:
    print("gneerator pswd:", password_generator_length(n))

password_generator_length(n)



