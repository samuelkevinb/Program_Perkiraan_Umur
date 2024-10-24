import datetime

# input nilai data mahasiswa
print("""=== Data Diri Mahasiswa ===""")
nim = input("Nim = ")
nama = input("Nama = ")
jurusan = input("Jurusan = ")
thnlahir = int(input("Tahun lahir = "))
blnlahir = int(input("Bulan lahir = "))

# ambil tahun dan bulan saat ini
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month

# perhitungan umur
if current_month >= blnlahir:
    jumlahthn = current_year - thnlahir
    jumlahbln = current_month - blnlahir
else:
    jumlahthn = current_year - thnlahir - 1
    jumlahbln = 12 - (blnlahir - current_month)

# output nilai data mahasiswa
print("\n=== Data Mahasiswa Kamu ===")
print("Nim Kamu adalah = " + str(nim)) 
print("Nama Kamu adalah = " + str(nama))
print("Jurusan Kamu adalah = " + str(jurusan))
print("Perkiraan umur = " + str(jumlahthn) + " tahun " + str(jumlahbln) + " bulan")
