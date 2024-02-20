from characters.character import Character  # Assuming there's a Character class imported
from actions.combat_actions import BasicAttack, Fireball, ShieldBash, StealthAttack  # Assuming action classes are imported

class Player(Character):
    """
    Represents a player character in the game.
    """

    def __init__(self, name, health, attack, defense, mana, player_type):
        """
        Initialize the player character.

        Args:
            name (str): The name of the player character.
            health (int): The health points of the player character.
            attack (int): The attack power of the player character.
            defense (int): The defense power of the player character.
            mana (int): The mana points of the player character.
            player_type (str): The type of the player character.
        """
        super().__init__(name, health, attack, defense, mana)
        self.player_type = player_type
        self.abilities_cooldown = {}

    def reduce_cooldowns(self):
        """
        Reduce cooldowns of player character's abilities.
        """
        for ability in self.abilities_cooldown:
            if self.abilities_cooldown[ability] > 0:
                self.abilities_cooldown[ability] -= 1
        self.update_status_effects()  # Update status effects at the start of each turn

    def is_ability_ready(self, ability_name):
        """
        Check if an ability is ready to be used.

        Args:
            ability_name (str): The name of the ability.

        Returns:
            bool: True if the ability is ready, False otherwise.
        """
        return self.abilities_cooldown.get(ability_name, 0) == 0

    def use_ability(self, ability_name, cooldown):
        """
        Use an ability of the player character.

        Args:
            ability_name (str): The name of the ability.
            cooldown (int): The cooldown of the ability.

        Returns:
            bool: True if the ability was successfully used, False otherwise.
        """
        if self.is_ability_ready(ability_name):
            self.abilities_cooldown[ability_name] = cooldown
            return True
        else:
            print(f"{ability_name} is not ready yet.")
            return False


class Warrior(Player):
    """
    Represents a Warrior player character.
    """

    def __init__(self, name):
        """
        Initialize the Warrior player character.
        """
        super().__init__(name, 150, 20, 10, 0, "Warrior")  # Assuming Warrior does not use mana

    def shield_bash(self, target):
        """
        Perform a shield bash action.

        Args:
            target (Character): The target of the shield bash.
        """
        if self.use_ability("Shield Bash", 3):  # Cooldown of 3 turns
            ShieldBash(self).execute(target)


class Mage(Player):
    """
    Represents a Mage player character.
    """

    def __init__(self, name):
        """
        Initialize the Mage player character.
        """
        super().__init__(name, 100, 30, 5, 100, "Mage")  # Starting with 100 mana

    def cast_fireball(self, target):
        """
        Cast a fireball spell.

        Args:
            target (Character): The target of the fireball spell.
        """
        if self.use_mana(Fireball.mana_cost) and self.use_ability("Fireball", 2):  # Cooldown of 2 turns
            Fireball(self).execute(target)
        else:
            print(f"Not enough mana or ability is on cooldown.")


class Rogue(Player):
    """
    Represents a Rogue player character.
    """

    def __init__(self, name):
        """
        Initialize the Rogue player character.
        """
        super().__init__(name, 120, 25, 8, 0, "Rogue")  # Assuming Rogue does not use mana
        self.is_stealthed = False

    def stealth_attack(self, target):
        """
        Perform a stealth attack.

        Args:
            target (Character): The target of the stealth attack.
        """
        if not self.is_stealthed:
            print(f"{self.name} is not in stealth.")
            return

        if self.use_ability("Stealth Attack", 1):  # Cooldown of 1 turn
            StealthAttack(self).execute(target)
            self.is_stealthed = False  # Exiting stealth mode after the attack

    def enter_stealth(self):
        """
        Enter stealth mode.
        """
        if self.use_ability("Enter Stealth", 3):  # Cooldown of 3 turns to re-enter stealth
            self.is_stealthed = True
            print(f"{self.name} enters stealth mode.")

    def collect_treasure(self):
        """Collect treasure found in a TreasureRoom."""
        print(f"{self._name} collects treasure!")
        # Add treasure to player's inventory or increase player's stats
    
    def trigger_trap(self):
        """Trigger a trap in a TrapRoom."""
        trap_damage = 10  # Example damage value
        self.take_damage(trap_damage)
        print(f"{self._name} triggers a trap and takes {trap_damage} damage!")
    
    def solve_puzzle(self):
        """Attempt to solve a puzzle in a PuzzleRoom."""
        # This could be simplified to a random chance or based on player's attributes
        puzzle_solved = True  # Simplification for example purposes
        if puzzle_solved:
            print(f"{self._name} solves the puzzle and discovers a hidden treasure or key!")
            self.collect_treasure()  # Assuming solving the puzzle yields treasure
            return True
        else:
            print(f"{self._name} fails to solve the puzzle.")
            return False
    
    def fight_enemy(self, is_boss=False):
        """Fight an enemy in an EnemyRoom."""
        # Simplified combat logic; in a real game, this would be more complex
        if is_boss:
            print(f"{self._name} bravely fights the boss!")
        else:
            print(f"{self._name} engages in combat with an enemy.")
        
        # Determine outcome of the fight (simplified for example)
        enemy_defeated = True  # Simplification for example purposes
        if enemy_defeated:
            print(f"{self._name} defeats the enemy!")
            return True
        else:
            print(f"{self._name} is defeated by the enemy.")
            self.take_damage(20)  # Example damage if defeated
            return False
