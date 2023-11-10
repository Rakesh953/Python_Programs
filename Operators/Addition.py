tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Element-wise subtraction
result_tuple = tuple(x - y for x, y in zip(tuple1, tuple2))
print(result_tuple)  # Output: (-3, -3, -3)


T1=(2,3,4,5)
T2=(1,2,3,4)
R=T1-T2
print(R)
