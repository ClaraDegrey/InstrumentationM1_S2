# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 08:42:02 2025

@author: cdegrey
"""
import pyvisa

rm = pyvisa.ResourceManager() # Initialiser PyVISA Resource Manager

print("Instruments disponibles :", rm.list_resources()) # Lister les instruments connectés

# Connexion à l'instrument via port série
try:
    instrument = rm.open_resource("TCPIP0::218B-02::INSTR")
    print("Connecté à l'instrument via port série.")
    
    # Interrogation de la configuration actuelle de l'instrument
    try:
        response = instrument.query("APPLy?\n")  # Commande SCPI pour obtenir la configuration
        print("Configuration actuelle :", response)
    except Exception as e:
        print("Erreur lors de la lecture de la configuration :", e)
    
except Exception as e:
    print(f"Erreur lors de la connexion à l'instrument : {e}")
    
finally:
    # Fermer la connexion proprement
    if 'instrument' in locals():
        instrument.close()
        print("Connexion fermée.")