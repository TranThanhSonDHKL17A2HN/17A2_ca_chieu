van_ban = '''One day I was returning from the school. When I was about 1 Km away from my house, it started raining. I had no umbrella. I stood under a shed in front of a shop. Half an hour passed. Rain became heavier. Street was full of water now.  I could not stand like this forever. So I decided to go in rain. I drenched completely. Some children were playing with paper boats. I also joined them. I forgot everything. Suddenly I saw my mother was coming with an umbrella. She scolded me. But I was happy. I can’t forget that day.'''

van_ban = van_ban.replace(".", " ")
van_ban = van_ban.replace(",", " ")
van_ban = van_ban.replace("'s", " ")
van_ban = van_ban.lower()

danh_sach = van_ban.split()
tan_suat = {}

for i in range(len(danh_sach)):
    count = 0
    for j in range(len(danh_sach)):
        if danh_sach[i] == danh_sach[j]:
            count += 1
    tan_suat[danh_sach[i]] = count
print("Tần suất xuất hiện của các từ trong đoạn văn là:")
print(tan_suat)

xuat_hien_nhieu = max(tan_suat, key=tan_suat.get)
so_lan_xh_nhieu = tan_suat[xuat_hien_nhieu]
print("Từ xuất hiện nhiều nhất là '{}' với {} lần xuất hiện.".format(xuat_hien_nhieu, so_lan_xh_nhieu))

xuat_hien_it = min(tan_suat, key=tan_suat.get)
so_lan_xh_it = tan_suat[xuat_hien_it]
print("Từ xuất hiện ít nhất là '{}' với {} lần xuất hiện.".format(xuat_hien_it, so_lan_xh_it))