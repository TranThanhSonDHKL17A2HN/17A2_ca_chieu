so_tien_bd=10000
lai_suat=0.06
#1 So tien sau 5 nam
amount_after_5_years=so_tien_bd * ((1+lai_suat)**5)
print("Tổng tiền có được sau 5 năm là {:.2f}".format(amount_after_5_years))
#2 So tien sau 10 nam
amount_after_10_years=so_tien_bd * ((1+lai_suat)**10)
print("Tổng tiền có được sau 10 năm là {:.2f}".format(amount_after_10_years))
#3 Tinh ty le tang truong
growth_rate=(amount_after_10_years - amount_after_5_years)/amount_after_5_years
print("Tỷ lệ tăng trưởng sau 10 năm so với sau 5 năm là: {:.2f}".format(growth_rate))







