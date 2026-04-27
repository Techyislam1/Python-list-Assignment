student = ['Usman Muhammad Lawan',24,'mechatronics eng',2.7,'Nigeria']
print('name:',student[0])
print('Age:',student[1])
print('Department:',student[2])
print('CGPA:',student[3])
print('country:',student[4])

#change department and CGPA
student[2],student[3] = 'Robotics engineering', 4.0
print(student)

#Print reversed record
rv = student[::-1]
print(rv)

#print first 3 values
f3 = student[0:3]
print(f3)


