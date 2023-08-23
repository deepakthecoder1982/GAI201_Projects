def max_salary_employee(employee_list=[]):
    max_salary_employee = 0;
    try:
        for employee in employee_list:
            if int(employee['salary']) > max_salary_employee:
                max_salary_employee = employee['salary']
    
        for employee in employee_list:
            if max_salary_employee == employee['salary']:
                max_salary_employee = employee
                
        return max_salary_employee
    
    except ValueError:
        print("There is an value error")

employee = [
    {'name': 'John', "salary":2500,"designation":'developer'},
    {'name': 'kelly', "salary":3000,"designation":'tester'},
    {'name': 'Emma', "salary":3500,"designation":'manager'},
]
result = max_salary_employee(employee)
print(result)