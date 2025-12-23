def is_valid(plate):

    if len(plate) != 6:
        return False
    

    valid = "ABCEHKMOPTXY"
    

    if plate[0] not in valid: return False
    if plate[4] not in valid: return False
    if plate[5] not in valid: return False
    

    if not (plate[1].isdigit() and plate[2].isdigit() and plate[3].isdigit()):
        return False
        
    return True

n= int(input())
for i in range(n):
    plate= input()

    if is_valid(plate):
        print("Yes")
    else:
        print("No")