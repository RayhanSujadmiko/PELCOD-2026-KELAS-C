#PROGRAM DATA DIRI MAHASISWA

#Data diri Mahasiswa
nama = input("Masukkan Nama Anda : ")
NIM = input("Masukkan NIM Anda : ")
tempat_lahir = input("Masukkan Tempat Lahir Anda : ")
alamat = input("Masukkan Alamat Anda : ")
hobi = input("Masukkan Hobi Anda : ")

#Menginput tahun lahir dan IPK
tahun_lahir = int(input("Masukkan Tahun Lahir Anda : "))
ipk = float(input("Masukkan IPK Anda : "))

#Menghitung data diri mahasiswa
tahun_sekarang = 2026
umur_saat_ini = tahun_sekarang - tahun_lahir
umur_10_tahun_kedepan = umur_saat_ini + 10
jumlah_karakter_nama = len(nama)
tahun_saat_umur_30 = tahun_lahir + 30

#Menampilkan data diri mahasiswa
print("Halo, nama saya", nama)
print("NIM saya", NIM)
print("Saya lahir di", tempat_lahir)
print("Alamat saya di", alamat)
print("Hobi saya adalah", hobi)
print("Umur saya saat ini adalah", umur_saat_ini, "tahun")
print("Umur saya 10 tahun kedepan adalah", umur_10_tahun_kedepan, "tahun")
print("Jumlah karakter dalam nama saya adalah", jumlah_karakter_nama)
print("Tahun saat saya berumur 30 tahun adalah", tahun_saat_umur_30)

#Menampilkan tipe data 
print("Tipe data nama adalah", type(nama))
print("Tipe data NIM adalah", type(NIM))
print("Tipe data tahun_lahir adalah", type(tahun_lahir))
print("Tipe data ipk adalah", type(ipk))
print("Tipe data umur_saat_ini adalah", type(umur_saat_ini))
print("Tipe data umur_10_tahun_kedepan adalah", type(umur_10_tahun_kedepan))
print("Tipe data jumlah_karakter_nama adalah", type(jumlah_karakter_nama))
print("Tipe data tahun_saat_umur_30 adalah", type(tahun_saat_umur_30))

#SELESAI