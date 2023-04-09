import random 

def password():
    s1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
    result = ''
    for i in range(11):
        result += random.choice(s1)
    return result
    
p = password()
print(p)