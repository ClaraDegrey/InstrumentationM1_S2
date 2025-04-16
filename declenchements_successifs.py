import pyvisa
import time

# Initialiser le gestionnaire de ressources PyVISA
rm = pyvisa.ResourceManager()

instrument = rm.open_resource('GPIB0::5::INSTR')  

instrument.write("FUNC SIN") #Fonction sinus
instrument.write("VOLT 2")  #  2V
instrument.write("FREQ:STAR 1")  # Fréquence de départ à 1 Hz
instrument.write("FREQ:STOP 100") # Fréquence d'arrêt à 100 Hz
instrument.write("SWE:SPAC LIN")  # Espacement linéaire
instrument.write("SWE:TIME 2")    # Durée du balayage de 2 secondes
instrument.write("TRIG:SOUR IMM")  # Source de déclenchement immédiate

# Effectuer 3 déclenchements successifs avec des amplitudes différentes

amplitudes = [1.5, 2.0, 2.5]  # Amplitudes à tester
for amplitude in amplitudes:
    # Configurer l'amplitude
    instrument.write(f"VOLT {amplitude}")   # Définir l'amplitude

    # Attendre que la configuration soit appliquée
    time.sleep(0.5)  # Pause de 0.5s pour s'assurer que la configuration est prête
    
    # Déclencher le signal
    instrument.write("*TRG")  # Déclenchement via le bus
    
    # Affichage de l'amplitude et du déclenchement
    print(f"Déclenchement {amplitude} V")
    
    # Attendre quelques secondes pour que le signal soit visible
    time.sleep(2)  # Attendre 2 secondes avant de passer au suivant

# Fermer la connexion à l'instrument
instrument.close()
