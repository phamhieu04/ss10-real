# Khai báo 1 dictionary biểu diễn 1 câu hỏi trắc nghiệm (em có thể thay đổi nội dung nếu muốn)
dapan={
    'nhom nhac kpop nu duoc yeu thich nhat' : 'black pink',
}
luachon={
    '1' : 'twice',
    '2' : 'mamamo',
    '3' : 'black pink',
    '4' : 'itzy',
}
list=[dapan,luachon]


# Thực hiện in ra câu trắc nghiệm này và hỏi đáp án từ người dùng
print(*list[0],":")
for i,k in luachon.items():
    print(i,k,sep='.')
ask=input("dap an ban chon la:")
if ask!=3:
    print("sai r")
else:
    print("chuan r")


# Sử dụng các kiểu dữ liệu đã học khai báo nhiều hơn 2 câu trắc nghiệm, các câu trắc nghiệm có nội dung,  các lựa chọn và các đáp án đúng khác nhau
    dapan1={
        'tuong duoc choi nhieu nhat lol' : 'yasuo',
    }
    luachon1={
        '1' : 'leesin',
        '2' : 'zed',
        '3' : 'yasuo',
        '4' : 'darius',
    }
    list1=[dapan1,luachon1]
    print(*list1[0],":")
    for i,k in luachon.items():
        print(i,k,sep='.')
    ask1=input("dap an ban chon la:")
    if ask1!=3:
        print("sai r")
    else:
        print("chuan r")