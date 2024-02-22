# setup_game.py
from characters.player import Player
from gameengine import GameEngine
from states.MenuState import MenuState
from states.DungeonState import DungeonState
from states.CombatState import CombatState

def setup_game(screen):
    game_engine = GameEngine(screen)

    # Create a default or placeholder player object
    default_player = Player(name='Test', health=100, attack=10, defense=10, mana=10, player_type='Warrior') 

    # Create and register states
    menu_state = MenuState(game_engine)
    dungeon_state = DungeonState(game_engine, default_player)
    combat_state = CombatState(game_engine, default_player)

    game_engine.register_state('menu', menu_state)
    game_engine.register_state('dungeon', dungeon_state)
    game_engine.register_state('combat', combat_state)

    # Initially set to menu state
    game_engine.change_state('menu')

    return game_engine
