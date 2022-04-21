import os

list_size = []

list_size.append(os.stat('1.py').st_size)

list_size.append(os.stat('2.py').st_size)

list_size.append(os.stat('4.py').st_size)

list_size.append(os.stat('Rozhkova_Darya_dz_7.1.py').st_size)

list_size.append(os.stat('5.py').st_size)

print(list_size)

dict = {}

dict[500] = 3
dict[1000] = 2
dict[1500] = 0

print(dict)