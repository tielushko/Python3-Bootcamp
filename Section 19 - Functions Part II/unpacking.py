#using * in front of an argument that is a list or tuple will allow us to unpack individual values from it and pass them in

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

nums = (1,2,3,4,5,6)
nums1 = [1,2,3,4,5,6]
print(sum_all_nums(*nums))
print(sum_all_nums(*nums1))

#using ** in front of a dictionary arguent will allow us to unpack it and use as kwargs
