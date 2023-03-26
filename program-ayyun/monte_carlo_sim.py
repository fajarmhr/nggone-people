import random

def monte_carlo_sim(N):
    #inisialisasi kondisi awal
    energy = 0
    n_A = 100 #jumlah awal A
    n_B = 50 #jumlah awal B

    for i in range(N):
        #menentukan kemungkinan berinteraksi
        prob = min(1, (n_A * n_B)/(n_A + n_B))
        if random.uniform(0, 1) < prob:
            n_A -= 1
            n_B -= 1
            energy -= 1
        else:
            n_A += 1
            n_B += 1
            energy += 1

    return (n_A, n_B, energy)

#menjalankan simulasi Monte Carlo dengan 10000 iterasi
result = monte_carlo_sim(10000)
print("Jumlah akhir A: ", result[0])
print("Jumlah akhir B: ", result[1])
print("Energi reaksi: ", result[2])
# Kode di atas menggunakan algoritma Monte Carlo untuk mensimulasikan reaksi antara A dan B dengan kondisi awal 100 molekul A dan 50 molekul B. Hasil simulasi menunjukkan jumlah akhir molekul A dan B setelah 10000 iterasi serta energi yang dibutuhkan untuk reaksi.