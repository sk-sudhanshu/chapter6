#recursion..

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("End")
# show(5)


#recursion with fectorial
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n * factorial(n-1)

print(factorial(5))