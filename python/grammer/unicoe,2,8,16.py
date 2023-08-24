print(ord('a'))
print(chr(97))
# encode, decode

value = 60
# 10진수 -> 2진수, 8진수, 16진수
b1 = format(value,'#b')  # 0b111100
# bin(value)
o1 = format(value,'#o')  # 0o74
# oct(value)
h1 = format(value,'#x')  # 0x3c
# hex(value)

b2 = format(value,'b')   # 111100
o2 = format(value,'o')   # 74
h2 = format(value,'x')   # 3c

# 2진수, 8진수, 16진수 -> 10진수
b3 = int('0b111100', 2)  # 60
o3 = int('0o74', 8)      # 60
h3 = int('0x3c', 16)     # 60

