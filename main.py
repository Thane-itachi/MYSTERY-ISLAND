# player_name = "Thane"
# energy = 5
# location = "jungle"


# print(player_name)
# print(location)
# print(energy)

# player_name = input("Enter your name: ")
# print("Welcome to Mystery Island!")


from game import create_game, collect_item, move_player, can_cross_bridge, can_light_beacon, win_game, lose_game

print("==============================")
print("     THE LOST LIGHTHOUSE")
print("==============================")

# REPLAY LOOP
while True:

    player_name = input("\nEnter your name: ")


    # current_location = "Beach"

    # energy = 5

    # inventory = []


    current_location, energy, inventory = create_game()

    print(f"\nWelcome to Mystery Island, {player_name}!")
    # GAME LOOP
    while True:
        print(f"\n========== {current_location.upper()} ==========")
        
        if current_location == "Beach":
            print("You wake up on a mysterious island.")
    
        elif current_location == "Jungle":
            print("You are surrounded by tall trees.")
    
        elif current_location == "Cave":
            print("You are inside a dark cave.")
    
        elif current_location == "Old Bridge":
            print("You are standing on an old wooden bridge.")
    
        elif current_location == "Lighthouse":
            print("You have reached the lighthouse.")
    
    
        print(f"Energy: {energy}")
        print(f"Inventory: {inventory}")        
    
    
        print("\nWhat would you like to do?")
        print("1. Look around")
        print("2. Check the surroundings")
        print("3. Move")
        print("4. Check inventory")
        print("5. Light lighthouse beacon")
        print("Q. Quit game")
    
    
        choice = input("\nEnter your choice: ").strip().lower()
    
     # EXPLORE
    
        if choice == "1":
    
            if current_location == "Beach":
    
                print("\nYou search the beach.")
    
                if collect_item(inventory, "rope"):
                    print("You found a rope!")
                else:
                    print("You already collected the rope.")
    
            elif current_location == "Jungle":
    
                print("\nYou explore the jungle.")
                print("You discover a hidden path leading to a cave.")
    
            elif current_location == "Cave":
    
                print("\nYou explore the dark cave.")
    
                if collect_item(inventory, "lantern"):
                    print("You found a lantern!")
                else:
                    print("You already collected the lantern.")
    
            elif current_location == "Old Bridge":
    
                print("\nYou inspect the old bridge.")
    
                if "rope" in inventory:
                    print("Your rope can help you cross safely.")
                else:
                    print("The bridge is damaged. You need a rope.")
    
            elif current_location == "Lighthouse":
    
                print("\nYou explore the lighthouse.")
                print("The beacon is waiting to be restored.")
    
        # CHECK SURROUNDINGS
    
        elif choice == "2":
    
            print(f"\nYou carefully inspect the {current_location}.")
    
            if current_location == "Beach":
                print("You see the jungle ahead.")
    
            elif current_location == "Jungle":
                print("You see a dark cave nearby.")
    
            elif current_location == "Cave":
                print("You see an old bridge ahead.")
    
            elif current_location == "Old Bridge":
                print("The lighthouse stands across the bridge.")
    
            elif current_location == "Lighthouse":
                print("You see the broken lighthouse beacon.")
    # MOVEMENT

        elif choice == "3":

            if current_location == "Beach":
                print("\nAvailable destination: Jungle")

            elif current_location == "Jungle":
                print("\nAvailable destinations: Beach, Cave")

            elif current_location == "Cave":
                print("\nAvailable destinations: Jungle, Old Bridge")

            elif current_location == "Old Bridge":
                print("\nAvailable destinations: Cave, Lighthouse")

            elif current_location == "Lighthouse":
                print("\nAvailable destination: Old Bridge")

            destination = input("Where do you want to go? ").strip().lower()

            if current_location == "Cave" and destination == "old bridge" and not can_cross_bridge(inventory):
                print("\nYou need a rope to cross the bridge.")

            elif energy <= 0:
                print("\nYou have no energy left.")

            else:
                current_location, energy, moved = move_player(
                    current_location, destination, energy, inventory
                )

                if moved:
                    print(f"\nYou travelled to {current_location}!")

                else:
                    print("\nInvalid destination.")

    
            # ENERGY CHECK
    
            if lose_game(energy):
                print("\nYou have run out of energy!")
                print("GAME OVER!")
                break
    
        # INVENTORY
    
        elif choice == "4":
    
            print("\n========== INVENTORY ==========")
    
            if inventory:
                for item in inventory:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")
    
        # LIGHTHOUSE
    
        elif choice == "5":
    
            if current_location != "Lighthouse":
    
                print("\nYou must reach the Lighthouse first.")
    
            elif not can_light_beacon(inventory):
    
                print("\nYou need a lantern to light the beacon.")
    
            elif energy <= 0:
    
                print("\nYou are too exhausted to light the beacon.")
    
            elif win_game(current_location, inventory):
    
                print("\nYou climb the lighthouse stairs.")
                print("You use your lantern to restore the beacon.")
    
                print("\n================================")
                print("       THE BEACON IS LIT!")
                print("================================")
    
                print("\nA rescue boat sees the light.")
                print("Congratulations! You escaped Mystery Island!")
    
                break
    
        # QUIT
    
        elif choice == "q":
    
            print("\nYou abandoned your adventure.")
            print("Thanks for playing Mystery Island!")
    
            break
    
        # INVALID INPUT
    
        else:
    
            print("\nInvalid choice. Please try again.")
    
    # REPLAY

    print("\n================================")
    print("          GAME ENDED")
    print("================================")

    replay = input("Would you like to play again? (yes/no): ").strip().lower()

    if replay != "yes":
        print("Thanks for playing THE LOST LIGHTHOUSE!")
        break
