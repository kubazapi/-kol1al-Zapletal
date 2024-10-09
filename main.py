import random

#první úkol
array1 = [random.randint(0,100)for _ in range(9)]
print("První pole:", array1)

#druhý úkol
print("První hodnota:", array1[0])
print("Prostřední hodnota:", array1[int(len(array1)/2)])
print("Poslední hodnota:", array1[-1])

#třetí úkol
array1[5]=34

#čtvrtý úkol
print("7 hodnota indexově je:", array1[6])

#pátý úkol
print("Délka pole je:", len(array1))

#šestý úkol
print("Minimální hodnota pole je:", min(array1))
print("Maximální hodnota pole je:", max(array1))

#sedmý úkol
array2 = [1,2,3,4,5,6,7,8,9]
print("Druhé pole:", array2)

#osmý úkol
print("Součet pole je:", sum(array2))

#devátý úkol
soucet = array2[0] + array2[4]
print("Součet indexově 1 a 5 pozice je:", soucet)