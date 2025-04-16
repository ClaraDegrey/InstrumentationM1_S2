import pyvisa
import time

rm = pyvisa.ResourceManager()
inst = rm.open_resource('GPIB0::5::INSTR') 

inst.write("FUNC SIN")
inst.write("FREQ 1000")
inst.write("OUTP ON")

try:
    # Balayage d'amplitude de 1V à 3V par pas de 0.5V
    for amp in [1.0, 1.5, 2.0, 2.5, 3.0]:
        inst.write(f"VOLT {amp}")
        time.sleep(1)  # Pause d’1 seconde entre chaque amplitude
except Exception as e:
    print(f"Erreur lors de la configuration de l'instrument : {e}")
    
finally:
    # Fermer l'instrument proprement
    if inst is not None:
        inst.close()
        print("Connexion fermée.")
