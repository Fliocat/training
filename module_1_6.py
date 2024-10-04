# Словарь

my_dict = {
           'Петя': 2003,
           'Витя': 1995,
           'Галя': 1845,
           'Ольга': 1984
           }

print(my_dict)

print(my_dict['Петя'])
print(my_dict.get('Иван'))

my_dict.update({'Вася': 1456,
                'Ева': 2000})
print(my_dict)

i = my_dict.pop('Галя')
print(i)

#Множество

my_set = {24, 26, 24, 24, 26, 'Кот', False, 3.14, ('Костя', 'Инна')}
print(my_set)

my_set.update({'Колчак',28})
print(my_set)

my_set.discard('Кот')
print(my_set)