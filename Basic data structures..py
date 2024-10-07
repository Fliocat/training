grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
i = sorted(students)

p_0 = sum(grades[0]) / len(grades[0])
p_1 = sum(grades[1]) / len(grades[1])
p_2 = sum(grades[2]) / len(grades[2])
p_3 = sum(grades[3]) / len(grades[3])
p_4 = sum(grades[4]) / len(grades[4])

p = dict()

p.setdefault(i[0], p_0)
p.setdefault(i[1], p_1)
p.setdefault(i[2], p_2)
p.setdefault(i[3], p_3)
p.setdefault(i[4], p_4)

print(p)
