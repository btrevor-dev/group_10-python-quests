#Adventure game#


def start_adventure():
    """Start the adventure."""
    print("You wake up at the edge of a dark forest.")
    print("Do you enter the forest or walk along the river?")
    choice = input("Type 'forest' or 'river': ").strip().lower()

    if choice == "forest":
        forest()
    elif choice == "river":
        river()
    else:
        print("Indecision costs you time. Try again.\n")
        start_adventure()


def forest():
    """Forest path."""
    print("\nYou step into the forest. It grows darker.")
    print("You see a cabin and a cave.")
    choice = input("Type 'cabin' or 'cave': ").strip().lower()

    if choice == "cabin":
        good_ending()
    elif choice == "cave":
        bad_ending()
    else:
        print("You wander in circles.\n")
        forest()


def river():
    """River path."""
    print("\nYou walk along the river.")
    print("You find a boat and a bridge.")
    choice = input("Type 'boat' or 'bridge': ").strip().lower()

    if choice == "boat":
        bad_ending()
    elif choice == "bridge":
        good_ending()
    else:
        print("You slip on a rock and rethink your life choices.\n")
        river()


def good_ending():
    """Good ending."""
    print("\nYou made wise choices.")
    print("You discover treasure and live comfortably.")
    print("THE END - Victory")


def bad_ending():
    """Bad ending."""
    print("\nYour choices lead to danger.")
    print("You fall into a trap. Adventure over.")
    print("THE END - Defeat")


if __name__ == "__main__":
    start_adventure()