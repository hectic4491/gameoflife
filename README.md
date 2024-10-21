# Conway's Game of Life
> A Python GUI application to simulate _John Conway's_ [_Game of Life_](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).



![](gameoflife_example-1.jpg)


## About

  This application provides a full graphical user interface to simulate the famous [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton) Game of Life. The **rule set** was devised by English mathematician [John Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in 1970. The universe of the Game of Life is a two-dimensional matrix of square cells. Traditional simulations allow the matrix to be infinite, but this simulation provides "pac-man connectivity" where the horizontal and vertical edges of the matrix connect back onto itself. Each cell is in either two states, alive or dead. Every cell is connected to it's neighboring eight cells; i.e. the cells horizontally, vertically, and diagonally adjacent. Cells at the edge refer the opposite edge's cells as neighbors. The simulation iterates through generations, where the state of each generation is determined by the **rule set**:
  
> * Any alive cell with fewer than two alive neighbours dies, as if by underpopulation.
> * Any alive cell with two or three alive neighbours lives on to the next generation.
> * Any alive cell with more than three alive neighbours dies, as if by overpopulation.
> * Any dead cell with exactly three alive neighbours becomes an alive cell, as if by reproduction.


  The application comes with a set of initial [patterns](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns) to demonstrate different behaviors. 

  
> * The main _random_ pattern creates a randomized initialized pattern that shows the chaotic nature of the Game of Life.
> * Blinker, Toad, Beacon, Pulsar, and Penta Decathlon show [oscillator](https://en.wikipedia.org/wiki/Oscillator_(cellular_automaton)) behaviors.
> * Glider shows the potential for [spaceships](https://en.wikipedia.org/wiki/Spaceship_(cellular_automaton)); moving cell patterns that traverse the matrix space.
> * [Glider Gun](https://en.wikipedia.org/wiki/Gun_(cellular_automaton)) shows the possibility of creating an infinite reproduction of cells \(the pac-man connectivity eventually causes the pattern to crash into itself, but a truely infinite matrix would show true infinite reproduction\). This pattern of infinite behavior was the first demonstration to disprove Conway's upper limit conjecture. As a result, Game of Life was eventually proved to be Turing Complete.
> * Bunnies demonstrates the potential for emerging behavior, where certain patterns can expand in population rather quickly.

The application was constructed fully in Python. The GUI was constructed with python's native cross-platform _tkinter_ GUI library. Data files are formatted with the _TOML_ configuration file format. The application allows for Windowed and Fullscreen display modes. Further settings can be adjusted in the applications settings menu; specifically the color theme, display characters, and framerate. Default settings are saved in a default.toml file and restored on future launches of the application. This project was created to test python's capabilites of application development with GUI functionality.


## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Requirements
Python:
   * version: 3.12.26
    
Python Libraries:
* toml
   * version: 0.10.2

## Release History

* 1.0.0 (10/20/2024)
   * Release of Conway's Game of Life application.

## Meta

Robert Hunt - ig: [@furtiveplant](https://www.instagram.com/furtiveplant/) - X: [@FurtivePlant](https://x.com/FurtivePlant) - finalrob@gmail.com

[https://github.com/hectic4491/gameoflife](https://github.com/hectic4491/gameoflife)
