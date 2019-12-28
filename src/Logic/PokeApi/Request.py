import requests
import Exceptions.py as ex

class PokemonRequests:
  def __init__(this, pokename):
    this.pokename = Pokename

  url = 'https://pokeapi.co/api/v2/pokemon/'
  statusCode

  def GetPokemon() :
    request = requests.get(this.url + this.pokechoice)
    statusCode = request.status_code
    return = request.text
