# -*- coding: utf-8 -*-
"""
Génération et synchronisation de signaux de type "burst" entre deux générateurs de signaux
(GBF), un en sinusoidal et l'autre en carré, avec déclenchement externe.
"""

import pyvisa
import time

# Initialiser PyVISA
rm = pyvisa.ResourceManager()
print("Instruments disponibles :", rm.list_resources())

# Connexion aux deux GBF (adapter l'adresse GPIB ou TCP/IP si nécessaire)
try:
    GBF_1 = rm.open_resource('GPIB0::5::INSTR')  # Exemple d'adresse pour GBF1
    GBF_2 = rm.open_resource('GPIB0::6::INSTR')  # Exemple d'adresse pour GBF2
    print("Connecté à :", GBF_1.query("*IDN?"))
    print("Connecté à :", GBF_2.query("*IDN?"))
except Exception as e:
    print("Erreur de connexion :", e)
    exit()

try:
    # ---------------- CONFIGURATION POUR LE PREMIER GBF (GBF1) ----------------
    GBF_1.write("FUNC SIN")              # Signal sinusoïdal
    GBF_1.write("FREQ 1000")             # Fréquence 1 kHz
    GBF_1.write("VOLT 2")                # Amplitude 2 Vpp
    GBF_1.write("VOLT:OFFS 0")           # Offset 0 V

    GBF_1.write("BURS:STAT ON")          # Activer le mode rafale
    GBF_1.write("BURS:NCYC 5")           # 5 cycles par rafale
    GBF_1.write("BURS:MODE TRIG")        # Mode rafale déclenchée

    GBF_1.write("TRIG:SOUR EXT")         # Déclenchement externe
    GBF_1.write("TRIG:SLOP POS")         # Front MONTANT

    GBF_1.write("OUTP ON")               # Activer la sortie

    # ---------------- CONFIGURATION POUR LE DEUXIEME GBF (GBF2) ----------------
    GBF_2.write("FUNC SQR")              # Signal carré
    GBF_2.write("FREQ 1000")             # Fréquence 1 kHz
    GBF_2.write("VOLT 2")                # Amplitude 2 Vpp
    GBF_2.write("VOLT:OFFS 0")           # Offset 0 V

    GBF_2.write("BURS:STAT ON")          # Activer le mode rafale
    GBF_2.write("BURS:NCYC 5")           # 5 cycles par rafale
    GBF_2.write("BURS:MODE TRIG")        # Mode rafale déclenchée

    GBF_2.write("TRIG:SOUR EXT")         # Déclenchement externe
    GBF_2.write("TRIG:SLOP POS")         # Front MONTANT

    GBF_2.write("OUTP ON")               # Activer la sortie

    # ---------------- SYNCHRONISATION EXTERNE ----------------
    # Le signal carré de GBF3 est utilisé comme signal de synchronisation externe pour les deux instruments.
    # Connectez les entrées de synchronisation de chaque GBF 1 et 2 à un signal extérieur, par exemple, un générateur de signaux.
    # Ce code présume que les deux instruments reçoivent ce signal de synchronisation externe.

    # Si besoin, vous pouvez ajouter un petit délai pour s'assurer que la configuration est prise en compte avant de démarrer
    time.sleep(3)

    # Démarrer la génération des signaux sur les deux instruments
    # Les deux instruments devraient être synchronisés sur le signal externe.

except Exception as e:
    print(f"Erreur lors de la configuration des instruments : {e}")
    
finally:
    # Fermer les instruments proprement
    if GBF_1 is not None:
        GBF_1.close()
        print("Connexion à GBF1 fermée.")
    if GBF_2 is not None:
        GBF_2.close()
        print("Connexion à GBF2 fermée.")
