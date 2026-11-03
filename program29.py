#write a recursive function to calculate the sum of first n natural numbers


def sum_of_numbers(n):
    if (n == 0):
        return 0
    return n + sum_of_numbers(n-1)

sum = sum_of_numbers(5)
print(sum)


#write a recursive function to print all elements of a list
def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1)

my_list = [1, 2, 3, 4, 5]
print_list(my_list)