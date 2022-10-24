# importation des libraries python pour le projet
import logging
import sys
import argparse
import json
import jmespath
import requests

# Configuration du Logger

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pokepi.pika")


# Ajout des argument de recuperation des données, acces au log debug


def recup_parametres(list_args):
    logger.debug("list_args : %s", list_args)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-P",
        "--pokemon",
        type=str,
        action="store",
        dest="pokemon",
        required=True,
    )
    parser.add_argument("--save-output", type=str, action="store", dest="save_moves")
    return parser.parse_args(list_args)


# Recupere avec l'API le poke choisit selon "recup_parametre"


def get_data(args):

    # Creation d'une variable Args.pokemon et l'afficher en log

    print(args.pokemon)
    f"args {args.pokemon}"
    #print(f"https://pokeapi.co/api/v2/pokemon/$pokemon{args.pokemon}")

    # Verification connection API est disponible et recupere les données du pokemon choisit

    try:
        poke = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{args.pokemon}", timeout=10
        )
        poke.status_code
    except:
        logger.error("Echec de l'API")
        sys.exit()
    return poke


# Formate le tout dans un dictionnaire en python pur et avec jmespath


def get_name(data_json):
    #logger.info("Recuperation des moves du pokemon choisi en python")
    move_name = []
    for data in data_json["abilities"]:
        move_name.append(data["ability"]["name"])
    move_name.sort()
    return move_name


def get_name_jmespath(data_json):
    #logger.info("Recuperation des moves du pokemon choisi en jmespath")
    moves_name = []
    for ability in data_json["abilities"]:
        moves_name.append(jmespath.search("ability.name", ability))
    moves_name.sort()
    return moves_name


# Verification de l'existance du pokemon


def poke_exist(pokemon):
    if not pokemon:
        logger.error("Le pokemon pokemon-inexistant est introuvable")
        sys.exit()


# Fonction Maitre pour afficher chaque methode


def main(args):
    pokemon = get_data(args)
    poke_json = json.loads(pokemon.text)
    json.dumps(poke_json)
    logger.info("Avec Jmespath : %s", get_name_jmespath(poke_json))
    logger.info("En Python pur : %s", get_name(poke_json))
    with open("save_move_python.json", "w") as save_move:
        json.dump(get_name(poke_json), save_move)
    with open("save_move_jmespath.json", "w") as save_move:
        json.dump(get_name_jmespath(poke_json), save_move)


if __name__ == "__main__":
    logger.info("debut du traitement")
    args = recup_parametres(sys.argv[1:])
    main(args)
    print(sys.argv[1:])
