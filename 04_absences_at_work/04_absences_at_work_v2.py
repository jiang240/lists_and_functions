"""Program to record data about absences in a workplace
Version 2 - adding input loop to main routine"""
def name_and_days_check(info):
    days=""
    info=info.split()
    while len(info) != 3:
        info=input("Please enter employee name and absence"
                                       " days in 'John Smith 3' format: ").split()
    while not isinstance(days, int):
        try:
            days=int(info[2])
        except ValueError:
            info=name_and_days_check(input("Please enter employee name and "
                                           "absence days in 'John 3' "
                                           "format: "))
    employee_name= f"{info[0]} {info[1]}".title()
    return [employee_name,days]

# Main routine
all_absences=[]
total_absences=0
name_absence=input("Employee name and absent days: ")
while name_absence!="$": # Input loop to get employee names and absences
    name_absence=name_and_days_check(name_absence)
    total_absences+=name_absence[1]
    all_absences.append(name_absence)
    name_absence=input("Employee name and absent days: ")

# Processing data for the summary
average_absence=total_absences/len(all_absences)
most_absent=["",0]
no_absences=[]
above_average=[]
for employee in all_absences:
    if employee[1]>most_absent[1]:
        most_absent=employee
    if employee[1]==0:
        no_absences.append(employee)
    if employee[1]>average_absence:
        above_average.append(employee)
print()
print(f"Average number of days staff were absent: {average_absence:.2f}")
print()
print(f"Person with most days absent: {most_absent[1]} with {most_absent[0]}")
print()
print("List of people not absent at all: ")
for employee in no_absences:
    print(employee[1])
print()
print("List of people absent above average: ")
for employee in above_average:
    print(employee[0])
