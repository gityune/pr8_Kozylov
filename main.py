import random 

def password():
    s1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
    s2 = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
    s3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = ''
    for i in range(11):
        result += random.choice(s1+s2+s3)
    return result
    
p = password()
print(p)