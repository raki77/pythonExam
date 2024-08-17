class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}

    def connect(self, direction, room):
        self.connections[direction] = room

    def get_room_in_direction(self, direction):
        return self.connections.get(direction)

    def __str__(self):
        return f"{self.name}\n{self.description}\nExits: {', '.join(self.connections.keys())}"


class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room

    def move(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room:
            self.current_room = next_room
            return True
        else:
            return False


class Game:
    def __init__(self):
        self.rooms = self.create_rooms()
        self.player = Player(self.rooms['entrance'])

    def create_rooms(self):
        # 방 생성
        entrance = Room("Entrance", "You are at the entrance of the dungeon.")
        hall = Room("Hall", "A long hall with doors on either side.")
        kitchen = Room("Kitchen", "A kitchen with a lingering smell of food.")
        library = Room("Library", "A room full of dusty books.")

        # 방 연결
        entrance.connect('north', hall)
        hall.connect('south', entrance)
        hall.connect('west', kitchen)
        hall.connect('east', library)
        kitchen.connect('east', hall)
        library.connect('west', hall)

        return {
            'entrance': entrance,
            'hall': hall,
            'kitchen': kitchen,
            'library': library
        }

    def play(self):
        print("Welcome to the MUD game!")
        while True:
            print("\n" + str(self.player.current_room))
            command = input("\n> ").strip().lower()
            if command in ['north', 'south', 'east', 'west']:
                if self.player.move(command):
                    print(f"You move {command}.")
                else:
                    print("You can't go that way.")
            elif command == 'quit':
                print("Thanks for playing!")
                break
            else:
                print("Invalid command. Try 'north', 'south', 'east', 'west', or 'quit'.")


if __name__ == "__main__":
    game = Game()
    game.play()