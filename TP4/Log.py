# import logging
import logging

class Log(): # declaration de la classe
    def __init__(self): #self est le premier argument de la classe
        logging.basicConfig(f='l.log', format='%(f)s: %(msg)s', lvl=logging.DEBUG) # on utulise DEBUG pour obtenir des information detailles. C'est utile quand on diagnostique un probleme

    def Erreur(self):
        logging.warning("message d'alerte") # on utulise warning pour dire que quelque chose d'innatendue a eu lieu
    
    
    def Information(self,messages):
        logging.info(str(messages)) # on utilise info pour dire que tous c'est passé comme prevu
        print(str(messages))

    def Sauvegarder(self,auteur,messages):
        logging.debug(str(auteur)+": "+str(messages))
