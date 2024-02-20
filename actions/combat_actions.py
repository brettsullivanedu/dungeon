class CombatAction:
    """
    Base class for all combat actions.
    """

    def __init__(self, performer):
        """
        Initialize the combat action.

        Args:
            performer (Character): The character performing the action.
        """
        self.performer = performer

    def execute(self, target):
        """
        Execute the combat action. Must be implemented by subclasses.

        Args:
            target (Character): The target of the action.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError("Each action must implement an execute method.")

class BasicAttack:
    def __init__(self, performer):
        self.performer = performer

    def execute(self, target):
        # Check if the target dodges the attack
        if hasattr(target, 'dodge_attack') and target.dodge_attack():
            print(f"{target.name} dodges the attack from {self.performer.name}!")
            return False  # Attack was dodged

        # Proceed with the attack as normal if not dodged
        damage = self.performer.attack - target.defense
        if damage > 0:
            print(f"{self.performer.name} attacks {target.name} for {damage} damage.")
            target.take_damage(damage)
            return True
        else:
            print(f"{self.performer.name}'s attack is too weak to damage {target.name}.")
            return False



class Fireball(CombatAction):
    """
    Represents a fireball spell action.
    """

    mana_cost = 30  # Define mana cost for the ability

    def execute(self, target):
        """
        Execute the fireball spell action.

        Args:
            target (Character): The target of the spell.
        """
        try:
            if self.performer.use_mana(self.mana_cost):
                damage = self.performer.attack * 2
                print(f"{self.performer.name} casts Fireball on {target.name}, dealing {damage} damage.")
                target.take_damage(damage)
            else:
                print(f"{self.performer.name} does not have enough mana for Fireball.")
        except AttributeError:
            print(f"Error: {self.performer.name} does not have a 'use_mana' method.")


class ShieldBash(CombatAction):
    """
    Represents a shield bash action.
    """

    def execute(self, target):
        """
        Execute the shield bash action.

        Args:
            target (Character): The target of the bash.
        """
        damage = self.performer.attack // 2
        print(f"{self.performer.name} uses Shield Bash on {target.name}, dealing {damage} damage.")
        target.take_damage(damage)
        # Example effect: target is stunned and skips next turn
        target.apply_status_effect("Stunned", 1)


class StealthAttack(CombatAction):
    """
    Represents a stealth attack action.
    """

    def execute(self, target):
        """
        Execute the stealth attack action.

        Args:
            target (Character): The target of the attack.
        """
        if hasattr(self.performer, "is_stealthed"):
            if self.performer.is_stealthed:
                damage = self.performer.attack * 3
                print(f"{self.performer.name} performs a stealth attack on {target.name}, dealing {damage} damage.")
                target.take_damage(damage)
                self.performer.is_stealthed = False
            else:
                print(f"{self.performer.name} is not stealthed and cannot perform a stealth attack.")
        else:
            print(f"Error: {self.performer.name} does not have 'is_stealthed' attribute.")


class FireBreath(CombatAction):
    """
    Represents a fire breath action.
    """

    def execute(self, target):
        """
        Execute the fire breath action.

        Args:
            target (Character): The target of the breath.
        """
        damage = self.performer.attack * 3  # Fire Breath is very powerful
        print(f"{self.performer.name} unleashes a devastating fire breath on {target.name}, dealing {damage} damage.")
        target.take_damage(damage)
        target.apply_status_effect("Burned", 3, lambda target: target.take_damage(5))


class PoisonBite(CombatAction):
    """
    Represents a poison bite action.
    """

    def execute(self, target):
        """
        Execute the poison bite action.

        Args:
            target (Character): The target of the bite.
        """
        initial_damage = self.performer.attack
        poison_damage = 5
        poison_duration = 3
        print(f"{self.performer.name} bites {target.name}, dealing {initial_damage} damage and poisoning them.")
        target.take_damage(initial_damage)
        target.apply_status_effect("Poisoned", poison_duration, lambda target: target.take_damage(poison_damage))
