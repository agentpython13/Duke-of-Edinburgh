n = int(input())
students = [int(x) for x in input().split()]
number = min(students.count(1),students.count(2),students.count(3))
print(number)
for x in range(number):
    string = ""
    string += str(students.index(1) + 1) + " "
    string += str(students.index(2) + 1) + " "
    string += str(students.index(3) + 1) + " "
    students[students.index(3)] = 0
    students[students.index(1)] = 0
    students[students.index(2)] = 0
    print(string)