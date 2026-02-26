#import modul yang akan digunakan
from datetime import datetime
from dateutil import parser
from prettytable import PrettyTable
from prettytable.colortable import ColorTable,Themes
from termcolor import colored

#membuat variabel berisikan data awal
data_karyawan = {
    '20120013' : {'Nama':'Asep Surasep','Tanggal Lahir':'12-03-1989','Divisi':'Marketing','Level':'Manager'},
    '20120015' : {'Nama':'Muhammad Bahlil','Tanggal Lahir':'30-01-1987','Divisi':'Finance','Level':'Manager'},
    '20120034' : {'Nama':'Andi Sutisna','Tanggal Lahir':'05-09-1990','Divisi':'Business Development','Level':'Manager'},
    '20130044' : {'Nama':'Robbi Ahmad Alfajri','Tanggal Lahir':'11-01-1990','Divisi':'General Affair','Level':'Manager'},
    '20130050' : {'Nama':'Maulana Septian','Tanggal Lahir':'10-09-1991','Divisi':'General Affair','Level':'Staff'},
    '20150014' : {'Nama':'Astiana Nur Azizah','Tanggal Lahir':'02-03-1995','Divisi':'Business Development','Level':'Staff'},
    '20190023' : {'Nama':'James Lebron','Tanggal Lahir':'04-07-1992','Divisi':'IT','Level':'Manager'},
    '20190035' : {'Nama':'Andhini Anggun Febri','Tanggal Lahir':'18-02-1991','Divisi':'IT','Level':'Staff'},
    '20200022' : {'Nama':'Ajeng Sekar Ayu','Tanggal Lahir':'13-04-1999','Divisi':'Marketing','Level':'Staff'},
    '20200041' : {'Nama':'Muhammad Indra','Tanggal Lahir':'09-07-1999','Divisi':'Finance','Level':'Staff'},
    '20220011' : {'Nama':'Radi Ramadhan Purba','Tanggal Lahir':'11-06-2000','Divisi':'HR','Level':'Manager'},
    '20230009' : {'Nama':'Pratama Agung','Tanggal Lahir':'23-05-2001','Divisi':'HR','Level':'Staff'},
}

for key, value in data_karyawan.items():
    data_karyawan[key]['Tanggal Lahir'] = datetime.strptime(data_karyawan[key]['Tanggal Lahir'],"%d-%m-%Y").date()

divisi_list = ['Marketing', 'Finance', 'General Affair', 'Business Development', 'IT', 'HR']
kolom_list = ['ID','Nama','Tanggal Lahir','Divisi','Level']

#membuat tabel untuk display menggunkan colortable
#setting tabel karyawan untuk display
tabel_karyawan = ColorTable(theme=Themes.EARTH)
tabel_karyawan.title = 'DATA KARYAWAN'
tabel_karyawan.field_names = ['ID','Nama','Tanggal Lahir','Divisi','Level']
for id, data in data_karyawan.items():
    tabel_karyawan.add_row([id, data['Nama'], data['Tanggal Lahir'], data['Divisi'], data['Level']])

tabel_menu_read = ColorTable(theme=Themes.LAVENDER)
tabel_menu_read.field_names = [colored('No.','magenta'), colored('Perintah','magenta')]
menu_read_dict = {1:"Urutkan tabel",2:"Kembali ke menu awal"}
for key, value in menu_read_dict.items():
    tabel_menu_read.add_row([key,value])

#setting display tabel karyawan yang digunakan untuk menampung data sementara    
tabel_karyawan_baru = ColorTable(theme=Themes.LAVENDER)
tabel_karyawan_baru.field_names = ['ID','Nama','Tanggal Lahir','Divisi','Level']

#setting display menu
tabel_menu = ColorTable(theme=Themes.LAVENDER)
tabel_menu.field_names = [colored('No.','magenta'), colored('Perintah','magenta')]
tabel_menu.title = colored('⋆༺❀༻⋆ MENU ⋆༺❀༻⋆','magenta',attrs=['bold'])
menu_dict = {1:"Tampilkan data karyawan",2:"Tambahkan data karyawan baru",3:"Hapus data karyawan",
                4:"Modifikasi data karyawan",5:"Keluar menu"}
for key, value in menu_dict.items():
    tabel_menu.add_row([key,value])

#defining function
def konfirmasi():
    konfirmasi_user = input(colored("Apakah semua sudah sesuai ? (Y/N) : ", "red", attrs=["bold"])).upper()
    if konfirmasi_user == 'Y':
        decision = 'break'
        return decision
    else:
        decision = 'continue'
        return decision
    
def id_generator():
    current_year = str(datetime.now().year)
    temp_list = []
    #mengecek apabila telah terdapat id dengan tahun yang sama pada database
    for key in data_karyawan.keys():
        if current_year in key[:4]:
            temp_list.append(key)
        else: 
            pass
    #set id karyawan menjadi urutan pertama jika tidak ditemukan id dengan tahun yang sama
    if not temp_list:
        new_id = current_year + '0001'
        return new_id
    #set id karyawan sesuai urutan sebelumnya
    else:
        last_row = int(max(temp_list))
        new_id = str(last_row + 1)
        return new_id

#defining CRUD function    
def read():
    print(tabel_karyawan)
    while True:
        print(tabel_menu_read)
        pilihan_read = int(input("Masukkan perintah yang ingin anda jalankan (1-2) : "))
        if pilihan_read == 1:
            while True:
                pilihan_kolom = input("Urutkan berdasarkan kolom : ")
                #mengubah format input menjadi sesuai dengan yang ada pada list kolom
                pilihan_kolom_convert = [col for col in kolom_list if col.casefold() == pilihan_kolom]
                if not pilihan_kolom_convert:
                    print(colored("Kolom yang anda masukkan tidak valid","red"))
                    continue
                else:
                    pilihan_kolom = "".join(pilihan_kolom_convert)
                    break

            #set urutan naik atau turun
            while True:
                pilihan_urutan = input("Ketik"+colored(' naik ',attrs=['italic'])+"untuk urutan naik, ketik"+colored(' turun ',attrs=['italic'])+"untuk urutan turun : ").lower()
                if pilihan_urutan == 'naik':
                    simbol = '↑'
                    break
                elif pilihan_urutan == 'turun':
                    simbol = '↓'
                    tabel_karyawan.reversesort = True
                    break
                else:
                    print(colored("Ketik 'naik' atau 'turun' : ","red"))
                    continue
            
            #highlight kolom yang digunakan sebagai acuan urutan
            kolom_baru = colored(pilihan_kolom+" "+simbol,"green","on_yellow",attrs=['bold'])
            kolom_read_list = ['ID','Nama','Tanggal Lahir','Divisi','Level']
            index_kolom = kolom_read_list.index(pilihan_kolom)
            kolom_read_list[index_kolom] = kolom_baru
            tabel_karyawan.field_names = kolom_read_list
            #set urutan tabel berdasarkan kolom yang dipilih
            tabel_karyawan.sortby = kolom_baru
            print(tabel_karyawan)
            #reset tabel karyawan menjadi default
            tabel_karyawan.sortby = None
            tabel_karyawan.reversesort = False
            tabel_karyawan.field_names = kolom_list
            
        elif pilihan_read == 2:
            break
        else:
            print(colored("Input tidak valid, ketik (1-2)","red"))
            continue

def create():
    global data_karyawan
    global tabel_karyawan
    
    while True:
        while True:
            nama = input("Masukkan nama karyawan : ").title()
            
            #konversi tanggal menjadi format yang sesuai
            while True:
                tanggal = input("Masukkan tanggal lahir : ")
                try:
                    tanggal_convert = parser.parse(tanggal,dayfirst=True)
                    tanggal_convert_str = tanggal_convert.date()
                    #tanggal_convert_str = tanggal_convert.strftime("%d-%m-%Y")
                    break
                except:
                    print("Tanggal lahir yang anda masukkan tidak valid")
                    continue
            
            #cek apakah divisi tersedia di perusahaan
            while True:
                divisi = input("Masukkan divisi : ")
                divisi_convert = [div for div in divisi_list if div.casefold() == divisi]

                if not divisi_convert:
                    print("divisi yang anda masukkan tidak valid")
                    continue
                else:
                    divisi = "".join(divisi_convert)
                    break
                
            level = input("Masukkan level : ").title()
            id = id_generator()
            
            #memasukan semua atribut yang telah diinput kedalam dictionary karyawan baru dan membuat tabel display sementara
            data_karyawan_baru = {'Nama':nama,'Tanggal Lahir':tanggal_convert_str,'Divisi':divisi,'Level':level}
            tabel_karyawan_baru.title = colored("BERIKUT DATA YANG AKAN DITAMBAHKAN KEDALAM DATABASE","magenta",attrs=['bold'])
            tabel_karyawan_baru.add_row([id,nama,tanggal_convert_str,divisi,level])
            print(tabel_karyawan_baru)
            tabel_karyawan_baru.clear_rows()
            if konfirmasi() == 'break':
                data_karyawan.update({id : data_karyawan_baru})
                print(colored("Data karyawan baru berhasil ditambahkan kedalam database !","green"))
                tabel_karyawan.add_row([id, nama, tanggal_convert_str, divisi, level])
                break
            else:
                continue
        pilihan = input("Apakah anda masih ingin menambahkan data lain ? (Y/N) : ").upper()
        if pilihan == 'Y':
            continue
        else:
            break

def delete():
    global tabel_karyawan
    global data_karyawan
    while True:
        while True:
            while True:
                #input id
                id = input("Masukkan ID karyawan : ")
                if id not in data_karyawan.keys():
                    print(colored("ID karyawan tidak ditemukan","red"))
                    continue
                else:
                    break
            #display data yang akan dihapus dengan tabel karyawan baru
            tabel_karyawan_baru.title = colored("BERIKUT MERUPAKAN DATA YANG AKAN DIHAPUS DARI DATABASE", "magenta", attrs=['bold'])
            tabel_karyawan_baru.add_row([id,data_karyawan[id]['Nama'],data_karyawan[id]['Tanggal Lahir'],
                                        data_karyawan[id]['Divisi'],data_karyawan[id]['Level']])
            print(tabel_karyawan_baru)
            tabel_karyawan_baru.clear_rows()
            if konfirmasi() == 'break':
                #menghapus data dari data karyawan sesuai dengan id
                data_karyawan.pop(id)
                print(colored("Data berhasil dihapus !","green"))
                
                #menghapus tabel karyawan untuk display dan membangunnya kembali
                tabel_karyawan.clear_rows()
                for id, data in data_karyawan.items():
                    tabel_karyawan.add_row([id, data['Nama'], data['Tanggal Lahir'], data['Divisi'], data['Level']])
                break
            else:
                continue
        pilihan = input("Apakah anda masih ingin menghapus data lain ? (Y/N) : ").upper()
        if pilihan == 'Y':
            continue
        else:
            break

def update():
    while True:
        while True:
            global data_karyawan
            global tabel_karyawan
            
            #input id
            while True:
                id = input("Masukkan ID karyawan : ")
                if id not in data_karyawan.keys():
                    print(colored("ID karyawan tidak ditemukan","red"))
                    continue
                else:
                    break
            
            #display data yang akan dimodifikasi
            tabel_karyawan_baru.title = colored("BERIKUT DATA YANG AKAN DIMODIFIKASI","magenta",attrs=['bold'])
            tabel_karyawan_baru.add_row([id,data_karyawan[id]['Nama'],data_karyawan[id]['Tanggal Lahir'],
                                                data_karyawan[id]['Divisi'],data_karyawan[id]['Level']])
            print(tabel_karyawan_baru)
            tabel_karyawan_baru.clear_rows()
            
            #input kolom dan value baru
            while True:
                kolom = input("Masukkan kolom data yang akan diubah : ").title()
                if kolom in ['ID','Id']:
                    print(colored("ID tidak dapat dimodifikasi","red"))
                    continue
                elif kolom not in kolom_list:
                    print(colored("Kolom yang anda masukkan tidak valid","red"))
                    continue
                else:
                    break
                  
            if kolom == 'Tanggal Lahir':
                while True:
                    value = input("Masukkan data baru kedalam kolom : ")
                    try:
                        tanggal_convert = parser.parse(value)
                        value = tanggal_convert.date()
                        break
                    except:
                        print(colored("Tanggal lahir yang anda masukkan tidak valid","red"))
                        continue
            elif kolom == 'Divisi':
                value = input("Masukkan data baru kedalam kolom : ")
                while True:
                    divisi_convert = [div for div in divisi_list if div.casefold() == value]

                    if not divisi_convert:
                        print(colored("divisi yang anda masukkan tidak valid","red"))
                        continue
                    else:
                        value = "".join(divisi_convert)
                        break
            else:
                value = input("Masukkan data baru kedalam kolom : ").title()
            
            #display data dengan atribut baru
            data_karyawan_modifikasi = {id:data_karyawan[id]}
            data_karyawan_modifikasi[id][kolom] = value
            tabel_karyawan_baru.title = "BERIKUT DATA YANG TELAH DIMODIFIKASI"
            tabel_karyawan_baru.add_row([id,data_karyawan_modifikasi[id]['Nama'],data_karyawan_modifikasi[id]['Tanggal Lahir'],
                                         data_karyawan_modifikasi[id]['Divisi'],data_karyawan_modifikasi[id]['Level']])
            print(tabel_karyawan_baru)
            tabel_karyawan_baru.clear_rows
            data_karyawan_modifikasi.clear()
    
            if konfirmasi() == 'break':
                #mengubah informasi pada data karyawan
                data_karyawan[id][kolom] = value
                print(colored("Data berhasil dimodifikasi !","green"))
                
                #menghapus tabel karyawan dan membangun kembali tabel display dengan data karyawan yang telah terupdate
                tabel_karyawan.clear_rows()
                for id, data in data_karyawan.items():
                    tabel_karyawan.add_row([id, data['Nama'], data['Tanggal Lahir'], data['Divisi'], data['Level']])
                tabel_karyawan_baru.clear_rows()
                break
            else:
                continue
        pilihan = input("Apakah anda masih ingin memodifikasi data lain ? (Y/N) : ").upper()
        if pilihan == 'Y':
            continue
        else:
            break
        
def exit():
    print(colored("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⡀⠀⢄⠈⢙⢒⠲⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠚⠃⢣⠀⠸⣶⠋⢈⠇⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠤⢄⡀⠀⠀⢀⣤⣶⢖⣿⣏⡷⠰⠞⠉⠉⢺⣇⠀⢹⠀⢸⡀⠋⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠤⠶⣚⣋⡅⠀⠀⠙⣻⡟⠋⡔⠛⠉⠁⠙⣷⠀⠰⣿⡄⠀⢻⡆⠀⢧⠀⠙⢦⠀⡿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣯⡵⠛⠛⠉⠈⣷⠀⠘⠉⠀⠙⢦⡀⠀⣾⣆⠀⢻⣇⠀⢳⣳⡀⠘⣷⣀⣨⠙⢲⣒⣤⢣⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡿⡇⢴⠀⠀⣿⠈⣇⠀⢸⣣⡀⠘⣧⡀⠙⠿⠀⠈⣿⣄⣸⡏⢻⣾⣥⢨⣿⣿⠿⠛⠛⠉⠀⠀⣀⣤⣤⠤⠤⣒⡲⠤⠤⣤⣤⣤⣤⣀⡀⢧⡀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠻⡆⢧⠀⠹⡄⢹⡄⠘⢏⢧⠀⢸⡷⣤⣤⣶⣚⠋⢸⠛⢳⣿⡅⠘⢇⢷⣿⠀⠀⣤⢔⣻⡯⠶⠛⠛⠋⠉⠉⠉⠉⣉⣉⣛⡛⠓⢲⣬⡝⣷⣤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⡘⡆⠀⢻⠀⢳⣄⣼⠛⢳⣾⢥⣴⠛⠉⠁⠉⢻⡄⠈⢣⢣⠀⠸⡎⠈⣧⣯⡾⠋⠁⠀⣠⣤⣴⣾⣿⣿⣿⣿⠿⢛⣭⣴⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⡛⠀⠚⢰⣿⣿⠛⠳⣼⡇⠀⣿⠀⠘⣟⡄⠈⢳⡀⠘⠿⠃⢠⡇⣠⣿⠛⢀⣤⣾⣿⣿⣿⣿⣿⡿⠟⣫⣤⣞⡯⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠪⠖⢻⣝⣦⠀⠘⠇⠀⡟⣦⠀⠛⠿⠀⡼⠓⡦⠤⠴⣫⣤⣿⡁⣠⣿⣿⣿⣿⣿⡿⢿⣡⡴⣿⡭⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢎⠳⡄⠀⠀⡇⢈⣓⣦⡴⢛⡥⣺⡿⠿⢿⣿⣿⠁⣵⣿⣿⣿⡿⠟⣡⣴⣿⣳⣛⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠤⠒⢦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠈⠆⠀⡧⢸⣿⠛⠛⠛⠛⠁⠀⣠⣾⣿⠃⣼⣿⣿⣿⢋⣴⠞⠋⠀⠴⠿⠿⣿⣯⣹⣀⣀⣀⡀⠀⠀⠀⠀⠀⣘⣦⣤⣀⠈⠑⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⣴⣃⡬⣿⣁⡀⠀⠀⠀⣼⣿⢿⡇⡴⠋⠀⣻⡿⠛⠁⠀⠀⠀⠀⠀⠀⠉⢙⣶⡿⠿⠿⠭⣍⣒⣶⢤⣀⣏⣀⠉⠓⣝⡄⠈⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢷⡿⠋⢉⣿⠀⢀⣞⡿⠃⠸⠃⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢦⣤⣀⣀⡀⠈⠉⠳⢮⣝⠯⣶⡀⠈⣿⠦⠼⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣰⡟⠀⣰⡿⠋⢹⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣿⣿⣷⣶⣄⡀⠉⠳⣝⢿⡉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣽⣿⣿⣏⣿⠀⠀⣿⠁⢠⣿⢻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣝⠿⣿⣿⣿⣿⣿⣿⣷⣄⠘⢷⣙⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⡿⠞⠉⠸⢏⣾⡟⠉⢷⡀⣿⣦⣼⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣶⣌⡙⠿⣿⣿⣿⣿⣿⣷⣄⠻⣍⢦⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⢸⣿⡇⠀⠈⢉⣿⢿⣿⣫⣿⠀⠀⠀⠀⠀⣀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣱⠁⠙⠯⢿⡶⣤⣉⡻⠿⣿⣿⣿⣦⠙⣮⢦⠀⠀⠀
⠀⠀⠀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠘⣟⣇⣀⣶⡯⠟⠋⠉⠀⢹⣆⠀⠀⠀⠀⠻⣦⣄⣀⣤⡶⠀⠀⠀⠀⠀⢐⠶⢀⣴⣿⠁⠀⠀⠀⠀⠉⠙⠯⢽⣷⡶⣍⣙⠻⣷⠈⢯⣣⡀⠀
⠀⠀⡼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠹⣾⣿⣋⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⢀⣀⠀⠘⠷⠛⣿⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠻⢿⣶⣤⣜⢯⣣⡀
⠀⢸⣿⠃⢰⠀⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⠖⠀⠀⠀⠀⠀⠀⠀⢹⣷⣤⡀⠀⠀⠀⠀⣷⣄⣀⣀⣈⡉⣀⡀⠀⢠⡿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣟⠇⠇
⢀⣿⡟⠀⠀⠀⣿⠀⢰⣇⠀⡴⠂⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠉⠛⠶⣤⣤⡀⠀⠉⠉⠁⠈⠙⢋⣠⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁
⢸⣿⡇⠀⠀⠀⠻⣄⣸⠙⢦⡀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠛⢿⣷⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡇⠀⠀⠀⠀⠙⠋⠀⠀⠹⠀⠀⢸⡿⣦⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠈⢷⣄⢀⣄⢰⣷⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⠙⠟⣿⣿⠻⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢷⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠲⣿⠀⠉⠹⣿⣦⠀⠀⠀⠀⠀⠀⢀⡀⢀⣰⣷⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⢟⣷⣄⡀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⢹⣇⠀⠀⠈⢙⣿⣷⡀⠀⢀⣴⣿⣴⣟⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠿⢟⣶⣤⣄⣀⣀⣀⣨⣿⣦⣀⣀⣀⣀⣀⣿⡄⠀⠀⠈⠉⣿⣿⡶⠛⠉⠀⣾⡝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠒⠚⠛⠓⠊⠉⠿⣿⣿⡋⢹⡁⣸⢷⡄⠀⠀⠀⠸⣆⣀⠀⠀⣾⣽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠯⠭⠭⠭⢽⣿⣦⡀⠰⣄⢺⣿⣆⣾⣽⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠚⠛⠲⣻⣛⣿⡿⣿⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""", "light_yellow"))
    
            
#Run program
while True:
    print(tabel_menu)
    try:
        menu_pilihan = int(input("Masukkan perintah pada menu yang ingin dijalankan (1-5) : "))
    except:
        print(colored("Input tidak valid, silahkan masukkan angka 1-5","red"))
        continue
    if menu_pilihan == 1:
        read()
    elif menu_pilihan == 2:
        create()
    elif menu_pilihan == 3:
        delete()
    elif menu_pilihan == 4:
        update()
    elif menu_pilihan == 5:
        exit()
        break
    else:
        print(colored("Input tidak valid, silahkan masukkan angka 1-5","red"))
        continue
            
            