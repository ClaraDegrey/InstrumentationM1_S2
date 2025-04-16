# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 08:42:02 2025
@author: cdegrey
"""

import pyvisa
import time

rm = pyvisa.ResourceManager() # Initialiser PyVISA Resource Manager

print("Instruments disponibles :", rm.list_resources()) # Lister les instruments connectés

instrument = None  # Pour la connexion à l'instrument

# Connexion à l'oscilloscope via TCP/IP
try:
    instrument = rm.open_resource('TCPIP0::218B-01::inst0::INSTR')
    print("Connecté à l'instrument")

    # Définir le délai d'attente si nécessaire
    instrument.timeout = 5000  # en millisecondes

    # Envoi d'une commande SCPI pour lire la tension crête-à-crête sur CHAN1
    vpp = instrument.query("MEAS:VPP? CHAN1")
    print(f"Tension crête-à-crête sur CHAN1 : {vpp.strip()} V")

except Exception as e:
    print(f"Erreur lors de la connexion ou de la communication : {e}")

finally:
    if instrument is not None:
        instrument.close()
        print("Connexion à l'instrument fermée.")
