from numpy import array

listS = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [20, 30, 40, 50, 60, 70, 80, 90, 100]]
print(listS)
temp_array = array(listS, dtype=object)
print(temp_array)
# listR = temp_array.tolist()
# print(listR)