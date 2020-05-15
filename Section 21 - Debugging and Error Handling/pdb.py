# FIRST EXAMPLE:
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)


# Be careful with variable names!
def add_numbers(a, b, c, d): #since some commands correspond to commands in pdb, use "p var_name" to actually print variable names
    import pdb; pdb.set_trace() #use like this

    return a + b + c + d
add_numbers(1,2,3,4)

# ===================
# NOTES  NOTES  NOTES
# ===================
# import pdb
# pdb.set_trace()

# Also commonly on one line:
# import pdb; pdb.set_trace()

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
