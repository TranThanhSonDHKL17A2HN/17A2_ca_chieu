phim_muon_chon = int(input("Nhap so tuong ung voi the loai phim\n1.Hanh dong\n2.Kinh di\n3.Tinh cam\n4.Hai huoc\n5.Hoat hinh\nNhap tai day:"))
if phim_muon_chon == 1:
    print("Da chon the loai Hanh dong(Trinh chieu ca ngay)")
    time = int(input("Chon suat chieu(Nhap thoi gian muon xem) : "))
    print(f"Hay quay lai vao luc {time}h!!!")
elif phim_muon_chon == 2:
    print("Da chon the loai Kinh di(Suat chieu tu 18h den 24h)")
    time = int(input("Chon suat chieu(Nhap thoi gian muon xem) : "))
    if 18 <= time <= 24:
        print(f"Hay quay lai vao luc {time}h!!!")
    else:
        print("Khong co xuat chieu phu hop")
elif phim_muon_chon == 3:
    print("Da chon the loai Tinh cam(Suat chieu tu 18h den 24h)")
    time = int(input("Chon suat chieu(Nhap thoi gian muon xem) : "))
    if 18 <= time <= 24:
        print(f"Hay quay lai vao luc {time}h!!!")
    else:
        print("Khong co xuat chieu phu hop")
elif phim_muon_chon == 4:
    print("Da chon the loai Hai huoc(Trinh chieu ca ngay)")
    time = int(input("Chon suat chieu(Nhap thoi gian muon xem) : "))
    print(f"Hay quay lai vao luc {time}h!!!")
elif phim_muon_chon == 5:
    print("Da chon the loai Hoat hinh(Suat chieu tu 8h den 15h)")
    time = int(input("Chon suat chieu(Nhap thoi gian muon xem) : "))
    if 8 <= time <= 15:
        print(f"Hay quay lai vao luc {time}h!!!")
    else:
        print("Khong co xuat chieu phu hop")   
else:
    print("Lua chon khong hop le")