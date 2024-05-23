import array as arr
print("NO 1")
arr = [8, 3, 12, 4, 7, 2]
output_arr = []
# menghapus semua angka kurang dari 5 dan menggantinya dengan nilai 0
for i in arr:
    if i <= 5:
        output_arr.append(0)
    else:
        output_arr.append(i)
# mengurutkan nilaimterbesar ke terkecil
output_arr.sort(reverse=True)
print(output_arr)  

print("NO 2")
arr = [7, 4, 9, 2, 5, 1]
output_arr = []
# menghapus nilai bilangan ganjil dan mengurutkan nilai tersebut dari terkecil ke terbesar
for i in arr:
    if i % 2 == 0:
        output_arr.append(i)

output_arr.sort()
print(output_arr)

print("NO 3")
kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
output = []
# menghapus kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata tersebut secara alfabetis
for i in kata:
    if len(i) >= 5:
        output.append(i)

output.sort()
print(output)

print("NO 4")
list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]
# menggabungkan kedua list tersebut dan menghapus semua buah yang sama dan mengurutkan sisa buah-buahan secara alfabetis.
hasil = sorted(set(list1 + list2))
print(hasil)

print("NO 5")
input_arr = [105, 20, 8, 150, 30, 5, 200]
output_arr = []
# menghapus nilai yang kurang dari 10 dan lebih dari 100
for i in input_arr:
    if 10 <= i <= 100:
        output_arr.append(i)

# mengurutkan sisa nilai tersebut dari terkecil ke terbesar
output_arr.sort()
print(output_arr)

print("NO 6")
list_buku = []
list_mahasiswa = []
list_peminjam = []

def menambahkan_buku (no_isbn, judul, pengarang, isiHalaman, deskripsi, stok, booked):
    buku = {
        "no_isbn": no_isbn,
        "judul": judul,
        "pengarang": pengarang,
        "isiHalaman": isiHalaman,
        "deskripsi": deskripsi,
        "stok": stok,
        "booked": booked
    }
    list_buku.append(buku)
    print("Buku telah ditambahkan ke dalam daftar")

def daftar_buku():
    if not list_buku:
        print("Tidak ada buku yang tersedia")
    else:
        for buku in list_buku:
            print(f"Judul: {buku['judul']}, No ISBN: {buku['no_isbn']}, Pengarang: {buku['pengarang']}, Isi Halaman: {buku['isiHalaman']}, Deskripsi: {buku['deskripsi']}, Stok: {buku['stok']}, Booked: {buku['booked']}")
 
def menambahkan_mahasiswa(nama, nim, kontak, alamat):
    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "kontak": kontak,
        "alamat": alamat
    }
    list_mahasiswa.append(mahasiswa)
    print("Mahasiswa telah ditambahkan ke dalam daftar")

def daftar_mahasiswa():
    if not list_mahasiswa:
        print("Tidak ada mahasiswa yang terdaftar")
    else:
        for mahasiswa in list_mahasiswa:
            print(f"Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, No HP: {mahasiswa['kontak']}, Alamat: {mahasiswa['alamat']}")

def menambahkan_peminjam(nim, no_isbn, tanggal_pinjam, tanggal_kembali, status):
    peminjam = {
        "nim": nim,
        "no_isbn": no_isbn,
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali,
        "status": status
    }
    list_peminjam.append(peminjam)
    print("Peminjaman telah ditambahkan ke dalam daftar")

def pinjam_buku(nim, no_isbn):
    mahasiswa = next((m for m in list_mahasiswa if m['nim'] == nim), None)
    buku = next((b for b in list_buku if b['no_isbn'] == no_isbn), None)
    
    if mahasiswa and buku:
        if buku['stok'] - buku['booked'] > 0:
            buku['booked'] += 1
            tanggalpinjam = datetime.now().strftime('%Y-%m-%d')
            tanggal_kembali = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
            tambahPeminjam(nim, no_isbn, tanggalpinjam, tanggal_kembali, 'Dipinjam')
            print(f"Buku '{buku['judul']}' berhasil dipinjam oleh {mahasiswa['nama']}")
        else:
            print('buku tidak tersedia atau stok habis')
    else:
        print('mahasiswa atau buku tidak ditemukan dalam daftar peminjaman')

def buku_dikembalikan(nim, no_isbn):
    peminjaman = next((p for p in list_peminjam if p['nim'] == nim and p['no_isbn'] == no_isbn and p['status'] == 'Dipinjam'), None)
    buku = next((b for b in list_buku if b['no_isbn'] == no_isbn), None)
    
    if peminjaman and buku:
        buku['booked'] -= 1
        peminjaman['status'] = 'Dikembalikan'
        peminjaman['tanggalkembali'] = datetime.now().strftime('%Y-%m-%d')
        print(f"Buku '{buku['judul']}' berhasil dikembalikan")
    else:
        print('buku tidak ditemukan')

def menu():
    while True:
        print("\n========== Manajemen Perpustakaan ==========")
        print("1. menambahkan buku")
        print("2. daftar buku")
        print("3. menambahakan Mahasiswa")
        print("4. daftar Mahasiswa")
        print("5. Peminjaman Buku")
        print("6. Pengembalian Buku")
        print("7. Keluar")
        
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            no_isbn = input("Masukkan ISBN buku: ")
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            isiHalaman = int(input("Masukkan jumlah halaman buku: "))
            deskripsi = input("Masukkan deskripsi buku: ")
            stok = int(input("Masukkan stok buku: "))
            booked = 0  
            menambahkan_buku (no_isbn, judul, pengarang, isiHalaman, deskripsi, stok, booked)
        elif pilihan == '2':
            daftar_buku()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            kontak = input("Masukkan kontak mahasiswa: ")
            alamat = input("Masukkan alamat mahasiswa: ")
            menambahkan_mahasiswa(nama, nim, kontak, alamat)
        elif pilihan == '4':
            menambahkan_mahasiswa()
        elif pilihan == '5':
            nim = input("Masukkan NIM mahasiswa: ")
            no_isbn = input("Masukkan ISBN buku: ")
            pinjam_buku(nim, no_isbn)
        elif pilihan == '6':
            nim = input("Masukkan NIM mahasiswa: ")
            no_isbn = input("Masukkan ISBN buku: ")
            pe(nim, no_isbn)
        elif pilihan == '7':
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.") 
menu()