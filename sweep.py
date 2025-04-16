# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 10:30:08 2025

@author: cdegrey
"""

import pyvisa
import time

# Initialiser PyVISA Resource Manager
rm = pyvisa.ResourceManager()

# Lister les instruments connectés
print("Instruments disponibles :", rm.list_resources())

# Déclaration des variables globales
instrument = None  # Pour la connexion à l'instrument

if instrument is None:
    try:
        instrument = rm.open_resource('GPIB0::5::INSTR')  # Connexion via GPIB
        print("Connecté à l'instrument")
    except Exception as e:
        print(f"Erreur lors de la connexion à l'instrument : {e}")
        exit()  # Arrêter l'exécution du programme si l'instrument n'est pas trouvé
        
        

try:
    instrument.write("FUNC SIN") #Fonction sinus
    instrument.write("VOLT 2")  #  2V
    instrument.write("FREQ:STAR 1")  # Fréquence de départ à 1 Hz
    instrument.write("FREQ:STOP 100") # Fréquence d'arrêt à 100 Hz
    instrument.write("SWE:SPAC LIN")  # Espacement linéaire
    #instrument.write("SWE:SPAC LOG")  # Espacement logarithmique
    instrument.write("SWE:TIME 2")    # Durée du balayage de 2 secondes
    #instrument.write("TRIG:SOUR IMM")  # Source de déclenchement immédiate
    instrument.write("TRIG:SOUR EXT")  # Source de déclenchement externe

    #Si on veut déclencher avec le BUS
    #instrument.write("TRIG:SOUR BUS")         # Déclenchement via le bus

    #time.sleep(1)  # Optionnel : laisser le temps au GBF de se configurer et lancer le Burts après 1s

    #instrument.write("*TRG")  # Déclenchement du Sweep

    instrument.write("SWE:STATE ON")  # Activer le balayage de fréquence
except Exception as e:
    print(f"Erreur lors de la configuration de l'instrument : {e}")
    
finally:
    # Fermer l'instrument proprement
    if instrument is not None:
        instrument.close()
        print("Connexion fermée.")
