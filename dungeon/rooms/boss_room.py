from dungeon.rooms.base_room import Room


class BossRoom(Room):
    def interact(self, player):
        if not self.visited:
            print("The final challenge! The boss awaits.")
            # Logic for boss fight
            self.visited = True
        else:
            print("You've conquered the boss. The path forward is clear.")