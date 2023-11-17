listA = [1, 2, 3, 4, 5]
listB = listA[2:4]
print(listB)
listB.append("hy")
print(listB)
listB.extend([7, 10, 9])
print(listB)
gabungkan_list = listB + listA
print(gabungkan_list)