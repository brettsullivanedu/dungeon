import random
from characters.character import (
    Character,
)  # Assuming there's a Character class imported
from actions.combat_actions import (
    BasicAttack,
    FireBreath,
    PoisonBite,
)  # Assuming action classes are imported


class Enemy(Character):
    """
    Represents an enemy character in the game.
    """

    def __init__(self, name, health, attack, defense, mana, enemy_type):
        """
        Initialize the enemy.

        Args:
            name (str): The name of the enemy.
            health (int): The health points of the enemy.
            attack (int): The attack power of the enemy.
            defense (int): The defense power of the enemy.
            mana (int): The mana points of the enemy.
            enemy_type (str): The type of the enemy.
        """
        super().__init__(name, health, attack, defense, mana)
        self.enemy_type = enemy_type

    def select_action(self, player):
        """
        Select an action for the enemy to perform.

        Args:
            player (Character): The player character.

        Returns:
            CombatAction: The selected action.
        """
        # Basic action selection logic; can be overridden by subclasses for unique behaviors
        return BasicAttack(self)

    def dodge_attack(self):
        # Simple dodge logic based on a dodge chance
        dodge_chance = 0  # Default dodge chance, could be overridden in subclasses
        if random.randint(1, 100) <= dodge_chance:
            return True  # Attack is dodged
        return False


class Goblin(Enemy):
    """
    Represents a Goblin enemy.
    """

    def __init__(self):
        """
        Initialize the Goblin enemy.
        """
        super().__init__("Goblin", 50, 15, 5, 0, "Goblin")
        self.dodge_chance = 30


class Ogre(Enemy):
    """
    Represents an Ogre enemy.
    """

    def __init__(self):
        """
        Initialize the Ogre enemy.
        """
        super().__init__("Ogre", 100, 20, 10, 0, "Ogre")
        self.dodge_chance = 20

    def select_action(self, player):
        """
        Select an action for the Ogre to perform.

        Args:
            player (Character): The player character.

        Returns:
            CombatAction: The selected action.
        """
        # Example of Ogre using a Poison Bite under certain conditions
        if self.health < 50 and self.is_ability_ready("Poison Bite"):
            self.use_ability("Poison Bite", 5)  # Cooldown of 5 turns
            return PoisonBite(self)
        else:
            return BasicAttack(self)


class Dragon(Enemy):
    """
    Represents a Dragon enemy.
    """

    def __init__(self):
        """
        Initialize the Dragon enemy.
        """
        super().__init__("Dragon", 200, 30, 20, 0, "Dragon")
        self.dodge_chance = 10

    def select_action(self, player):
        """
        Select an action for the Dragon to perform.

        Args:
            player (Character): The player character.

        Returns:
            CombatAction: The selected action.
        """
        # Example of Dragon choosing to use Fire Breath
        if self.is_ability_ready("Fire Breath"):
            self.use_ability("Fire Breath", 3)  # Cooldown of 3 turns
            return FireBreath(self)
        else:
            return BasicAttack(self)
