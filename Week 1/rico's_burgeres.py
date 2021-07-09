N = 5

employees_work_hours = []
for i in range (0, N):
    employee_hour = int(input('Hours?'))
    employees_work_hours.append(employee_hour)

total_pay = 0
total = 0
for i in range (0, N):
    total_pay += employees_work_hours[i] * 14.25
print(total_pay)  
