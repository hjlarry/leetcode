# 另一个实现在stack中
def base_converter(num, base):
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    return base_converter(num // base, base) + digits[num % base]


print("25转二进制:", base_converter(25, 2))
print("960转十六进制:", base_converter(960, 16))
