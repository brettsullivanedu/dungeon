from dungeon.rooms.base_room import Room


class EmptyRoom(Room):
    def interact(self, player):
        if not self.visited:
            print("An empty room appears! Prepare for battle.")
            # Logic for initiating combat
            self.visited = True
        else:
            print("The defeated enemy lies before you. The room is now safe.")