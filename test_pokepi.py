# Import des Librairie de Test
import pytest
import argparse
from unittest.mock import patch
from unittest import mock
from pokepi import get_data, get_name, poke_exist, recup_parametres

@patch('requests.get')
def test_recup_parametres(poke):
    poke = ['-P', 'pikachu', '--save-output', 'moves.txt']
    expected_result = argparse.Namespace(pokemon='pikachu', save_moves='moves.txt')

    # exécution de la fonction avec les données de test
    result = recup_parametres(poke)
    
    # vérification du résultat
    assert result == expected_result

def test_get_data():
    with mock.patch("requests.get") as mock_get:
        
        #Simuler un succés API
        mock_ping = mock.Mock()
        mock_ping.status_code = 200
        mock_ping.json.return_value = {"name": "pikachu", "moves": []}
        mock_get.return_value = mock_ping
        
        #Appel de la fonction Get_Data
        result = get_data(mock.Mock(pokemon="pikachu"))
        assert result == {"name": "pikachu", "moves": []}
        
        #Simuler l'appel requests avec les bon args
        mock_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/pikachu', timeout=10)
        
        #Simuler une erreur API
        mock_get.reset_mock()
        mock_ping.status_code = 404
        mock_get.return_value = mock_ping
        
        result = get_data(mock.Mock(pokemon="pikachu"))
        assert result is None
        
        #Simuler l'appel requests avec les bon args
        mock_get.assert_called_once_with('https://pokeapi.co/api/v2/pokemon/pikachu', timeout=10)
        
        #Simuler une Exception
        mock_get.reset_mock()
        mock_get.side_effect = Exception("erreur")
        

def test_get_name():
    
    #Données de Test
    moves = {'moves': [{'move': {'name': 'move1'}}, {'move': {'name': 'move2'}}, {'move': {'name': 'move3'}}]}
    moves_clean = ['move1', 'move2', 'move3']
    
    result = get_name(moves)
    assert result == moves_clean

def test_poke_exist():
    
    #Test avec un pokemon existant
    pokemon = {"name": "pikachu", "type": "electric"}
    assert poke_exist(pokemon) is None
    
    #Test avec un pokemon inexistant 
    with pytest.raises(SystemExit):
        poke_exist(None)


