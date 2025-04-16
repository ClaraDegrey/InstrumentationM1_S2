import pyvisa
import time

# Initialiser PyVISA Resource Manager
rm = pyvisa.ResourceManager()

# Connexion à l'instrument via GPIB ou série
instrument = rm.open_resource('GPIB0::5::INSTR')  # Modifiez selon l'adresse de votre instrument
print("Connecté à l'instrument")

# Activer le Service Request (SRQ)
instrument.write('SRQ:ENABLE')  # Activer les demandes de service

# Configurer le balayage de fréquence (exemple)
instrument.write('FREQuency:STARt 1000')  # Fréquence de départ
instrument.write('FREQuency:STOP 4000')   # Fréquence de fin
instrument.write('SWEep:TIME 2')          # Durée du balayage
instrument.write('SWEep:SPACing LINear')  # Espacement linéaire

# Configurer la source de déclenchement externe si nécessaire
instrument.write('TRIGger:SOURce EXTernal')  # Utilisation d'un signal externe pour le déclenchement
instrument.write('TRIGger:SLOPe POSitive')  # Déclenchement sur le front montant du signal externe

# Lancer le balayage (exécution de la tâche)
instrument.write('SWEep:STATE ON')  # Activer le balayage

# Vérifier le Status Register pour savoir si le balayage est terminé
# Le registre de statut (par exemple, "STB" pour Status Byte) peut être utilisé pour vérifier la fin du balayage.
status_register = instrument.query('STB?')
print(f"Status Register : {status_register}")

# Utilisation d'un Service Request (SRQ) pour recevoir une notification quand l'opération est terminée
instrument.write('STATus:PRESet')  # Réinitialiser les registres de statut
instrument.write('STATus:MEAS:ENABle 1')  # Activer les événements de mesure pour le Service Request
instrument.write('STATus:OPER:ENABle 1')  # Activer les événements opérationnels pour SRQ

# Vérifier si l'instrument envoie un Service Request
srq_status = instrument.query('SRQ?')
if srq_status == '1':
    print("Service Request reçu : tâche terminée.")
else:
    print("Service Request non reçu.")

# Attente que la tâche soit terminée
while True:
    srq_status = instrument.query('SRQ?')
    if srq_status == '1':
        print("Tâche terminée, le balayage a été effectué.")
        break  # Terminer la boucle quand la tâche est terminée
    else:
        print("En attente de la fin du balayage...")
        time.sleep(1)  # Attendre avant de vérifier à nouveau

# Fermer la connexion à l'instrument
instrument.close()
