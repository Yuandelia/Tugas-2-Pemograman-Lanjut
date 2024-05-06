def input_nilai(n):
    for i in range(n):
        print(i**2)

n = int(input("Masukkan Nilai n: "))

if 1 <= n <= 20:
    input_nilai(n)