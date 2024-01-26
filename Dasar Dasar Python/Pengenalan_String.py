data = 'Pengenalan String'
print(data)
print(type(data))

# 1. cara membuat string
'''
    Dengan double quote "..."
    dengan single quote '...'
'''

# 2. menggunakan \
# membuat tanda ' menjadi string
print('hari ini hari jum\'at')
# backslash
print("C:\\User\\Alfredo")
# tab
print('ini \t saya')
# backspace
print('ini \bsaya')
# newline
print('baris 1.\nbaris 2.') # LF (Line Feed)
print('baris 1.\rbaris 2.') # CR (Carriage Return)
print('baris 1.\r\nbaris 2.') # CRLF (Carriage Return Line Feed)

# 3. String literal atau Raw
# benar:
print('C:\\new folder')
# salah:
# print('C:\new folder')

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
    nama : Alfredo
    kelas : XII
""")

# multiline literal string dan Raw
print(r"""
    nama : Alfredo
    kelas : XII\newnormal
    web : www.alfred.com
""")
