immutable_var = 24, 'lop', True, 15.5
print(immutable_var)

immutable_var[0] = str(25)          #У меня в кортеже прописаны неизменяемые элементы!!!
print(immutable_var)

mutable_list = ['cat', 'dog', 'bird', 'lion', 'fish']
print(mutable_list)

mutable_list[4] = 'hare'.upper()
print(mutable_list)

