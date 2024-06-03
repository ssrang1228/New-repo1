def gcd(a,b):
    if a>b:
        while True:
            if a%b==0:
                return b
            else:
                temp=a
                a=b
                b=temp%a

    elif a<b:
        while True:
            if b%a==0:
                return a
            else:
                temp=b
                b=a
                a=temp%b


def lcm(a,b):
    num_lcm=(a*b)//gcd(a,b)
    return num_lcm



num1=int(input('정수1 입력:'))
num2=int(input('정수1 입력:'))
print('(%s, %s) GCD :' %(num1, num2), gcd(num1,num2))
print('(%s, %s) GCD :' %(num1, num2), lcm(num1,num2))          
            
