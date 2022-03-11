import commandes
import bot
import pickle

config_dictionary = [commandes.Joueur object at 0x0000022E8B84EBB0]
 
# Step 2
with open('classement.txt', 'wb') as config_dictionary_file:
 
  # Step 3
  pickle.dump(config_dictionary, config_dictionary_file)