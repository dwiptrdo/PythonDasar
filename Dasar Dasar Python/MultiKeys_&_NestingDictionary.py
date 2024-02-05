# Multi Keys & Nesting Dictionary
import datetime

pelajar1 = {
    'nama':'Alfredo Dwi Putra',
    'kelas':'XII TKJ 4',
    'masuk':'2021',
    'lulus':2024,
    'pelajar':True,
    'lahir':datetime.datetime(2006,10,4)
}


pelajar2 = {
    'nama':'Fajar Ali Rohman',
    'kelas':'XII TKJ 2',
    'masuk':'2021',
    'lulus':2024,
    'pelajar':True,
    'lahir':datetime.datetime(2005,11,15)
}


pelajar3 = {
    'nama':'Munib Farikhul Aziz',
    'kelas':'XII TKJ 2',
    'masuk':'2021',
    'lulus':2024,
    'pelajar':True,
    'lahir':datetime.datetime(2005,11,4)
}

data_pelajar = {
    'KYS01':pelajar1,
    'KYS02':pelajar2,
    'KYS03':pelajar3
}

print(f'{'KEY':<19} {'NAMA':<21} {'KELAS':<11} {'MASUK':<10} {'LULUS':<10} {'PELAJAR':<10} {'LAHIR':<10}')
print('-'*93)

for pelajar in data_pelajar:
    KEY = pelajar

    NAMA = data_pelajar[KEY]['nama']
    KELAS = data_pelajar[KEY]['kelas']
    MASUK = data_pelajar[KEY]['masuk']
    LULUS = data_pelajar[KEY]['lulus']
    PELAJAR = data_pelajar[KEY]['pelajar']
    LAHIR = data_pelajar[KEY]['lahir'].strftime("%x")

    print(f'{KEY:<12} {NAMA:<26} {KELAS:^10} {MASUK:^10} {LULUS:^10} {PELAJAR:^11} {LAHIR:<10}')

# contoh jadi

# KEY                 NAMA                  KELAS       MASUK      LULUS      PELAJAR    LAHIR
# ---------------------------------------------------------------------------------------------
# KYS01        Alfredo Dwi Putra           XII TKJ      2021       2024         1      10/04/06
# KYS02        Fajar Ali Rohman            XII TKJ      2021       2024         1      11/15/05
# KYS03        Munib Farikhul Aziz         XII TKJ      2021       2024         1      11/04/05

