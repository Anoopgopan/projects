employees = [
    {"id": 1, "name": "John Smith", "dept": "Sales"},
    {"id": 2, "name": "Jane Doe", "dept": "Engineering"},
    {"id": 3, "name": "Joe Schmo", "dept": "Accounting"},
    {"id": 4, "name": "Mary Smith", "dept": "Sales"},
]

key = tuple(set(list(map(lambda x: x['dept'], employees))))

a = {}
for j in key:
    b =[]
    for i in employees:
        if j == i['dept']:
            b.append(i)
    a.update({j:b})
print(a)




# method 2

    # if key[0] == i['dept']:
    #     a.append(i)
    # elif key[1] == i['dept']:
    #     b.append(i)
    # else:
    #     c.append(i)
# print({key[0]:a,key[1]:b,key[2]:c})
            
# Method3
    
# employee_dict = {}
# for i in employees:
#     dept = i["dept"]
#     if dept not in employee_dict:
#         employee_dict[dept] = []
#     employee_dict[dept].append(i)

# print(employee_dict)

# response = {'Sales': [{'id': 1, 'name': 'John Smith', 'dept': 'Sales'}, {'id': 4, 'name': 'Mary Smith', 'dept': 'Sales'}], 'Engineering': [{'id': 2, 'name': 'Jane Doe', 'dept': 'Engineering'}], 'Accounting': [{'id': 3, 'name': 'Joe Schmo', 'dept': 'Accounting'}]}
