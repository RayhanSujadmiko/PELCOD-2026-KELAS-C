#NAMA : Rayhan Sujadmiko
#NIM : 260404100015
#KELOMPOK : SI-04-PBW

#TIKET BUS PULANG KAMPUNG (NIM GENAP)
print("Selamat Datang di Aplikasi Tiket Bus Pulang Kampung")

nama = input("Masukkan Nama Anda : ")
punya_ktm = input("Apakah Anda memiliki KTM? (ya / tidak) : ")
if punya_ktm == "ya":
    punya_ktm = True
else:
    punya_ktm = False
NIM = input("Masukkan NIM Anda : ")

#Keterangan harga tiket bus
print("Tiket Surabaya - Rp25.000")
print("Tiket Sumenep - Rp45.000")
print("Tiket Malang - Rp60.000") 

#Menginput data
print("Kota Tujuan Anda?")
kota_tujuan = input("Kemana kah Anda ingin pergi? (surabaya / sumenep / malang) : ")
kelas_tiket = input("Pilih Kelas Tiket (ekonomi / eksekutif) : ")
hari_keberangkatan = input("Masukkan Hari Keberangkatan (weekday / weekend) : ")
total_bagasi = float(input("Masukkan Berat Bagasi Anda (kg) : "))

#Menentukan harga tiket bus
if kota_tujuan == "surabaya":
    harga_tiket = 25000
elif kota_tujuan == "sumenep":
    harga_tiket = 45000
elif kota_tujuan == "malang":
    harga_tiket = 60000
else:
    print("Kota tujuan tidak tersedia")
    exit()

#Menentukan harga tiket bus berdasarkan kelas tiket
if kelas_tiket == "ekonomi":
    biaya_kelas = 0
elif kelas_tiket == "eksekutif":
    biaya_kelas = 25000
    if kota_tujuan == "surabaya":
        print("Maaf, Kelas Eksekutif tidak tersedia untuk tujuan Surabaya")
        print("Pesanan ditolak")
else:
    print("Kelas tiket tidak tersedia")
    
total_biaya_kelas = harga_tiket + biaya_kelas

#Menentukan harga tiket bus berdasarkan hari keberangkatan
if hari_keberangkatan == "weekend":
    subtotal1 = total_biaya_kelas * 15/100
    subtotal2 = total_biaya_kelas + subtotal1
elif hari_keberangkatan == "weekday":
    subtotal2 = total_biaya_kelas

#Diskon Mahasiswa
if punya_ktm == True:
    hitung_diskon = subtotal2 * 10/100
else:
    hitung_diskon = 0

setelah_diskon = subtotal2 - hitung_diskon

#Biaya bagasi
if total_bagasi < 20:
    biaya_bagasi = 0
elif total_bagasi >= 20 and total_bagasi <= 30:
    biaya_bagasi = 5000
elif total_bagasi > 30:
    print("Ditolak, bagasi harus dikirim lewat kargo") 

#Total pembarayan
total_pembayaran = setelah_diskon + biaya_bagasi

print("Nama :", nama)
print("NIM :", NIM)
print("Kota Tujuan :", kota_tujuan)
print("Kelas Tiket :", kelas_tiket)
print("Hari Keberangkatan :", hari_keberangkatan)
print("Berat Bagasi :", total_bagasi)
print("Total Pembayaran : Rp", int(total_pembayaran))

#SELESAI