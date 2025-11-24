def decimaltohex(decimalValue):
    hex = ''

    while decimalValue != 0:
        hexValue = decimalValue % 16
        hex = toHexNumber(hexValue) + hex
        decimalValue = decimalValue // 16
    return hex

def toHexNumber(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue - 1 + ord('1'))
    else:
        return chr(hexValue - 10 + ord('A'))
    
def main():
    decimalValue = eval(input("Enter a decimal number: "))
    print(decimaltohex(decimalValue))

main()