import math

#判断是否是质数
def PrimeQ(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False;
    return True;
 
#生成n挑k个数的模板，比如bits=5,k=3，返回会类似[1,0,1,0,1]
def NPickK(bits,k):
    if k == 0:
        yield [0]*bits
    elif k == bits:
        yield [1]*k
    else:
        for first in [0,1]:
            for sub in NPickK(bits-1,k-first):
                yield [first]+sub
 
#生成实际可用的模板，比如bit=7
#那么会生成NPickK(6,3)和NPickK(6,6)的模板，然后最后一位补零
def generate_Mask(bit):
    for mask_bit in range(3,bit,3):
        for mask in NPickK(bit-1,mask_bit):
            yield mask+[0]
 
#判断模板内是不是同一个数
def mask_is_same_number(strlist,mask):
    num = [strlist[x] for x in range(len(mask)) if mask[x]==1]
    return len(set(num)) == 1
 
#计算根据模板替换后质数的个数
def count_prime(strlist,mask):
    counter = 0;
    for dig in range(0+(mask[0]==1),10):
        strlist = [str(dig) if mask[x]==1 else strlist[x]
                   for x in range(len(mask))]
        counter += PrimeQ(int(''.join(strlist)))
    return counter
 
#测试这个数是否有符合条件
def template_test(n):
    strlist = list(str(n))
    for mask in generate_Mask(len(strlist)):
        if mask_is_same_number(strlist,mask):
            if count_prime(strlist,mask) >= 8:
                return True
    return False
 
#main
num = 1000
while True:
    #是否是1,3,7,9结尾
    if not num % 10  in [1,3,7,9]:
        pass
    #是不是有超过3个的0,1,2
    elif not (list(str(num)).count('0')>=3 or \
              list(str(num)).count('1')>=3 or \
              list(str(num)).count('2')>=3):
        pass
    elif not PrimeQ(num):
        pass
    elif not template_test(num):
        pass
    else:
        print(num);
        break
    num += 1