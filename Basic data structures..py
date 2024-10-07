from os.path import split

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
i = sorted(students)

p_0 = sum(grades[0]) / len(grades[0])
p_1 = sum(grades[1]) / len(grades[1])
p_2 = sum(grades[2]) / len(grades[2])
p_3 = sum(grades[3]) / len(grades[3])
p_4 = sum(grades[4]) / len(grades[4])

p = dict()

p0 = dict(key=i[0] , values = p_0)
p1 = dict(key=i[1] , values = p_1)
p2 = dict(key=i[2] , values = p_2)
p3 = dict(key=i[3] , values = p_3)
p4 = dict(key=i[4] , values = p_4)

p = p0, p1, p2, p3, p4

print(p)
