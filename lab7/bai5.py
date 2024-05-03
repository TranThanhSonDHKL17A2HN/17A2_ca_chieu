kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don = {}

tong_tien = 0
for mat_hang_da_mua in kho:
    so_luong_mat_hang_da_mua = kho[mat_hang_da_mua]
    don_gia_cua_mat_hang = gia_tien[mat_hang_da_mua]
    so_tien_hang_da_mua = so_luong_mat_hang_da_mua * don_gia_cua_mat_hang
    hoa_don[mat_hang_da_mua] = {
        "so_luong_mat_hang_da_mua": so_luong_mat_hang_da_mua,
        "don_gia_cua_mat_hang": don_gia_cua_mat_hang,
        "so_tien_hang_da_mua": so_tien_hang_da_mua
    }
    tong_tien += so_tien_hang_da_mua

print("Hóa đơn mua hàng:")
for mat_hang_da_mua, thong_tin in hoa_don.items():
    print(f"Mặt hàng đã mua là: {mat_hang_da_mua}")
    print(f"Số lượng mặt hàng đã mua là: {thong_tin['so_luong_mat_hang_da_mua']}")
    print(f"Đơn giá của mặt hàng là: {thong_tin['don_gia_cua_mat_hang']}")
    print(f"Số tiền của mặt hàng là: {thong_tin['so_tien_hang_da_mua']}")
    print()

print(f"Tổng số tiền của hóa đơn là: {tong_tien}")

print("\nSố lượng của các mặt hàng trong kho sau khi mua là:")
for mat_hang_da_mua, so_luong_mat_hang_da_mua in kho.items():
    print(f"{mat_hang_da_mua}: {so_luong_mat_hang_da_mua}")