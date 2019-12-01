# Hãy dùng List kết hợp với Dictionary để mô tả bảng lương 
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
list=[dict1,dict2,dict3,dict4,dict5]
print(list)

# Hãy in ra thông tin về lương trong hàng thứ 3 của bảng lương
a=dict3['Salary per hour']
print(a)

# Hãy thay thông tin hàng đầu tiên của bảng lương
list[0]={
    'Name' : 'Huyen',
    'Role' : 'Waitress',
    'Hours' : 14,
    'Salary per hour' : 1,
}
print(list)

# Hãy xoá đi hàng cuối cùng trong bảng lương
list.pop(4)
print(list)

# Hãy in ra tất cả thông tin trong bảng lương, mỗi nhân viên một dòng
for i in range(3):
    print(list[i])

# Từ thông tin bảng lương, hãy tính lương tháng của từng nhân viên một
dict1['Salary per month']=dict1['Salary per hour']*dict1['Hours']*30
dict2['Salary per month']=dict2['Salary per hour']*dict2['Hours']*30
dict3['Salary per month']=dict3['Salary per hour']*dict3['Hours']*30
dict4['Salary per month']=dict4['Salary per hour']*dict4['Hours']*30
dict5['Salary per month']=dict5['Salary per hour']*dict5['Hours']*30
print(list)