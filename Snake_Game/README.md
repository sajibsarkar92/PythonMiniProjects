# Snake Game 🐍

A classic Snake game implementation in Python using the Turtle graphics library.

## Overview

This is a fun, interactive Snake game where you control a snake to eat food and grow longer. The game features:
- Smooth snake movement and controls
- Food spawning at random locations
- Score tracking
- Progressive difficulty (speed increases every 10 food items eaten)
- Collision detection (walls and self)
- Game restart functionality

## Features

- **Classic Gameplay**: Guide your snake to eat food and avoid collisions
- **Score System**: Track your score as you eat food
- **Progressive Difficulty**: Game speed increases as you progress
- **Collision Detection**: Lose when hitting walls or yourself
- **Restart Functionality**: Press SPACE to restart after game over

## Requirements

- Python 3.6+
- Turtle (included with Python standard library)

## Installation

### Quick Start

Using the Makefile (recommended on macOS/Linux):
```bash
make install
make run
```

### Manual Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## How to Play

1. **Start the Game**: Run `python main.py` to launch the game
2. **Controls**:
   - `UP Arrow` - Move snake up
   - `DOWN Arrow` - Move snake down
   - `LEFT Arrow` - Move snake left
   - `RIGHT Arrow` - Move snake right
   - `SPACE` - Restart the game after game over

3. **Gameplay**:
   - Guide your snake to eat the red food circles
   - Each food item eaten increases your score by 1
   - Your snake grows longer with each food eaten
   - Every 10 food items eaten, the game speed increases by 5%
   - The game ends if you hit a wall or collide with your own tail

4. **Winning**: Try to get the highest score possible!

## Project Structure

```
Snake_Game/
├── main.py           # Main game loop and control logic
├── snake.py          # Snake class and movement logic
├── food.py           # Food class and spawning logic
├── scoreboard.py     # Score tracking and display
├── requirements.txt  # Python dependencies
├── Makefile          # Build and run automation
└── README.md         # This file
```

## File Descriptions

### main.py
The main entry point of the game. Handles:
- Screen setup and initialization
- Game loop management
- Collision detection
- Game state management (running/game over)
- Keyboard input binding

### snake.py
Defines the Snake class with:
- Snake segment management
- Movement logic
- Direction controls (up, down, left, right)
- Snake extension when eating food

### food.py
Defines the Food class with:
- Random food generation at valid positions
- Food spawning within game boundaries

### scoreboard.py
Defines the ScoreBoard class with:
- Score display and updates
- Game over message display

## Game Rules

1. **Movement**: The snake continuously moves in the direction it's heading
2. **Eating**: When the snake's head touches food, the food respawns and the snake grows
3. **Collision - Wall**: If the snake goes beyond the game boundary (±290 pixels), game over
4. **Collision - Self**: If the snake's head touches its own body, game over
5. **Speed**: Game speed increases by 5% for every 10 food items eaten

## Speed Progression

| Food Eaten | Game Speed |
|-----------|-----------|
| 0-9 | 0.10s per move |
| 10-19 | 0.095s per move |
| 20-29 | 0.0903s per move |
| 30+ | Progressively faster... |

## Troubleshooting

### Game window won't open
- Ensure Turtle is properly installed with Python
- On some systems, you may need to install additional graphics libraries

### Game runs very slowly
- Close other applications to free up system resources
- Check if your computer meets the minimum requirements

### Controls not responding
- Make sure the game window is active (focused)
- Try clicking on the game window before using arrow keys

## Development

To clean up cache files:
```bash
make clean
```

## Future Enhancements

Potential features for future versions:
- High score saving and loading
- Multiple difficulty levels
- Obstacles on the game board
- Sound effects and music
- Different snake and food themes
- Pause functionality

## License

This project is open source and available for personal and educational use.

## Author

Created as a learning project to practice Python and game development concepts.

---

**Enjoy the game and try to beat your high score! 🎮**

