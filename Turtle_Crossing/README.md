# Turtle Crossing Game

A fun and interactive game built with Python's `turtle` module where you help a turtle cross a busy street while avoiding cars!

## Overview

In this game, you control a turtle character trying to cross a road filled with moving cars. Each time you successfully reach the other side, the level increases and the cars move faster. The game ends if your turtle collides with a car.

## Game Features

- **Progressive Difficulty**: Each level increases car speed
- **Level Tracking**: Display current level on the scoreboard
- **Collision Detection**: Game over when turtle hits a car
- **Smooth Animation**: 60 FPS game loop
- **Random Car Generation**: Cars spawn at random positions with random colors

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python's standard library `turtle` module)

## Installation

1. Clone or download this repository
2. Ensure Python 3.6+ is installed on your system

## Usage

Run the game with:

```bash
python main.py
```

## Controls

- **Up Arrow**: Move the turtle up

## Game Mechanics

- **Objective**: Move the turtle to the top of the screen without hitting any cars
- **Cars**: Randomly spawn and move across the screen from right to left
- **Levels**: Each successful crossing increases the level and car speed
- **Game Over**: Collision with a car ends the game

## Project Structure

```
Turtle_Crossing/
├── main.py              # Main game loop
├── player.py            # Player/Turtle class
├── car_manager.py       # Car spawning and movement logic
├── scoreboard.py        # Level display and game over screen
└── requirements.txt     # Project dependencies
```

## File Descriptions

### `main.py`
The main game loop that initializes the screen, handles game logic, collision detection, and level progression.

### `player.py`
Defines the `Player` class which extends the `Turtle` class. Handles player movement and collision detection with the finish line.

### `car_manager.py`
Defines the `CarManager` class responsible for creating, moving, and managing cars. Handles speed increases with each level.

### `scoreboard.py`
Defines the `Scoreboard` class for displaying the current level and game over message.

## Game Tips

- Time your movements carefully to avoid cars
- Watch the patterns of car movement
- Reach the finish line to progress to the next level

## Future Enhancements

- Score multiplier system
- Different difficulty modes
- Sound effects
- Leaderboard

## Author

Created as a learning project for Python game development.

## License

This project is open source and available for educational purposes.

