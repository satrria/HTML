import random
import string
# pylint: disable=E1103
data_nasabah = []
nama = []
nomor_rekening = []
saldo = []

def singleList() :
    for i in data_nasabah :
        for j in i :
            nomor_rekening.append(j)

def openFile():
    f = open('nasabah.txt')
    for line in f:
        data = line.split(",")
        data_nasabah.append([data[0], data[1], int(data[2])])
    f.close()

# --- Fungsi Menu --- 
def menu() : 
    
    print("***** SELAMAT DATANG DI NF BANK *****") # program akan mencetak tulisan yang di dalem kurung
    print("MENU:") # program akan mencetak tulisan yang di dalem kurung
    print("[1] Buka rekening\n[2] Setoran tunai\n[3] Tarik tunai\n[4] Transfer\n[5] Lihat daftar transfer\n[6] Keluar")# program akan mencetak tulisan yang di dalem kurung

# --- Fungsi Buka Rekening ---
def bukaRekening() :
    f = open('nasabah.txt', 'a+') #untuk membuka file nasabah.txt

    print('\n*** BUKA REKENING ***') #program akan mencetak tulisan didalemkurung
    nama = input('Masukkan nama: ') #program meminta user memasukan nama
    setoran = int(input('Masukkan setoran awal: ')) #program meminta user memasukan nominal setoran awal
    norek = "REK" + ''.join(random.choice(string.digits) for i in range(3)) #ini copy paste dari pdf
     
    if setoran >= 50000: #jika if bernilai true atau setoran lebih dari sama dengan 50000
        nasabah = [norek, nama, str(setoran)] #variabel untuk memuat variabel norek, nama, dan setoran yang di ubah ke string ke dalam list
        print('Pembukaan rekening dengan nomor ' + norek + ' atas nama ' + nama + ' berhasil.') #program akan mencetak tulisan yag di dalem kurung
        f.write('\n'+','.join(nasabah)) #program akan menulisakan yang di dalamkurung pada file yang di buka
        f.close() #program menutup file yang dibuka
    else: #jika if bernilai false
        print("Nominal tidak bisa di masukan, Minimal setoran awal adalah 500000") #program akan mencetak tulisan yang di dalem kurung


    menu() #programmenjalankan fungsi menu

# --- Fungsi Setoran Tunai ----
def setoranTunai() :
    print('*** SETORAN TUNAI ***') #program mencetak tulisan yang di dalem kurung
    rekening = input("Masukan nomor rekening: ").upper() #program memerintah user memasukan nomor rekening
    nominal = int(input("Masukan nominal yang akan disetor: ")) #program menyuruh user memasukan nominal yang di setor
    openFile() #programmenjalankan fungsi open file 
    singleList() #program menjalankan fungsi single list
    if rekening in nomor_rekening : #jika if bernilai true atau rekening berada di dalam variabel nomor_rekening
        for i in data_nasabah: #perulangan di dalam variabel data_nasabah
            if i[0] == rekening : #jika if bernilai true atau i index 0 sama dengan rekening 
                if nominal < 0: #dan jika nominal kurang dari 0
                    print("Nominal tidak bisa dimasukan") #program akan mencetak tulisan di dalem kurung
                else: # jika if bernilai false
                    print("Setoran tunai sebesar", nominal, "ke rekening", rekening, "berhasil") #program akan mencetak tulisan di dalem kurung
                    i[2] += nominal #i index 2 akan di tambah dengan nominal yang di masukan
                    f = open("nasabah.txt", "w") #program membuka file nasabah.txt
                    f.write('\n'.join(map(lambda x: ','.join(map(str,x)), data_nasabah))) #program akan menulisakan tulisan yang di dalamkurung ke dalam file nasabah.tx
                    f.close()#program menutup file yang dibuka
                    break
    else :
        print("Nomor rekening tidak terdaftar. Setoran tunai gagal")#program akan mencetak tulisan di dalem kurung

    menu()

# --- Fungsi Tarik Tunai ---
def tarikTunai() :
    print('*** TARIK TUNAI ***')#program akan mencetak tulisan di dalem kurung
    rekening = input("Masukan nomor rekening: ").upper()#program akan meminta user untuk memasukan nomor rekening
    nominal = int(input("Masukan nominal yang akan ditarik: "))#program akan meminta user untuk memasukan nominal yang di tarik
    openFile() #program menjalankan fungsi open file
    singleList() #program menjalankan fungsi single list
    if rekening in nomor_rekening : #jika if bernilai true atau rekening berada di dalam nomor_rekening
        for i in data_nasabah: #perulangan pada variabel data_nasabah
            if i[0] == rekening : #jika if bernilai true atau i index 0 sama dengan rekening
                if i[2] < nominal : #jika if bernilai true atau i index 2 bernilai kurang dari nominal
                    print ("Saldo tidak mencukupi. Tarik tunai gagal.")#program akan mencetak tulisan di dalem kurung
                    break #untuk memberhentikan perulangan
                else :
                    i[2] -= nominal 
                    f = open("nasabah.txt", "+w")#program membuka file nasabah.txt
                    f.write('\n'.join(map(lambda x: ','.join(map(str,x)), data_nasabah))) #program menulis tulisan di dalam kurung dan di tulis di dalem file nasabah.txt
                    #lambda buat bikin anonimus fungsi atau fungsi sekali pake
                    f.close() #program menutup file yang dibuka
                    print("Tarik tunai sebesar", nominal, "dari rekening", rekening, "berhasil")#program akan mencetak tulisan di dalem kurung
                    break
    elif nominal < 0:
        print("Nominal tidak bisa dimasukan")#program akan mencetak tulisan di dalem kurung
    else :
        print("Nomor rekening tidak terdaftar. Setoran tunai gagal")#program akan mencetak tulisan di dalem kurung

    menu() #program menjalankan fungsi menu

# ---- Fungsi untuk menjalankan menu Transfer ----
def transfer() : 
    print('*** TRANSFER ***') #program akan mencetak tulisan pada tanda kutip
    norek_asal = input("Masukkan nomor rekening sumber: ").upper() #program akan meminta user untuk memasukan norek sumber
    norek_tujuan = input("Masukkan nomor rekening tujuan: ").upper() #program akan meminta user untuk memasukan norek tujuan
    nominal_transfer = int(input("Masukkan nominal yang akan ditransfer:")) #program akan meminta user untuk memasukan nominalyang di transfer
    data_dict = {} #variabel untuk menyimpan dictionary kosong
    f = open("nasabah.txt") #program akan membuka file nasabah.txt
    for i in f : #perulangan untuk variabel f
        i = i.split(",") #variabel i akan di pisahkan bedasarkan tanda koma
        data_dict[i[0]] = [i[1], int(i[2])] #programakan mengisi dictionary kosong dengan key dan value yang di tentukan yaitu i index 1 dan i index 2
    if norek_asal in data_dict and norek_tujuan in data_dict : #jika norek_asal dan norek tujuan berada dalam data_dict maka akan berjalan programdi bawahnya
        for i in data_dict : #perulangan pada variabel data_dict
            if i == norek_asal : #jika variabel i sama dengan norek_asal maka program di bawah aakan berjalan
                if nominal_transfer < 0 : #jika if bernilai true atau kurang dari 0 
                    print("Nominal tidak bisa di transfer") #program akan menulisakan tulisan dalem tanda kurung
                elif nominal_transfer > data_dict[norek_asal][1] : #untuk if diatas bernilai false dan elif bernilai true atu nominal_transfer lebih besar dari data_dict dengan key norek_asal dan value index 1
                    print("Saldo tidak mencukupi. Transfer gagal.")  #program akan menulisakan tulisan dalem tanda kurung     
                else : #jika if dan elif bernilai false
                    data_dict[norek_asal][1] -= nominal_transfer #data_dict dengan key norek_asal dan value index 1 akan di kurang dengan nominal              
                    data_dict[norek_tujuan][1] += nominal_transfer #data_dict dengan key norek_tujuan dan value index 1 akan di tambah dengan nominal
                    f = open("nasabah.txt", "w") #program membuka file nasabah.txt dan overwrite
                    for x, y in data_dict.items() : #perulangan pada variabel dan mengembalikan daftar key dan value
                        data_dictionary = [x, y[0],str(y[1])] #program akan mengisi data_dictionary dengan list yang berisi seperti di dalamkurung
                        f.write("\n" + ",".join(data_dictionary)) #program menulis yang ada di dalam kurung ke dalam file nasabah.txt
                        #join untuk mengubah nilai list menjadi string
                    no_trf = "TRF" + ''.join(random.choice(string.digits) for i in range(3)) #ini yang ada di pdf tingal kopi paste
                    transfer = [no_trf, norek_asal, norek_tujuan, str(nominal_transfer)] #varibel yang berisi list
                    f = open("transfer.txt", "a+") #membuka file.transfer dan men append
                    f.write("\n" + ",".join(transfer)) #program menuliskan seperti yang di dalam kurung ke dalam file transfer.txt
                    #join undtuk mengubah list jadi string
                    print("Transfer sebesar", nominal_transfer, "dari rekening", norek_asal, "ke rekening", norek_tujuan, "berhasil.")#program akan mencetak tulisan yang di dalem kurung
    elif norek_asal not in data_dict : #jika if bernilai false dan elif bernilai true dan norek _asal tidak ada di dalam data_dict
        print("Nomor rekening sumber tidak terdaftar. Transfer gagal.") #program akan mencetak tulisan yang di dalem kurung
    else: #jika if dan elif bernilai false
        print("Nomor rekening tujuan tidak terdaftar. Transfer gagal.")#program akan mencetak tulisan yang di dalem kurung               

    f.close() #program menutup file
    menu() #syntax untuk menjalankan fungsi menu

# --- Fungsi Lihat daftar transfer ---
def lihatDaftarTransfer() :
    print('*** LIHAT DATA TRANSFER ***') #program akan mencetak tulisan yang di dalem kurung
    sumber = input('Masukkan nomor rekening sumber transfer: ').upper() #user di suruh memasukan nomor rekening sumber
    cek = 0 #untuk menngecek nomor rekening sumber jika 0 berarti ga ada
    f = open("nasabah.txt") #untuk membuka file nasabah.txt
    for line in f : #untuk perulangan setiap baris di file nasabah
        lists = line.split(',') #untuk memisahkan data dalam line
        if lists[0] == sumber : # jika index 0 nya sama dengan sumber program lanjut 
            cek = 1 #untuk menngecek nomor rekening sumber jika 1 berarti ada

    if cek == 0 :#untuk menngecek nomor rekening sumber jika 0 berarti ga ada
        print('Nomor rekening sumber tidak terdaftar.') #program akan mencetak tulisan dalam kurungnya
        return menu() #kembali ke fungsi menu
            
    daftar = [] #list kosong
    f = open("transfer.txt") #untuk membuka file transfer.txt
    for line in f : #perulangan pada variable f
        lists = line.split(',') #untuk memisahkan antar string pada variabel ine
        if lists[1] == sumber : #jika index 1 pada lists sama dengan sumber rekening 
            daftar.append(lists) #variabel datar akan di tambah oleh variabel lists

    if len(daftar) == 0 : #jika panjang string dalam daftar sama dengan 0 
        print('Tidak ada data yang ditampilkan.') #program akan mencetak tulisan yang di dalem kurung
    else : #jika semua if tidak terpenuhi maka akan ke sini
        for i in daftar : #program akan melakukan perulangan pada variabel daftar
            print(i[0], i[1], i[2], i[3]) #program akan mencetak i index 0 i index 1 i index 2 i index 3 
    menu() #syntax untuk menjalankan fungsi menu


menu() #syntax untuk menjalankan fungsi menu
while True : #program di bawah akan berjalan terus menerus
    c = input('Masukkan menu pilihan Anda: ') # variabel untuk user memasukan menu pilihan nya
    if c == "1" : # jika user memilih inputan menu 1 akan berjalan program di bawahnya  
        bukaRekening() #syntax untuk menjalankan fungsi buka rekening
    elif c == "2" : # jika user memilih inputan menu 2 akan berjalan fungsi di bawahnya
        setoranTunai() #syntax untuk menjalankan fungsi setor tunai
    elif c == "3" : # jika user memilih inputan menu 3 akan berjalan fungsi di bawahnya
        tarikTunai() #syntax untuk menjalankan fungsi tarik tunai
    elif c == "4" : # jika user memilih inputan menu 4 akan berjalan fungsi di bawahnya
        transfer() #syntax untuk menjalankan fungsi transfer
    elif c == "5" : # jika user memilih inputan menu 5 akan berjalan fungsi di bawahnya
        lihatDaftarTransfer() #syntax untuk menjalankan fungsi lihat daftar transfer
    elif c == "6" : # jika user memilih inputan menu 6 akan berjalan fungsi di bawahnya
        break  # syntax untuk memberhentikan sebuah perulangan 
    else: #jika user memasukan inputan selain pilihan yang di atas akan berjalan program dibawah ini
        print('pilihan anda salah, Ulangi') # program akan mencetak 'pilihan anda salah, Ulangi'.

print('Terima kasih atas kunjungan Anda...') # program mencetak 'Terima kasih atas kunjungan Anda...' setelah perulangan di berhentikan oleh fungsi break