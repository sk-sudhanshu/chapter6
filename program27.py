#practic qustions.

# cities = ["delhi","gurgaon","noida","pune","mumbi","chenni"]
# heroes = ["thor","ironman","captain","shaktiman","krish","doom"]

# def print_len(list):
#     print(len(list))
    
# def print_list(list):
#     for item in list:
#         print(item, end="\n")
        
# print_list(heroes)
# print_list(cities)


# #factorial qustion

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
    
# cal_fact(5)

#convert currency..
def converter(usd_val):
    inr_val = usd_val*96
    print(usd_val, "USD =", inr_val, "INR")
    
converter(10)