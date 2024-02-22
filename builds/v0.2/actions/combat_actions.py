class CombatAction:
    """
    Base class for all combat actions, defining a common interface for executing actions.
    """
    def __init__(self, performer):
        """
        Initialize the combat action with the performer of the action.
        
        Args:
            performer (Character): The character performing the action.
        """
        self.performer = performer

    def execute(self, target):
        """
        Execute the combat action against a target. This method must be overridden by subclasses.
        
        Args:
            target (Character): The target of the action.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("Each action must implement an execute method.")

class BasicAttack(CombatAction):
    """
    A basic attack action that deals damage directly based on the performer's attack attribute.
    """
    def execute(self, target):
        if not target.dodge_attack():
            damage = max(0, self.performer.attack - target.defense)
            print(f"{self.performer.name} attacks {target.name} for {damage} damage.")
            target.take_damage(damage)
        else:
            print(f"{target.name} dodges the attack!")

class Fireball(CombatAction):
    """
    A fireball spell that consumes mana and deals significant damage to the target.
    """
    mana_cost = 30

    def execute(self, target):
        if self.performer.mana >= self.mana_cost:
            self.performer.mana -= self.mana_cost
            damage = 50  # Fixed damage for simplicity; could be based on performer's stats
            print(f"{self.performer.name} casts Fireball on {target.name}, dealing {damage} damage.")
            target.take_damage(damage)
        else:
            print(f"{self.performer.name} does not have enough mana to cast Fireball.")

class ShieldBash(CombatAction):
    """
    A shield bash that deals damage and has a chance to stun the target.
    """
    def execute(self, target):
        damage = max(0, (self.performer.attack // 2) - target.defense)
        print(f"{self.performer.name} uses Shield Bash on {target.name}, dealing {damage} damage.")
        target.take_damage(damage)
        # Example of adding a stun effect; implementation of effects would be needed
        if target.can_be_stunned():
            print(f"{target.name} is stunned by the shield bash!")

class StealthAttack(CombatAction):
    """
    A stealth attack that deals increased damage if the performer is stealthed.
    """
    def execute(self, target):
        if self.performer.is_stealthed:
            damage = self.performer.attack * 2  # Increased damage from stealth
            print(f"{self.performer.name} performs a stealth attack on {target.name}, dealing {damage} damage.")
            target.take_damage(damage)
            self.performer.is_stealthed = False  # Exiting stealth mode
        else:
            print(f"{self.performer.name} is not stealthed and performs a regular attack.")
            super().execute(target)  # Perform a basic attack if not stealthed

class FireBreath(CombatAction):
    """
    A powerful fire breath used by certain enemies, dealing massive damage to the target.
    """
    def execute(self, target):
        damage = 75  # Assuming a fixed high damage value
        print(f"{self.performer.name} unleashes a devastating fire breath on {target.name}, dealing {damage} damage.")
        target.take_damage(damage)

class PoisonBite(CombatAction):
    """
    A poison bite that deals initial damage and applies a poison effect to the target.
    """
    def execute(self, target):
        initial_damage = 20
        print(f"{self.performer.name} bites {target.name}, dealing {initial_damage} damage and applying poison.")
        target.take_damage(initial_damage)
        # Example of applying a poison effect; actual implementation would need status effect handling
        target.apply_effect("Poison", duration=3, damage_per_turn=5)
