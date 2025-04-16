# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 17:23:10 2025

@author: cdegrey
"""

# -*- coding: utf-8 -*-
"""
Génération d'un signal sinusoïdal en mode burst (rafale) avec déclenchement externe.
"""

import pyvisa
import time

# Initialiser PyVISA
rm = pyvisa.ResourceManager()
print("Instruments disponibles :", rm.list_resources())

# Connexion au GBF (adapter l’adresse si nécessaire)
try:
    instrument = rm.open_resource('GPIB0::5::INSTR')  # Exemple d'adresse
    print("Connecté à :", instrument.query("*IDN?"))
except Exception as e:
    print("Erreur de connexion :", e)
    exit()

try:
# ---------------- CONFIGURATION ----------------
    instrument.write("FUNC SQR")              # Signal carré
    instrument.write("FREQ 1000")             # Fréquence 1 kHz
    instrument.write("VOLT 2")                # Amplitude 2 Vpp
    instrument.write("VOLT:OFFS 0")           # Offset 0 V

    instrument.write("BURS:STAT ON")          # Activer le mode rafale
    instrument.write("BURS:NCYC 5")           # 5 cycles par rafale
    instrument.write("BURS:MODE TRIG")        # Mode rafale déclenchée

    #instrument.write("TRIG:SOUR IMM")  # Source de déclenchement immédiate
    #instrument.write("BURST:TIME 2")    # Durée de répétition du burst de 2 secondes si on veut que le signal se répète en déclenchement immédiat
    instrument.write("TRIG:SOUR EXT")         # Déclenchement EXTERNE
    instrument.write("TRIG:SLOP POS")         # Front MONTANT

    instrument.write("OUTP ON")               # Activer la sortie

    #Si on veut déclencher avec le BUS
    #instrument.write("TRIG:SOUR BUS")         # Déclenchement via le bus

    #time.sleep(3)  # Optionnel : laisser le temps au GBF de se configurer et lancer le Burts après 3s

    #instrument.write("*TRG")  # Déclenchement du Sweep

except Exception as e:
    print(f"Erreur lors de la configuration de l'instrument : {e}")
    
finally:
    # Fermer l'instrument proprement
    if instrument is not None:
        instrument.close()
        print("Connexion fermée.")

