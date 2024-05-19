def nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def tim_nguyen_to_sinh_doi(gioi_han):
    nguyen_to_sinh_doi = []
    for i in range(2, gioi_han - 1):
        if nguyen_to(i) and nguyen_to(i + 2):
            nguyen_to_sinh_doi.append((i, i + 2))
    return nguyen_to_sinh_doi

gioi_han = 1000
nguyen_to_sinh_doi = tim_nguyen_to_sinh_doi(gioi_han)
for sinh_doi in nguyen_to_sinh_doi:
    print(sinh_doi, end = ' ')