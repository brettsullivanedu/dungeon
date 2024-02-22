from dungeon.rooms.base_room import Room


class TrapRoom(Room):
    def interact(self, player):
        if not self.visited:
            print("Ouch! It's a trap! You take damage.")
            # Logic to apply damage to the player
            self.visited = True
        else:
            print("You see remnants of a trap you've already triggered.")