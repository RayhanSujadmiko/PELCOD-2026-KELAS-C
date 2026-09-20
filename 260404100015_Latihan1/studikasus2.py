#Rental Mobil "Rusdi Fortuner"

print("1. Brio - 150.000/hari")
print("2. Avanza - 200.000/hari")
print("3. Fortuner - 350.000/hari")

#Membuat Imputan
print("Jenis Mobil yang Anda Sewa?")
pilihan = int(input("Pilih Mobil 1-3 : "))
hari = int(input("Masukan lama sewa /hari : "))
kupon = input("Masukan Kupon : ")

#Menentukan jenis pilhan mobil
if pilihan == 1:
    mobil = "Brio"
    harga = 150000
elif pilihan == 2:
    mobil = "Avanza"
    harga = 200000
elif pilihan == 3:
    mobil = "Fortuner"
    harga = 350000
else :
    mobil = "Tidak Tersedia"
    harga = 0

#Menghitung harga sewa
sewa = harga * hari

#Mengecek lama sewa
if hari > 3:
    asuransi = 25000
else : 
    asuransi = 0

#Menghitung Subtotal
subtotal = sewa + asuransi

#Mengecek subtotal
if subtotal >= 500000:
    diskon1 = int(subtotal * 10/100)
else :
    diskon1 = 0

#Mengurangi subtotal dengan diskon 10%
setelah_diskon = subtotal - diskon1

#Mengecek diskon kupon
if kupon == "AMBATUNER":
    diskon2 = int(setelah_diskon * 5/100)
else : 
    diskon2 = 0

#Menghitung Total Pembayaran setelah diskon
total = setelah_diskon - diskon2

print("Jenis mobil : ", mobil)
print("Lama sewa : /hari ", hari)
print("subtotal : Rp", subtotal)
print("Diskon 1 : Rp", diskon1)
print("Diskon 2 : Rp", diskon2)
print("Total Bayar : Rp", total)
 