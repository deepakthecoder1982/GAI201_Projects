def allocate_projects(employees,projects):
    Employee_list_with_allocated_projects = []
    for emp in employees:
        curr_employee = emp["name"]
        emp_project = emp["current_project"]
        for project in projects:
            count_of_skills_match = 0
            max_skills_match = 0;
            for i in range(0,len(project["required_skills"])):
                if(emp["skills"][i] == project["required_skills"][i] ):
                    count_of_skills_match += 1
            if count_of_skills_match>max_skills_match:
                max_skills_match = count_of_skills_match
                emp_project = project["name"]
                print(emp_project)
        Employee_list_with_allocated_projects.append({curr_employee:emp_project});
    return Employee_list_with_allocated_projects


    


    

employees =[
    {"name": "John","skills":['Python',"Database"],"current_project":None},
    {"name": "Emma","skills":['Java',"Testing"],"current_project":None},
    {"name": "Kelly","skills":['Python',"Java"],"current_project":None}
] 

projects = [
    {"name": "Project A","required_skills":['Python',"Database"]},
    {"name": "Project B","required_skills":['Java',"Testing"]},
    {"name": "Project C","required_skills":['Python',"Java"]},
]

Question1 = allocate_projects(employees,projects);

print(Question1)