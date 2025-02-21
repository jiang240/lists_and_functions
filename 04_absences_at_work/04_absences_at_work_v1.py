"""Program to record data about absences in a workplace
Version 1 - basic working program"""
all_absences=[]
total_absences=0
name=input("Employee name: ")
absences=int(input("Number of absences: "))
total_absences+=absences
all_absences.append([name,absences])
average_absence=total_absences/len(all_absences)
print(f"Average number of days staff were absent: {average_absence}")
most_absent=["",0]
for employee in all_absences:
    if employee[1]>most_absent[1]:
        most_absent=employee
print(f"Person with most days absent: {most_absent[0]}")
no_absences=[]
for employee in all_absences:
    if employee[0]==0:
        no_absences.append(employee)
print("List of people not absent at all: ")
for employee in no_absences:
    print(employee)
above_average=[]
for employee in all_absences:
    if employee[1]>average_absence:
        above_average.append(employee)
print("List of people absent above average: ")
for employee in above_average:
    print(employee[0])