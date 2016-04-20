""" this object is a prototype room """

class Room:
    """ base class for rooms
    """

    def __init__(self, desc, whatshere, dirdict):
        self.description = desc
        self.roomcontents = whatshere
        self.directionsoutdict = dirdict

    def move(self, direction):
        """ function returns new room based on direction stored in directionsoutdict"""
        return self.directionsoutdict[direction]

    def describeroom(self):
        print(self.description)

    def exitsfromroom(self):
        print("Exits from this room are: ")
        for x in self.directionsoutdict:
            print(x)

""" main below, will likely go to it's own file in future, but for now this is the temp main """

def start():
    print("Welcome to Fun House, where anything could happen...")
    room1 = Room("You are in an empty room, painted in a pleasant indigo color.", [], {"n":"room2"})
    roomloop(room1)

def roomloop(currentroom):
    currentroom.describeroom()
    currentroom.exitsfromroom()
    command = input("What would you like to do?")
    if command in currentroom.directionsoutdict:
        currentroom = room1.directionsoutdict[command]
        print(currentroom)

if __name__ == '__main__':
    start()

