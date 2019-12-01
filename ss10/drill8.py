ten={
    'ten' : 'Sherlock Holmes',
}
nam={
    'nam phat hanh' : 1887 , 
}
nv=['Sherlock Holmes','Doctor Watson']
nvtg={
    'nhan vat tham gia' : nv ,
}
list=[ten,nam,nvtg]
print(list,'\n')

# Không thay đổi khai báo, tạo thêm thông tin về hãng sản xuất hoặc quốc gia vào dictionary ở bài trước
qg={
    'quoc gia' : 'Anh',
}
list.append(qg)
print(list,'\n')


# Hiện ra tất cả các thông tin có bên trong dictionary ở bài trước, mỗi thông tin mỗi dòng, key và value cách nhau bởi dấu gạch ngang ‘ - ’
print(*list[0],'-',ten['ten'])
print(*list[1],'-',nam['nam phat hanh'])
print(*list[2],'-',nvtg['nhan vat tham gia'])
print(*list[3],' - ',*qg['quoc gia'],sep='')


# Không thay đổi khai báo, thay toàn bộ danh sách nhân vật hoặc diễn viên ở trong bài trước bằng một danh sách mới
nvm=['zed','yasuo','leesin']
nvtg['nhan vat tham gia']=nvm
print(list,'\n')


# Không thay đổi khai báo, thêm một diễn viên hoặc nhân vật mới vào trong list của dictionary ở bài trước
nvm.append('kayn')
print(list,'\n')


# Không thay đổi khai báo, xoá đi diễn viên hoặc nhân vật đầu tiên trong list của dictionary ở bài trước
nvm.remove('yasuo')
print(list,'\n')


# Hiện ra chính xác nhân vật hoặc diễn viên thứ hai trong danh sách nhân vật hoặc diễn viên, không bao gồm các dấu nháy đơn (‘) hay ngoặc vuông ( [ ) ( ] )
print("nhan vat thu hai: ",*nvm[1],sep='')


# Sử dụng vòng for, in ra tất cả các diễn viên, nhân vật bên trong dictionary, mỗi diễn viên nhân vật một dòng
for i in range(3):
    print("nhan vat thu ",i+1,": ",*nvm[i],sep='')



