def create_game():
    current_location = "Beach"
    energy = 5
    inventory = []

    return current_location, energy, inventory


def collect_item(inventory, item):
    if item not in inventory:
        inventory.append(item)
        return True
    else:
        return False
def move_player(current_location, destination, energy, inventory):

    destination = destination.strip().lower()

    valid_moves = {
        "Beach": ["jungle"],
        "Jungle": ["beach", "cave"],
        "Cave": ["jungle", "old bridge"],
        "Old Bridge": ["cave", "lighthouse"],
        "Lighthouse": ["old bridge"]
    }

    if destination not in valid_moves[current_location]:
        return current_location, energy, False

    if current_location == "Cave" and destination == "old bridge":
        if not can_cross_bridge(inventory):
            return current_location, energy, False

    if energy <= 0:
        return current_location, energy, False

    if destination == "old bridge":
        new_location = "Old Bridge"
    else:
        new_location = destination.capitalize()

    energy -= 1

    return new_location, energy, True

def can_cross_bridge(inventory):
    if "rope" in inventory:
        return True
    else:
        return False 


def can_light_beacon(inventory):
    if "lantern" in inventory:
        return True
    else:
        return False  


def win_game(current_location, inventory):
    if current_location == "Lighthouse" and "lantern" in inventory:
        return True
    else:
        return False


def lose_game(energy):
    if energy <= 0:
        return True
    else:
        return False      