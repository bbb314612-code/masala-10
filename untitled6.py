# ===== Array1 =====
n = int(input("Array1 uchun n = "))
arr1 = []
for i in range(n):
    arr1.append(2 * i + 1)
print("Array1:", arr1)


# ===== Array2 =====
n = int(input("\nArray2 uchun n = "))
arr2 = []
for i in range(n):
    arr2.append(2 ** i)
print("Array2:", arr2)


# ===== Array3 =====
n = int(input("\nArray3 uchun n = "))
A = int(input("A = "))
D = int(input("D = "))
arr3 = [A]
for i in range(1, n):
    arr3.append(arr3[i-1] + D)
print("Array3:", arr3)


# ===== Array4 =====
n = int(input("\nArray4 uchun n = "))
A = int(input("A = "))
D = int(input("D = "))
arr4 = [A]
for i in range(1, n):
    arr4.append(arr4[i-1] * D)
print("Array4:", arr4)


# ===== Array5 =====
n = int(input("\nArray5 uchun n = "))
arr5 = [1, 1]
for i in range(2, n):
    arr5.append(arr5[i-1] + arr5[i-2])
print("Array5:", arr5[:n])


# ===== Array6 =====
n = int(input("\nArray6 uchun n = "))
A = int(input("A = "))
B = int(input("B = "))
arr6 = [A, B]
for i in range(2, n):
    arr6.append(sum(arr6))
print("Array6:", arr6)


# ===== Array7 =====
arr7 = list(map(int, input("\nArray7 massivni kiriting: ").split()))
print("Array7 (teskari):", arr7[::-1])


# ===== Array8 =====
arr8 = list(map(int, input("\nArray8 massivni kiriting: ").split()))
toq = []
for x in arr8:
    if x % 2 != 0:
        toq.append(x)
print("Toqlar:", toq)
print("Soni:", len(toq))


# ===== Array9 =====
arr9 = list(map(int, input("\nArray9 massivni kiriting: ").split()))
juft = []
for x in arr9:
    if x % 2 == 0:
        juft.append(x)
juft.sort(reverse=True)
print("Juftlar:", juft)
print("Soni:", len(juft))


# ===== Array10 =====
arr10 = list(map(int, input("\nArray10 massivni kiriting: ").split()))
juft = []
toq = []

for x in arr10:
    if x % 2 == 0:
        juft.append(x)
    else:
        toq.append(x)

juft.sort()
toq.sort(reverse=True)

print("Natija:", juft + toq)