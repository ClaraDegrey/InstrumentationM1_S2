import pyvisa

# Créer le gestionnaire de ressources VISA
rm = pyvisa.ResourceManager()

# Lister les instruments disponibles
print("Instruments disponibles :", rm.list_resources())

try:
    # Se connecter à l'instrument (adapter l'adresse si besoin)
    inst = rm.open_resource('GPIB0::1::INSTR')
    print("Connecté à l'instrument :", inst.query("*IDN?").strip())

    # Configurer un signal carré à 100 Hz, 4 Vpp, offset 1 V
    inst.write("APPL:SQU 100,4,1")

    # Lire et afficher la configuration actuelle
    config = inst.query("APPL?")
    print("Configuration actuelle :", config.strip())

    # Fermer la connexion
    inst.close()

except Exception as e:
    print("Erreur :", e)
