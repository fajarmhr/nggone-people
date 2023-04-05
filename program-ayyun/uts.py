# This code is belong to Ayunita Maharani
# Define the given values
mass_precentage_h2so4 = 96 # %
density_h2so4 = 1.8 # g/mL
density_h2o = 1 # g/mL
Mr_h2so4 = 98  # g/mol
Mr_h2o = 18  # g/mol

# fungsi persen volume
def persenvolume():
  print("\nPersen Volume\n")
  print("rumus %V = %m H2SO4 / ρ H2SO4 x 100%")
  print(f"%V = {mass_precentage_h2so4} / {density_h2so4} x 100%")
  print(f"%V = {mass_precentage_h2so4/density_h2so4*100} %")

# fungsi persen massa per volume
def persenmassapervolume():
  print("\nPersen Massa per Volume\n")
  print("rumus %m/v = %m H2SO4 / (ρ H2SO4 - ρ H2O) x 100%")
  print(f"%m/v = {mass_precentage_h2so4} / ({density_h2so4} - {density_h2o}) x 100%")
  print(f"%m/v = {mass_precentage_h2so4/(density_h2so4-density_h2o)*100} %")

# fungsi ppm
def ppm():
  print("\nppm\n")
  print("rumus ppm = ρ H2SO4 / Mr H2SO4 x %m H2SO4 x 10000")
  print(f"ppm = {density_h2so4} / {Mr_h2so4} x {mass_precentage_h2so4} x 10000")
  print(f"ppm = {density_h2so4/Mr_h2so4*mass_precentage_h2so4*10000} mg/L")

# fungsi molaritas
def molaritas():
  print("\nMolaritas\n")
  print("rumus M = ρ H2SO4 x %m H2SO4 / (Mr H2SO4 x 10000)")
  print(f"M = {density_h2so4} x {mass_precentage_h2so4} / ({Mr_h2so4} x 1000)")
  print(f"M = {density_h2so4*mass_precentage_h2so4/(Mr_h2so4*1000)} M")

# fungsi molalitas
def molalitas():
  print("\nMolalitas\n")
  print("rumus m = ρ H2SO4 x %m H2SO4 / (Mr H2SO4 + Mr H2O) / 1000")
  print(f"m = {density_h2so4} x {mass_precentage_h2so4} / ({Mr_h2so4} + {Mr_h2o} ) / 1000")
  print(f"m = {density_h2so4*mass_precentage_h2so4/(Mr_h2so4+Mr_h2o)/1000} m")

# fungsi normalitas
def normalitas():
  print("\nNormalitas\n")
  print("rumus N = M x Mr H2SO4/ 2")
  print(f"N = {(density_h2so4*mass_precentage_h2so4/(Mr_h2so4+Mr_h2o)/1000)*Mr_h2so4/2} M")

# fungsi fraksi mol
def fraksimol():
  print("\nFraksi Mol\n")
  print("rumus N = M x Mr H2SO4/ 2")
  print(f"Xt = {mass_precentage_h2so4 / Mr_h2so4 / (mass_precentage_h2so4 / Mr_h2so4 + (100 - mass_precentage_h2so4) / Mr_h2so4)} mol")

# main code
if __name__ == "__main__":
  print("Diketahui :")
  print("%mass H2SO4 = 96%\nρ H2SO4 = 1,8 g/mL\nρ H2O = 1 g/mL\nMr H2SO4 = 98\nMr H2O = 18")
  persenvolume()
  persenmassapervolume()
  ppm()
  molaritas()
  molalitas()
  normalitas()
  fraksimol()
