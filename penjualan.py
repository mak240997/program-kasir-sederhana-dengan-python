total = []
lagi = "y"
diskon = 0
while lagi == "y":
    a = nama = input("masukkan nama barang : ")
    b = harga = int(input("masukkan harga : "))
    c = banyak = int(input("masukkan jumlah yang dibeli : "))
    t = b * c
    total.append(t)
    lagi =input("apakah masih ingin mengimputkan barang? [y/t] ")
jumlah =sum(total)
anggota = input("apakah anda anggota? [y/t] ")
if anggota == "y":
    if jumlah >= 20000:
        diskon = jumlah * 20/100
    else:
        pass
else:
    if jumlah >= 20000:
        diskon = jumlah * 10/100
    else:
        pass

f = jumlah - diskon
print()
print ("total belanja : ",jumlah)
print("diskon : ",diskon)
print("Bayar, : ", f, "(total belanja - diskon)")