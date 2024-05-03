f_list = []
d_list = []
c_list = []
b_list = []
a_list = []

for i in range(1, 11):
    ten = input("Nhập tên sinh viên(Cách nhau bằng khoảng trống): ").split()
    diem = map(float, input("Nhập điểm số của sinh viên: ").split())

    ten = list(ten)
    
    j = 0
    for grade in diem:
        name = ten[j]
        j += 1
        
        if grade < 4:
            f_list.append((name, grade))
        elif 4 <= grade < 5.5:
            d_list.append((name, grade))
        elif 5.5 <= grade < 7:
            c_list.append((name, grade))
        elif 7 <= grade < 8.5:
            b_list.append((name, grade))
        else:
            a_list.append((name, grade))

    thong_ke_f = len(f_list)
    thong_ke_d = len(d_list)
    thong_ke_c = len(c_list)
    thong_ke_b = len(b_list)
    thong_ke_a = len(a_list)
    
print(f"Danh sách sinh viên có điểm là F:{f_list}\nDanh sách sinh viên có điểm là D:{d_list}\nDanh sách sinh viên có điểm là C:{c_list}\nDanh sách sinh viên có điểm là B:{b_list}\nDanh sách sinh viên có điểm là A:{a_list}")
print(f"Số lượng sinh viên có điểm là F: {thong_ke_f}\nSố lượng sinh viên có điểm là D: {thong_ke_d}\nSố lượng sinh viên có điểm là C: {thong_ke_c}\nSố lượng sinh viên có điểm là B: {thong_ke_b}\nSố lượng sinh viên có điểm là A: {thong_ke_a}")