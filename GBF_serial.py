import pyvisa

rm = pyvisa.ResourceManager() # Initialiser PyVISA Resource Manager

print("Instruments disponibles :", rm.list_resources()) # Lister les instruments connectés

# Connexion à l'instrument via port série
try:
    instrument = rm.open_resource(
        'ASRL1::INSTR',           # L'adresse du port série (modifiez selon votre système)
        baud_rate=9600,           # Vitesse de communication
        data_bits=8,              # Nombre de bits de données
        parity=pyvisa.constants.Parity.none,  # Parité (aucune ici)
        stop_bits=pyvisa.constants.StopBits.one,  # Nombre de bits de stop
        read_termination='\n'     # Caractère de fin de lecture
    )
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
