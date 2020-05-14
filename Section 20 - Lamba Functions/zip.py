#imagine two lists of numbers with same length
# zip will make the pair combination from two lists.

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
print(list(zip(nums1, nums2))) #prints a zip object without conversion to list, if convert, [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(dict(zip(nums1, nums2))) #{1: 6, 2: 7, 3: 8, 4: 9, 5: 10}


# zip will stop as soon as the shortest iterable is exhausted
# we are not limited to just two containers
# to unpack, use the star operator
five_by_two = [(0, 1), (1,2), (2,3), (3,4), (4,5)] 
list(zip(*five_by_two)) #[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING LIST COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)































# # r = dict(zip(students, midterms))
# print(r)

# r = {item[0]: max(item[1], item[2]) for item in zip(students,midterms, finals)}
# print(r)

# r = {item[0]: round((item[1] + item[2])/2) for item in zip(students,midterms, finals)}
# print(r)


# z = zip(
# 	students,
# 	map(
# 		lambda pair: max(pair),
# 		zip(midterms, finals)
# 	)
# )

