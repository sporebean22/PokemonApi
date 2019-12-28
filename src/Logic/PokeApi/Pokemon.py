#____________________________________________________________________________________#

class Pokemon:
  """
  Required Attributes to Instantiate a Pokemon.
  """
  def __init__
    """
    All Attributes that make up a Pokemon need to be 
    """
    (
      self, abilities, base_experience, forms, game_indicies, 
      height, held_items, id, is_default, location_area_encounters,
      moves, name, order, species, sprites, stats, types, weight
    ):
      self.abilities = Abilities
      self.base_experience = Base_Experience
      self.forms = Forms
      self.game_indicies = Game_Indicies
      self.height = Height
      self.held_items = Held_Items
      self.id = ID
      self.is_default = Is_Default
      self.location_area_encounters = Location_Area_Encounters
      self.moves = Moves
      self.name = Name
      self.order = Order
      self.species = Species
      self.sprites = Sprites
      self.stats = Stats
      self.types = Types
      self.weight = Weight
#____________________________________________________________________________________#

class Ability:
  """
  Propeties and fields of the Pokemons' primary Ability.
  """
  def __init__(self, ability, is_hidden, slot)
  """
  Definition of a Pokemons' primary ability.
  """
    self.ability = Ability
    self.is_hidden = is_hidden
    self.slot = Slot

#____________________________________________________________________________________#

class Ability2(Ability):
  """
  Propeties and fields of the Pokemons' secondary Ability.
  """
  def __init__(self, name, url)
    """
    Definition of a Pokemons' secondary ability.
    """
    self.name = Name
    self.url = Url

#____________________________________________________________________________________#

class Form:
  """

  """
  def __init__(self, name, url)
    """
    Definition of the description of a Pokemons' form.
    """
    self.name = Name
    self.url = Url

#____________________________________________________________________________________#

