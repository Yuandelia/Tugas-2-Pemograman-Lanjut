def kuadrat_ganjil(n):
    for i in range(n):
        if i % 2 != 0:  
            print(i**2)

n = int(input("Masukkan nilai n: "))

if n > 0:
    kuadrat_ganjil(n)