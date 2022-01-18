def conversion(num,base):
    result = 0
    i=1
    while num != 0:
        result += num%base*i
        num=int(num/base)
        i=i*10
    return result
    
           
print(conversion(379,16))