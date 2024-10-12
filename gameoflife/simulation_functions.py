from random import randint
from tkinter import END

import gameoflife.cell as cell
import gameoflife.toml_functions as tf


def generateDisplay(displaySize: tuple) -> list:
    """
    Generates a display of given display size.\n
    A display is a list of lists, where the lists contain cell objects.\n
    """
    # create display
    display = list()

    for j in range(0, displaySize[1]):
        display.append([cell.Cell() for _ in range(0, (displaySize[0]))])

    # Connect neighbors by appending neighboring cells for each _cell.neighbors attribute.
    for j, row in enumerate(display):
        for i, _cell in enumerate(row):

            _cell.neighbors.append(display[j-1][i-1])
            _cell.neighbors.append(display[j-1][i])
            _cell.neighbors.append(display[j-1][(i+1) % len(row)])

            _cell.neighbors.append(display[j][i-1])
            _cell.neighbors.append(display[j][(i+1) % len(row)])

            _cell.neighbors.append(display[(j+1) % len(display)][i-1])
            _cell.neighbors.append(display[(j+1) % len(display)][i])
            _cell.neighbors.append(display[(j+1) % len(display)][(i+1) % len(row)])
            
    return display


def insertDisplay(label, display):
    """
    Inserts the given display into the given label widget.\n
    """
    label.delete("1.0", END)
    for i, row in enumerate(display):
        line = str()
        for cell in row:
            line += cell.character + ' '
        line += '\n'
        index = str(i+1) + ".0"
        label.insert(index, line)
    label.delete("end-1l", END) # removes last '\n'


def createEmptyDisplay(label, displaySize):
    """
    Generates and inserts a blank display of given display size into given label widget.
    """
    display = generateDisplay(displaySize)
    insertDisplay(label, display)


def randomizeInitialAliveCells(display, rollUpperLimit=3):
    """
    Calls the cell.makeAlive() method to a random set of the cells on the given display.\n
    A higher rollUpperLimit results in a lower probability of calling cell.makeAlive().
    """
    for j in range(len(display)):
        for i in range(len(display[0])):
            randomRoll = randint(0, rollUpperLimit)
            if randomRoll == 1:
                display[j][i].makeAlive()


def setInitialAliveCells(display, SEED):
    """
    Calls the cell.makeAlive() method to a set group of cells on the given disaply.\n
    The set of cells depends on the given SEED.
    """
    alive_cells = tf.readTOML_cells(SEED)

    for j, i in alive_cells:
        display[j][i].makeAlive()


def determineNextGen(display):
    """
    Calls the cell.determineNextState() method on every cell of the given display.
    """
    for j in range(len(display)):
        for i in range(len(display[0])):
            display[j][i].determineNextState()


def updateNextGen(display):
    """
    Calls the cell.updateState() method on every cell of the given display.
    """
    for j in range(len(display)):
        for i in range(len(display[0])):
            display[j][i].updateState()


def countPopulation(display):
    """
    Counts the cell population of the given display.\n
    Returns the population as an int.
    """
    population = int()
    for j in range(len(display)):
        for i in range(len(display[0])):
            if display[j][i].alive:
                population += 1
    return population



### TODO ###
def checkStaticPop(population, running, popcheck):
    if len(popcheck) >= 10:
        running = False

    if len(popcheck) == 0:
        popcheck.append(population)
    elif popcheck[-1] == population:
        popcheck.append(population)
    else:
        popcheck = []
### TODO ###