# Fungsi dengan argument/parameter (input)


# Template
# def nama_fungsi(argument):
#     Badan Fungsi

def hello_world(nama):
    # fungsi hello world menerima input dengan variabel nama
    print(f"Selamat datang {nama}")

hello_world("Alfredo")
hello_world("Dwi")

# program tambah

def tambah(angka1, angka2):
    # fungsi tambah
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1, 4)
tambah(10, 7)


def say_hi(list_peserta):
    # fungsi say hi
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

    
anggota = ["Alfredo", "Dwi", "Putra"]

say_hi(anggota)
