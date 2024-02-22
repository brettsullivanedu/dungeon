from dungeon.rooms.base_room import Room


class TreasureRoom(Room):
    def interact(self, player):
        if not self.visited:
            print("You've discovered treasure! Your wealth grows.")
            # Logic to add treasure to player's inventory
            self.visited = True
        else:
            print("An empty room. You've already taken the treasure.")