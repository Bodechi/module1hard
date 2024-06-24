grades = [sum([5, 3, 3, 5, 4]) / 5, sum([2, 2, 2, 3]) /4, sum([4, 5, 5, 2])/4, sum([4, 4, 3])/3, sum([5, 5, 5, 4, 5])/5]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(students)
average_grade = dict(zip(students, grades))
print(average_grade)
