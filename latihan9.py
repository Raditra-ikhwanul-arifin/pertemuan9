#akses list
my_list = [1, 2, 3, 4, 5]
print(my_list[2])
print(my_list[1:4])
print(my_list[-1])

#ubah elemen list
my_list[3] = 99
print(my_list)
my_list[3:] = [66, 77]
print(my_list)

#tambah elemen list:
listA = [1, 2, 3, 4, 5]
listB = listA[2:4]
print(listB)
listB.append("hy")
print(listB)
listB.extend([7, 10, 9])
print(listB)
gabungkan_list = listB + listA
print(gabungkan_list)
