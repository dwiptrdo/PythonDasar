import datetime
import os
import string
import random


# template dict pelajar
template_pelajar = {
    'nama':'nama',
    'kelas':'kelas',
    'lulus':0,
    'lahir':datetime.datetime(2000, 2, 20)
}

data_pelajar = {}

while True:
    os.system("cls")
    print(f"{'DATA PELAJAR':^20}")
    print('-'*20)

    pelajar = dict.fromkeys(template_pelajar.keys())

    pelajar['nama'] = input('Nama Pelajar: ')
    pelajar['kelas'] = input('Kelas Pelajar: ')
    pelajar['lulus'] = int(input('Tahun Lulus Pelajar: '))
    TAHUN = int(input('Tahun Lahir (YYYY): '))
    BULAN = int(input('Bulan Lahir (1-12): '))
    TANGGAL = int(input('Tanggal Lahir (1-31): '))
    pelajar['lahir'] = datetime.datetime(TAHUN, BULAN, TANGGAL)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(3)))
    data_pelajar.update({KEY:pelajar})

    print(f'{'KEY':<19} {'NAMA':<21} {'KELAS':<11} {'LULUS':<10} {'LAHIR':<10}')
    print('-'*71)

    for pelajar in data_pelajar:
        KEY = pelajar

        NAMA = data_pelajar[KEY]['nama']
        KELAS = data_pelajar[KEY]['kelas']
        LULUS = data_pelajar[KEY]['lulus']
        LAHIR = data_pelajar[KEY]['lahir'].strftime("%x")

        print(f'{KEY:<12} {NAMA:<26} {KELAS:^10} {LULUS:^10} {LAHIR:<10}')
    print('\n')

    selesai = input('Sudah selesai? (y/n) : ')
    if selesai == "y":
        break

print('Prgram Telah Selesai!')

# contoh jadi:

# KEY                 NAMA                  KELAS       LULUS      LAHIR
# -----------------------------------------------------------------------
# XHT          Alfredo Dwi Putra          XII TKJ 4     2024    04/10/06
# VSL          Fajar Ali Rohman           XII TKJ 2     2024    11/15/05
# ZZP          Munib Farikhul Aziz        XII TKJ 2     2024    11/04/05
# DXK          Rohman Setiono             XII TKJ 4     2024    07/03/06