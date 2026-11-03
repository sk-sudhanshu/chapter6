#Function in python..

def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum

cal_sum(5,6)
cal_sum(4,7)
cal_sum(9,16)

#exemple 

#function defination 
def calc_sum(x, y):#parameters
    return x + y

sum = cal_sum(1, 2)#function call
print(sum)


#exemple-Average of 3 numbers
def calc_avg(p,q,s):
    sum = p+q+s
    avg = sum / 3
    print(avg)
    return avg 


calc_avg(23,45,67)