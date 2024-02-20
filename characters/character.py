class Character:
    """
    Represents a character in the game.
    """

    def __init__(self, name, health, attack, defense, mana=100):  # Default mana added
        """
        Initialize the character.

        Args:
            name (str): The name of the character.
            health (int): The health points of the character.
            attack (int): The attack power of the character.
            defense (int): The defense power of the character.
            mana (int, optional): The mana points of the character. Defaults to 100.
        """
        self._name = name
        self._health = health
        self._attack = attack
        self._defense = defense
        self._mana = mana
        self.status_effects = {}  # Track active status effects

    @property
    def name(self):
        """
        Get the name of the character.
        """
        return self._name

    @property
    def health(self):
        """
        Get the current health points of the character.
        """
        return self._health

    @property
    def attack(self):
        """
        Get the attack power of the character.
        """
        return self._attack

    def apply_status_effect(self, effect_name, duration, effect=None):
        """
        Apply a status effect to the character.

        Args:
            effect_name (str): The name of the status effect.
            duration (int): The duration of the effect.
            effect (function, optional): The effect function to apply. Defaults to None.
        """
        self.status_effects[effect_name] = {"duration": duration, "effect": effect}

    def update_status_effects(self):
        """
        Update the status effects of the character.
        """
        to_remove = []
        for effect_name, details in self.status_effects.items():
            # Apply effect (e.g., take damage for "Poison")
            if details["effect"]:
                details["effect"](self)

            # Reduce duration
            details["duration"] -= 1
            if details["duration"] <= 0:
                to_remove.append(effect_name)

        # Remove expired effects
        for effect_name in to_remove:
            del self.status_effects[effect_name]
            print(f"{self._name} is no longer affected by {effect_name}.")

    def take_damage(self, damage):
        """
        Inflict damage on the character.

        Args:
            damage (int): The amount of damage to inflict.

        Returns:
            int: The reduced damage after considering defense.
        """
        reduced_damage = max(0, damage - self._defense)
        self._health -= reduced_damage
        return reduced_damage

    def is_alive(self):
        """
        Check if the character is alive.

        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self._health > 0

    def use_mana(self, amount):
        """
        Consume mana points from the character.

        Args:
            amount (int): The amount of mana to consume.

        Returns:
            bool: True if there is enough mana and it's successfully consumed, False otherwise.
        """
        if self._mana >= amount:
            self._mana -= amount
            return True
        return False

    def restore_mana(self, amount):
        """
        Restore mana points to the character.

        Args:
            amount (int): The amount of mana to restore.
        """
        self._mana += amount
