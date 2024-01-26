a = 9
b = 5

# bitwise OR(|)
c = a | b
print('nilai a = ',a ,'binary = ', format(a, '08b'))
print('nilai b = ',b, 'binary = ', format(b, '08b'))
print('bitwise (|)')
print('nilai c = ',c, 'binary = ', format(c, '08b'))

# bitwise AND (&)
print('\nBITWISE AND\n')
c = a & b
print('nilai a = ',a ,'binary = ', format(a, '08b'))
print('nilai b = ',b, 'binary = ', format(b, '08b'))
print('bitwise (&)')
print('nilai c = ',c, 'binary = ', format(c, '08b'))

# bitwise XOR (^)
print('\nBITWISE XOR\n')
c = a ^ b
print('nilai a = ',a ,'binary = ', format(a, '08b'))
print('nilai b = ',b, 'binary = ', format(b, '08b'))
print('bitwise (^)')
print('nilai c = ',c, 'binary = ', format(c, '08b'))

# bitwise NOT (~)
c = ~a
print('\nBITWISE NOT\n')
print('nilai a = ',a ,'binary = ', format(a, '08b'))
print('bitwise (~)')
print('nilai c = ',c, 'binary = ', format(c, '08b'))
print('bitwise (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai = ', e^d, 'binary = ', format(e^d, '08b'))

# shifting 
# shift right (>>)
c = a >> 2
print('\nBITWISE >>\n')
print('nilai a = ',a ,'binary = ', format(a, '08b'))
print('bitwise (>>)')
print('nilai c = ',c, 'binary = ', format(c, '08b'))

# shift left (<<)
c = a << 2
print('\nBITWISE <<\n')
print('nilai a = ',a ,'binary = ', format(a, '08b'))
print('bitwise (<<)')
print('nilai c = ',c, 'binary = ', format(c, '08b'))


