import random

def format_name(name):
    return name & " du " & random.randint(0,100)

name ="Théophile"
print(format_name(name))