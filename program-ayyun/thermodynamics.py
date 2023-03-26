# This code is belong to Ayunita Maharani
import math, random, os, platform

# isian variabel dengan angka random
def angkarandom():
  global vaw, vak, n, taw, tak, cv, R, dv, dt, paw, pak
  vaw = random.uniform(1,50)
  vak = random.uniform(1,50)
  n = random.randint(1,20)
  taw = random.uniform(1,100)
  tak = random.uniform(1,100)
  cv = random.uniform(1,10)
  R = 8.314472
  dv = vak - vaw
  dt = tak - taw
  paw = n*R*taw/vaw
  pak = n*R*tak/vak

# input variabel
def masukan():
  global vaw, vak, n, taw, tak, cv, R, dv, dt, paw, pak
  vaw = float(input("Masukkan volume awal:\n"))
  vak = float(input("Masukkan volume akhir:\n"))
  n = float(input("Masukkan jumlah mol (n):\n"))
  taw = float(input("Masukkan suhu awal:\n"))
  tak = float(input("Masukkan suhu akhir:\n"))
  cv = float(input("Masukkan nilai kapasitas kalor volume tetap (Cv):\n"))
  R = 8.314472
  dv = vak - vaw
  dt = tak - taw
  paw = n*R*taw/vaw
  pak = n*R*tak/vak

# fungsi isotermal
def isotherm():
  print("Proses Isotermal\n")
  print("dalam proses isotermal ΔT = 0 dan W = Q, sehingga Δu = 0")
  print("rumusnya Q = W = n.R.T.ln(V2/V1)")
  print(f"Q=W = {n} x {R} x {taw} x ln({vak}/{vaw})")
  print(f"Q=W = {n * R * taw * math.log(vak/vaw)} Joule")

# fungsi isobarik
def isobar():
  print("Proses Isobarik\n")
  print("dalam proses isobarik Δp = 0")
  print("rumusnya W = p.ΔV")
  print(f"W = {paw} x ({vak}-{vaw})")
  print(f"W = {paw * dv} Joule")

# fungsi isokhorik
def isokhor():
  print("Proses Isokhorik\n")
  print("dalam proses isokhorik ΔV = 0")
  print("rumusnya Q = n.Cv.ΔT")
  print(f"Q = {n} x {cv} x ({tak} - {taw})")
  print(f"Q = {n * cv * dt} Joule")

# fungsi untuk mencari Δu
def deltau():
  Q=n*cv*dt
  W=paw*dv
  print(f"Δu = {Q} Joule - {W} Joule")
  print(f"Δu = {Q - W} Joule")

# fungsi menghapus tulisan di terminal
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

# This code runs only in python 3.10 or above versions
def number_to_string(choice):
  match choice:
    case 0:
      deltau()
    case 1:
      isotherm()
    case 2:
      isobar()
    case 3:
      isokhor()
    case default:
      return "Wrong Choice, terminating the program."

# main code
if __name__ == "__main__":
  choice = int(input("Pilihan Proses:\n\n0 Δu\n1 Isotermal.\n2 Isobarik.\n3 Isokhorik.\n\n"))
  clear()
  inp = int(input("1 Masukkan nilai variabel.\n2 Gunakan angka random\n\n"))
  clear()
  if inp == 1:
    masukan()
    clear()
  elif inp == 2:
    angkarandom()
  else:
    print("Wrong Choice, terminating the program.")

  number_to_string(choice)