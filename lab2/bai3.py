x=int(input("Nhap so can doc:"))
if 100 <= x <= 999:
    cs_hang_tram=x//100
    cs_hang_chuc=(x//10)%10
    cs_hang_dvi=x%10
    if cs_hang_tram == 1:
        doc_hang_tram = "One hundred"
    elif cs_hang_tram  == 2:
        doc_hang_tram = "Two hundred"
    elif cs_hang_tram  == 3:
        doc_hang_tram = "Three hundred"
    elif cs_hang_tram  == 4:
        doc_hang_tram = "Four hundred"
    elif cs_hang_tram  == 5:
        doc_hang_tram = "Five hundred"
    elif cs_hang_tram  == 6:
        doc_hang_tram = "Six hundred"
    elif cs_hang_tram  == 7:
        doc_hang_tram = "Seven hundred"
    elif cs_hang_tram  == 8:
        doc_hang_tram = "Eight hundred"
    elif cs_hang_tram  == 9:
        doc_hang_tram = "Nine hundred"
    elif cs_hang_tram  == 0:
        doc_hang_tram = ""
    if cs_hang_chuc == 1:
        doc_hang_chuc = "ten"
    elif cs_hang_chuc == 2:
        doc_hang_chuc = "twenty"
    elif cs_hang_chuc == 3:
        doc_hang_chuc = "thirty"
    elif cs_hang_chuc == 4:
        doc_hang_chuc = "forty"
    elif cs_hang_chuc == 5:
        doc_hang_chuc = "fifty"
    elif cs_hang_chuc == 6:
        doc_hang_chuc = "sixty"
    elif cs_hang_chuc == 7:
        doc_hang_chuc = "seventy"
    elif cs_hang_chuc == 8:
        doc_hang_chuc = "eighty"
    elif cs_hang_chuc == 9:
        doc_hang_chuc = "ninety"
    elif cs_hang_chuc == 0:
        doc_hang_chuc = ""
    if cs_hang_dvi == 1:
        doc_hang_don_vi = "one"
    elif cs_hang_dvi == 2:
        doc_hang_don_vi = "two"
    elif cs_hang_dvi == 3:
        doc_hang_don_vi = "three"
    elif cs_hang_dvi == 4:
        doc_hang_don_vi = "four"
    elif cs_hang_dvi == 5:
        doc_hang_don_vi = "five"
    elif cs_hang_dvi == 6:
        doc_hang_don_vi = "six"
    elif cs_hang_dvi == 7:
        doc_hang_don_vi = "seven"
    elif cs_hang_dvi == 8:
        doc_hang_don_vi = "eight"
    elif cs_hang_dvi == 9:
        doc_hang_don_vi = "nine"
    elif cs_hang_dvi == 0:
        doc_hang_don_vi = ""
    print(f"So {x} doc la {doc_hang_tram} {doc_hang_chuc} {doc_hang_don_vi}")
else:
    print("Xin moi nhap lai")


      
      
      
      
      
      
      
      
