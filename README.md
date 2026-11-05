# 🏝️ Mystery Island: The Lost Lighthouse

## Project Description

Mystery Island: The Lost Lighthouse is a beginner-friendly, text-based adventure game built with Python.

The player is stranded on a mysterious island after a storm. To escape, they must explore different locations, collect useful items, manage their energy, cross an old bridge, and restore the lighthouse beacon to signal a rescue boat.

## Features

- Player name input.
- Five explorable locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- Item collection and inventory tracking.
- Energy management system.
- Movement between locations.
- Bridge access requires a rope.
- Lighthouse beacon requires a lantern.
- Winning and losing conditions.
- Invalid input handling.
- Quit and replay options.
- Automated unit tests.

## Technologies Used

- Python 3
- Python unittest module
- Standard Python libraries

No external packages are required.

## Project Structure

```text
MYSTERY-ISLAND/
│
├── main.py
├── game.py
├── main-backup.py
├── README.md
│
└── tests/
    ├── __init__.py
    └── test_game.py
```

## Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.

## How to Run the Game

1. Clone or download the project.
2. Open the project folder in your terminal.
3. Run:

```bash
python3 main.py
```

## How to Play

1. Enter your player name.
2. Start your adventure at the Beach.
3. Explore the island and collect the rope.
4. Travel through the Jungle to find the Cave.
5. Collect the lantern inside the Cave.
6. Use the rope to cross the Old Bridge.
7. Reach the Lighthouse.
8. Use the lantern to restore the beacon.
9. Signal the rescue boat and escape the island.

## Game Rules

- The player starts with 5 energy points.
- Each successful movement consumes 1 energy point.
- Invalid movement does not consume energy.
- The rope is required to cross the Old Bridge.
- The lantern is required to restore the lighthouse beacon.
- Each item can only be collected once.
- The player loses when energy reaches zero before completing the mission.
- The player wins by successfully lighting the lighthouse beacon.
- The player can quit or restart the game.

## Running the Tests

The project includes automated unit tests for the game functions.

Run the tests with:

```bash
python3 -m unittest discover -s tests -v
```

The test suite contains **21 tests** covering:

- Game initialization.
- Valid and invalid movement.
- Energy management.
- Item collection.
- Duplicate item prevention.
- Bridge restrictions.
- Beacon requirements.
- Winning and losing conditions.

## Learning Objectives

This project helped me practise:

- Python variables and data types.
- Lists and inventory management.
- Conditional statements.
- Loops.
- Functions.
- User input and output.
- Error handling.
- Unit testing with unittest.

## Known Limitations

- The game runs in the terminal and does not have a graphical interface.
- Player progress is not saved after exiting.
- The island uses a fixed map and predefined locations.

## Project Status

The game is functional and includes working gameplay, movement, item collection, energy management, winning and losing conditions, invalid input handling, and replay functionality.

The automated test suite contains **21 passing tests**.