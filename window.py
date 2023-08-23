# =========================================================
# affiche génération de Mots de passe
# =========================================================

# bibliothèque importé
import tkinter as tk 
from gen_mdp import *

# paramètre fenètre
# init 
window = tk.Tk()
# geometry
window.geometry("500x550")
window.minsize(500, 550)
window.maxsize(500, 550)
# title & icon
window.title('gen_MDP')

# recup du mdp
space = tk.Label(window, text="")
space.pack(side="top", pady=10)
mdp_text2 = tk.Label(window, text="Mot de passe", font=("colibri", 30))
mdp_text2.pack(side="top", pady=20)
mdp_text = tk.StringVar()
mdp_entry = tk.Entry(window,
                     font=('colibri', 30),
                     textvariable=mdp_text
                     )
mdp_entry.pack(side='top')
# objet de la fenètre
window_param = tk.Frame(window, bd=1, relief="sunken")
# case lettres
space2 = tk.Label(window, text="")
space2.pack(side="top", pady=15)
mdp_param_letter = tk.Checkbutton(window_param, text="Lettres", font=('colibri', 12), command=select_letters)
mdp_param_letter.grid(column=0, row=0, sticky="w", pady=5)
mdp_param_letter.select()
# case nombres
mdp_param_numbers = tk.Checkbutton(window_param, text="Nombres", font=('colibri', 12), command=select_numbers)
mdp_param_numbers.grid(column=0, row=1, sticky="w", pady=5)
mdp_param_numbers.select()
# case ponctuation
mdp_param_ponctuation = tk.Checkbutton(window_param, text="Ponctuations", font=('colibri', 12), command=select_ponctuation)
mdp_param_ponctuation.grid(column=0, row=2, sticky="w", pady=5)
mdp_param_ponctuation.select()
# longuer du mdp
text_longeur_mdp = tk.Label(window_param, text="Longeur du MDP:", font=('colibri', 12))
text_longeur_mdp.grid(column=1, row=0, sticky="e", pady=5)
entry_longeur_mdp = tk.Entry(window_param, textvariable="", font=('colibri', 12), width=3)
entry_longeur_mdp.grid(column=2, row=0, sticky="e", pady=5, padx= 1)
entry_longeur_mdp.bind("<KeyRelease>", lambda event : no_none(entry_longeur_mdp.get(), gen_mdp_button))
# forcer l invocation
force_invoc_char = tk.Checkbutton(window_param, text="forcer la présence", font=("colibri", 12), command=invoc_order)
force_invoc_char.grid(column=0, row=3)
# affichage de window_param
window_param.pack(side="top")
# button générer
gen_mdp_button = tk.Button(window, text="Générer", 
                           font=("colibri", 30), 
                           width=12, 
                           command=lambda: f_mdp(mdp_text, entry_longeur_mdp.get()), 
                           state="disabled")
gen_mdp_button.pack(side="top", pady= 15)
# affichage 
window.mainloop()



