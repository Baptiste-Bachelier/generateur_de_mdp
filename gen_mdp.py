# =========================================================
# génération de Mots de passe
# =========================================================

# bibliothèque importé
import random as rd 
import string 

# variables
letters = string.ascii_letters
numbers = string.digits
ponctuation = string.punctuation
force_invoc = False

# fonction génération de mot de passe
def f_mdp(exit_mdp=None, longeur=12):
    global letters, numbers, ponctuation, force_invoc
    # création de la liste de caractère 
    list_character = [letters, numbers, ponctuation]
    while None in list_character:
        list_character.remove(None)
        
    if list_character == []:
        mdp="choisissez les caractères"
    else:                            
        all_character = "".join(list_character)
            
        list_character = []       
        for j in all_character:
            list_character.append(j)        
        # max longeur mdp 
        if int(longeur) > 99:
            longeur = 99   
        # gen mdp 
        mdp = ""
        if force_invoc == True and int(longeur) >= 3:
            mdp_list_char = [rd.choice(numbers), rd.choice(letters), rd.choice(ponctuation)]
            longeur = int(longeur) - 3
        else:
            mdp_list_char = []            
        for k in range(int(longeur)):
            k = rd.choice(list_character)
            mdp += k   
        for char in mdp:
            mdp_list_char.append(char)
        mdp= "".join(rd.sample(mdp_list_char, len(mdp_list_char)))              
    return  exit_mdp.set(mdp) 

def select_letters():
    global letters
    if letters == None:
        letters = string.ascii_letters
    else:
        letters = None   
    return letters

def select_numbers():
    global numbers
    if numbers == None:
        numbers = string.digits
    else:
        numbers = None  
    return numbers
    
def select_ponctuation():
    global ponctuation
    if ponctuation == None:
        ponctuation = string.punctuation
    else:
        ponctuation = None
    return ponctuation     

def no_none(entry, button, verif= ""):
    if entry != verif:
        button.config(state="normal")
    else:
        button.config(state="disabled")

def invoc_order():
    global force_invoc          
    if force_invoc == False:
        force_invoc = True
    else:
        force_invoc = False
    return force_invoc        