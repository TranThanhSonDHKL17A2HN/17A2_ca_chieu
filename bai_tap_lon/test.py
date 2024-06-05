import csv
import random

horses = {
    1: {'xac_xuat_di_chuyen': 0.2, 'khoang_cach': 0},
    2: {'xac_xuat_di_chuyen': 0.3, 'khoang_cach': 0},
    3: {'xac_xuat_di_chuyen': 0.1, 'khoang_cach': 0},
    4: {'xac_xuat_di_chuyen': 0.4, 'khoang_cach': 0},
    5: {'xac_xuat_di_chuyen': 0.25, 'khoang_cach': 0}
}

do_dai_duong_dua = 500
ket_qua_dua = []
ve_dich = []

while len(ve_dich) < 5:
    for ma_ngua, du_lieu_ngua in horses.items():
        if ma_ngua not in ve_dich:
            move = random.random()
            if move <= du_lieu_ngua['xac_xuat_di_chuyen']:
                du_lieu_ngua['khoang_cach'] += 10

            if du_lieu_ngua['khoang_cach'] >= do_dai_duong_dua:
                ve_dich.append(ma_ngua)
                ket_qua_dua.append((len(ve_dich), ma_ngua, du_lieu_ngua['khoang_cach']))

with open('ket_qua_dua.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Vị trí", "Mã ngựa", "Khoảng cách di chuyển"])

    for result in ket_qua_dua:
        writer.writerow(result)

for vi_tri, ma_ngua, khoang_cach in ket_qua_dua:
    print(f"Vị trí: {vi_tri}, Mã ngựa: {ma_ngua}, Khoảng cách di chuyển: {khoang_cach} mét")