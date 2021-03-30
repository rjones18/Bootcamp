employee1 = {
  'name': 'Jill Swanson',
  'age': 55,
  'department': 'Management',
  'phone': '555-1234',
  'salary': '$87,000'
}


employee2 = {
  'name': 'Leslie Knope',
  'age': 49,
  'department': 'Middle Management',
  'phone': '555-4321',
  'salary': '$69,000'
}

employee3 = {
  'name': 'Andy Dwyer',
  'age': 31,
  'department': 'Shoe Shining',
  'phone': '555-1122',
  'salary': '$42,000'
}


employee4 = {
  'name': 'April Ludgate',
  'age': 31,
  'department': 'Administration',
  'phone': '555-3345',
  'salary': '$42,000'
}

employees = [employee1 , employee2 , employee3 , employee4]

for employee in employees:
      print(f'{employee["name"]} in {employee["department"]} can be reached at {employee["phone"]}.')
