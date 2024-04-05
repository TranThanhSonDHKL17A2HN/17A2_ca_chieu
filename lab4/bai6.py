so = input("Nhap so bat ky: ")
for doc_so in so:
    if doc_so in '0 1 2 3 4 5 6 7 8 9':
        doc_so = int(doc_so)
        if doc_so == 0:
            print("zero", end=' ')
        elif doc_so == 1:
            print("one", end=' ')
        elif doc_so == 2:
            print("two", end=' ')
        elif doc_so == 3:
            print("three", end=' ')
        elif doc_so == 4:
            print("four", end=' ')
        elif doc_so == 5:
            print("five", end=' ')
        elif doc_so == 6:
            print("six", end=' ')
        elif doc_so == 7:
            print("seven", end=' ')
        elif doc_so == 8:
            print("eight", end=' ')
        elif doc_so == 9:
            print("nine", end=' ')
    else:
        print("Khong doc duoc chu so !!!", end=' ')