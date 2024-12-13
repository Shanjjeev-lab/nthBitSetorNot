def nthBitSectorNot(num, position):
    if num & (1 << (position - 1)):
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
position = int(input("Enter the position you want to check: "))
print(f"Bin of {num}: {bin(num)[2:]}")
result = nthBitSectorNot(num, position)

if result:
    print("It is a Set Bit")
else:
    print("It is not a Set Bit")
