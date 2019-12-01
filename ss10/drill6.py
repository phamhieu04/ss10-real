
dict1={
    'Name' : 'Huy',
    'Role' : 'Waiter',
    'Hours' : 12,
    'Salary per hour' : 0.8,
}
dict2={
    'Name' : 'Tung',
    'Role' : 'Cook',
    'Hours' : 24,
    'Salary per hour' : 1.5,
}
dict3={
    'Name' : 'M.Duc',
    'Role' : 'Wanager',
    'Hours' : 20,
    'Salary per hour' : 2,
}
dict4={
    'Name' : 'Don',
    'Role' : 'Waiter',
    'Hours' : 12,
    'Salary per hour' : 0.9,
}
dict5={
    'Name' : 'H.Duc',
    'Role' : 'Waiter',
    'Hours' : 14,
    'Salary per hour' : 0.7,
}
dict6={
    'Name' : 'Huyen',
    'Role' : 'Waitress',
    'Hours' : 14,
    'Salary per hour' : 1,
}
list=[dict1,dict2,dict3,dict4,dict5,dict6]
for i in range(6):
    print(list[i])
a=dict1['Hours']*dict1['Salary per hour']
b=dict2['Hours']*dict2['Salary per hour']
c=dict3['Hours']*dict3['Salary per hour']
d=dict4['Hours']*dict4['Salary per hour']
e=dict5['Hours']*dict5['Salary per hour']
f=dict6['Hours']*dict6['Salary per hour']
sum=(a+b+c+d+e+f)*30
print("Tong so tien chi nhanh phai tra cho nhan vien la:",sum)