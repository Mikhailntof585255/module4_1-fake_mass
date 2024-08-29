def divide(first, second):
    rez1 = str
    if second == 0:
        rez1 = "Ошибка"
        return rez1
    rez = first / second
    return rez


rezuilt1 = divide(69, 3)
rezuilt2 = divide(3, 0)
rezuilt3 = divide(49, 7)
#rezuilt4 = divide(15, 0)
print(rezuilt1)
print(rezuilt2)
print(rezuilt3)
#print(rezuilt4)
