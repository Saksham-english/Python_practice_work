#WAP to convert 
#decimal to binary and vice versa 
# decimal to hexa decimal and vice versa 
# octal to decimal and to binary and v.v. make use of default arguments , 
# positional arguments keywords argument and vice versa 
# Number Conversion Program

def convert_number(number, from_base=10, to_base=2):
    """
    Convert number from one base to another.
    Default: Decimal (10) to Binary (2)
    """

    # Convert input number to decimal first
    if from_base == 10:
        decimal = int(number)
    else:
        decimal = int(str(number), from_base)

    # Convert decimal to required base
    if to_base == 10:
        return decimal
    elif to_base == 2:
        return bin(decimal)[2:]
    elif to_base == 8:
        return oct(decimal)[2:]
    elif to_base == 16:
        return hex(decimal)[2:].upper()
    else:
        return "Unsupported base"


# ------------------------------
# 1️ Decimal to Binary (Default Argument)
print("Decimal to Binary (Default):", convert_number(10))

# 2️ Decimal to Hexadecimal (Positional Arguments)
print("Decimal to Hex:", convert_number(255, 10, 16))

# 3️ Binary to Decimal (Keyword Arguments)
print("Binary to Decimal:", convert_number(number="1010", from_base=2, to_base=10))

# 4️ Decimal to Hex using Keyword Argument
print("Decimal to Hex (Keyword):", convert_number(number=100, to_base=16))

# 5️ Octal to Decimal
print("Octal to Decimal:", convert_number("17", 8, 10))

# 6️ Octal to Binary
print("Octal to Binary:", convert_number("17", 8, 2))

# 7️ Hexadecimal to Decimal
print("Hex to Decimal:", convert_number("1A", 16, 10))

# 8️ Binary to Octal
print("Binary to Octal:", convert_number("1101", 2, 8))