# PokePi
Exercice python pour les nouveaux arrivant chez Pôle Emploi  
Contient le fichier python " pokepi.py " qui permet d'executer le programme et " test_pokepi.py " qui sont les test unitaire
Le principe du script est de prendre l'api " https://pokeapi.co/ " choisir un pokemon verifié qu'il existe, verifié que l'Api n'as aucun probleme  
Extraire ces "moves" de 2 facon differentes une en python pur et la deuxieme via jmespath  
Formater le tout dans un fichier " save_move_python.json " / " save_move_jmespath.json  quand il as une sauvegarde avec l'argument " --save-output "

# Pour Executer le script  
Attention il faut Python 3.10
```
python3 pokepi.py --pokemon pikachu --save-output save_moves_python.json
```
# Sortie dans save_move_python.json et save_move_jmespath.json  
```
["lightning-rod", "static"]
```
