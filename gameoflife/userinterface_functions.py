import simulation_functions as sf
import toml_functions as tf

import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk 
from functools import partial
from cell import Cell

### Command Functions ###
def startSimulation(ui, simulation):
    """
    Command Function.
        -
        Starts/Continues the simulation.
        Disables the Start, New, Select buttons.
        Initiates the loopSimulation loop.
    """
    ui.btn_start.configure(state="disabled") 
    ui.btn_new.configure(state="disabled")
    ui.btn_select.configure(state="disabled")

    simulation.PAUSE = False
    
    if not simulation.DISPLAY:     # if there isn't an active display. i.e. "not continuing an exisiting simulation."
        simulation.GENERATION = 0
        simulation.POPULATION = 0
        buildDisplay(ui=ui, simulation=simulation)

    ui.txt_display_field.configure(state="normal") # open to allow text editing
    
    ui.txt_display_field.delete("1.0", tk.END)
    sf.insertDisplay(ui.txt_display_field, simulation.DISPLAY)

    ui.txt_display_field.configure(state="disabled") # close after editing

    loopSimulation(ui=ui, simulation=simulation)


def stopSimulation(ui, simulation):
    """
    Command Function.
        -
        Pauses the active simulation.
        Sets simulation.PAUSE to True.
        Reenables the Start, New, Select buttons.
    """
    ui.btn_start.configure(state="normal")
    ui.btn_new.configure(state="normal")
    ui.btn_select.configure(state="normal")
    simulation.PAUSE = True


def newSimulation(ui, simulation):
    """
    Command Function.
        -
        Restores the simulation attributes DISPLAY, PAUSE, GENERATION, POPULATION to their default.
        Clears the txt_field text widget.
        Updates the generation and population labels.
    """
    simulation.DISPLAY = None
    simulation.PAUSE = False
    simulation.GENERATION = 0
    simulation.POPULATION = 0

    ui.txt_display_field.configure(state="normal")
    ui.txt_display_field.delete("1.0", tk.END)
    sf.createEmptyDisplay(ui.txt_display_field, simulation.DISPLAY_SIZE)
    ui.txt_display_field.configure(state="disabled")

    ui.lbl_gen.configure(text=f"Gen: {simulation.GENERATION}")
    ui.lbl_pop.configure(text=f"Pop: {simulation.POPULATION}")


def submitSelection(ui, simulation):
    """
    Command Function.
        -
        Sets the global variable SEED to the user's curser selection from the sim_selection listbox.
        Updates the name label.
    """

    ### BUG ### if no selection is made, the active display restarts upon clicking "Start"
    index = ui.listbox_select.curselection()

    if index:   # i.e if index returns nonempty
        simulation.DISPLAY = None
        simulation.SEED = ui.listbox_select.get(index)
        ui.lbl_name.configure(text=simulation.SEED)


def submitSettings(ui, simulation):
    """
    Command Function.
        -
        Updates and sets the settings in the Simulation object.
    """
    THEMES_NAME = ui.cmbbx_themes.get()
    GRAPHICS_NAME = ui.cmbbx_graphics.get()
    if not simulation.FULLSCREEN:
        RESOLUTION_NAME = ui.cmbbx_resolution.get()
    else:
        RESOLUTION_NAME = ""
    FRAMERATE = ui.cmbbx_framerate.get()

    if THEMES_NAME == "":
        THEMES_NAME = simulation.THEMES_NAME

    if GRAPHICS_NAME == "":
        GRAPHICS_NAME = simulation.GRAPHICS_NAME

    if RESOLUTION_NAME == "":
        RESOLUTION_NAME = simulation.RESOLUTION_NAME

    if FRAMERATE == "":
        FRAMERATE = int(simulation.FRAMERATE)
    else:
        FRAMERATE = int(FRAMERATE)

    tf.writeTOML_default(themes=THEMES_NAME, graphics=GRAPHICS_NAME, resolution=RESOLUTION_NAME, framerate=FRAMERATE)


    simulation.THEMES_NAME = THEMES_NAME
    simulation.THEMES = tf.readTOML_themes(THEMES_NAME)
    ui.lbl_themes_cur.configure(text=f"Current: {simulation.THEMES_NAME}")
    updateWidgetThemes(ui=ui, simulation=simulation)

    simulation.GRAPHICS_NAME = GRAPHICS_NAME
    simulation.GRAPHICS = tf.readTOML_graphics(GRAPHICS_NAME)
    ui.lbl_graphics_cur.configure(text=f"Current: {simulation.GRAPHICS_NAME}")
    Cell.setGraphics(simulation)

    simulation.RESOLUTION_NAME = RESOLUTION_NAME
    simulation.RESOLUTION = tf.readTOML_resolution(RESOLUTION_NAME)
    ui.lbl_resolution_cur.configure(text=f"Current: {simulation.RESOLUTION['WINDOW_SIZE']}")
    updateWidgetResolution(ui=ui, simulation=simulation)


    simulation.FRAMERATE = FRAMERATE
    ui.lbl_framerate_cur.configure(text=f"Current: {simulation.FRAMERATE}")

    ui.root.update()
    center_window(ui=ui)

### TODO ###
def toggleFullscreen(ui, simulation):
    if simulation.FULLSCREEN == False:

        simulation.FULLSCREEN = True
        tf.writeTOML_default_fullscreen(fullscreen=True)

        ui.btn_fullscreen.configure(text = "Windowed")
        ui.lbl_resolution_cur.configure(text=f"Current: Fullscreen")
        ui.cmbbx_resolution.destroy()
        ui.root.attributes("-fullscreen", True)
        updateWidgetResolution(ui=ui, simulation=simulation)
        ui.root.update()

    else:

        simulation.FULLSCREEN = False
        tf.writeTOML_default_fullscreen(fullscreen=False)

        ui.btn_fullscreen.configure(text = "Fullscreen")
        ui.lbl_resolution_cur.configure(text=f"Current: {simulation.RESOLUTION['WINDOW_SIZE']}")

        selected_resolution = tk.StringVar()
        ui.cmbbx_resolution = ttk.Combobox(master=ui.settings_tab,
                                             font=ui.menu_font,
                                             textvariable=selected_resolution,
                                             state='readonly')
        ui.cmbbx_resolution.grid(row=3,
                                 column=2,
                                 sticky="new",
                                 padx=5,
                                 pady=5)
        insertResolutionSizes(ui=ui)

        ui.root.attributes("-fullscreen", False)
        updateWidgetResolution(ui=ui, simulation=simulation)
        ui.root.update()


### Helper Functions ###
def buildDisplay(ui, simulation):
    """
    Helper Function.
        -
        Generates a new Display by either:
            - Using the default Random SEED
            - Using the chosen SEED
    """
    simulation.DISPLAY = sf.generateDisplay(simulation.DISPLAY_SIZE)

    # This is the default SEED
    if not simulation.SEED or simulation.SEED == "Random":
        sf.randomizeInitialAliveCells(simulation.DISPLAY, simulation.SPARSITY)
        simulation.SEED = "Random"
        ui.lbl_name.configure(text=simulation.SEED)

    # This is the selected SEED
    else:
        sf.setInitialAliveCells(simulation.DISPLAY, simulation.SEED)


def loopSimulation(ui, simulation):
    """
    Helper Function.
        -
        Loops the simulation:
        Inserts the Display.
        Determines the next gen with .determineNextGen().
        Updates the Display with .updateNextGen().
        Updates the simulation GENERATION and POPULATION attributes.
    """
    if simulation.DISPLAY is not None:
        ui.txt_display_field.configure(state="normal")

        sf.insertDisplay(ui.txt_display_field, simulation.DISPLAY)
        simulation.POPULATION = sf.countPopulation(simulation.DISPLAY)
        sf.determineNextGen(simulation.DISPLAY)
        sf.updateNextGen(simulation.DISPLAY)
        simulation.GENERATION += 1

        ui.lbl_gen.configure(text=f"Gen: {simulation.GENERATION}")
        ui.lbl_pop.configure(text=f"Pop: {simulation.POPULATION}")

        ui.txt_display_field.configure(state="disabled")
        
        if not simulation.PAUSE:

            # f_rate = 1000 // simulation.FRAMERATE

            ui.txt_display_field.after(1000 // simulation.FRAMERATE, partial(loopSimulation,
                                                                    ui=ui,
                                                                    simulation=simulation))


def initialize_txt_field(ui, simulation):
    """
    Helper Function.
        -
        Initializes the txt_field with an empty display.
    """
    ui.txt_display_field.configure(state="normal")
    sf.createEmptyDisplay(ui.txt_display_field, simulation.DISPLAY_SIZE)
    ui.txt_display_field.configure(state="disabled")
    ui.txt_display_field.bind("<Button-1>", disable_text_selection)


def measure_txt_field(ui, simulation):
    """
    Helper Function.
        -
        Measures the width and height of the txt_display_field.
        Sets these measurements to the simulations DISPLAY_SIZE attribute.
    
    """
    # Measure display field height #
    ui.txt_display_field.configure(state="normal")
    ui.txt_display_field.delete("1.0", "end")
    ui.root.update()
    ui.height = 0
    while ui.txt_display_field.yview()[1] == 1.0:
        ui.txt_display_field.insert(tk.END, "H\n")
        ui.height += 1
    ui.txt_display_field.delete("end-2l","end-1l")
    ui.txt_display_field.insert(tk.END, "H")

    # Measure display field width #
    ui.txt_display_field.delete("1.0", "end")

    max_w = ui.txt_display_field.winfo_width()
    max_w -= (ui.txt_display_field['bd']*2)
    font = tkFont.Font(ui.txt_display_field, ui.txt_display_field.cget("font"))
    new_string = ''
    str_pixels = font.measure(new_string, ui.txt_display_field)

    while str_pixels <= max_w:
        new_string += "W"
        str_pixels = font.measure(new_string, ui.txt_display_field)

        if str_pixels > max_w:
            new_string = new_string[:-2]
            break
    ui.width = (len(new_string) // 2)       # we floor divide by 2 because the printed
                                            # display is half cells, half ' ' space characters,
                                            # so the self.width attribute should tell us how many cells to make.
    ui.txt_display_field.configure(state="disabled")
    simulation.DISPLAY_SIZE = (ui.width, ui.height)


def center_window(ui, offset=0):
    """
    Helper Function.
        -
        Centers the application's window to the user's screen.
    """
    
    screen_width = ui.root.winfo_screenwidth()
    screen_height = ui.root.winfo_screenheight()
    x = (screen_width - ui.root.winfo_reqwidth()) // 2
    y = (screen_height - ui.root.winfo_reqheight()) // 2 + offset
    ui.root.geometry(f"+{x}+{y}")


def insertSimInitializations(ui):
    """
    Helper Function.
        -
        Inserts the simulation initialization choices into the listbox widget.
        Reads choice names from the simulations.toml file,
        using the readTOML_names function from the read_toml module.
    """
    # Built in simulation initializations:
    ui.listbox_select.insert(0, 'Random')

    # Simulation initializations from 
    sim_dict_names = tf.readTOML_sim_names()

    for i, key in enumerate(sim_dict_names):
        ui.listbox_select.insert(i+1, key)
        #  i + 1, to offset from the built in simulation type 'Random'


def insertThemes(ui):
    """
    Helper Function.
        -
        Inserts the theme choice into the listbox widget.
    """
    themes_names = tf.readTOML_all_themes_name()
    ui.cmbbx_themes['values'] = themes_names


def insertGraphics(ui):
    """
    Helper Function.
        -
        Inserts the graphic choice into the listbox widget.
    """
    graphics = tf.readTOML_all_graphics_name()
    ui.cmbbx_graphics['values'] = graphics


def insertResolutionSizes(ui):
    """
    Helper Function.
        -
        Inserts the resolution choice into the listbox widget.
    """
    resolutions = tf.readTOML_all_resolutions_name()
    ui.cmbbx_resolution['values'] = resolutions


def insertFramerates(ui):
    """
    Helper Function.
        -
        Inserts the framerate choice into the listbox widget.
    """
    framerates = [1, 2, 3, 4, 8, 12, 16, 24, 30, 60]
    ui.cmbbx_framerate['values'] = framerates


def quitApplication(ui):
    """
    Helper Function.
        -
        Quits the application.
    """
    ui.root.destroy()


def disable_text_selection(event):
    """
    Helper Function.
        -
        Prevents text from being selected in the txt_field widget.
    """
    return "break"


def updateWidgetThemes(ui, simulation):
    """
    Helper Function
        -
        Updates all widgets to the current theme configuration.
    """
    ui.main_tab.configure(bg=simulation.THEMES["Frame"])

    ui.settings_tab.configure(bg=simulation.THEMES["Frame"])

    ui.about_tab.configure(bg=simulation.THEMES["Frame"])

    ui.btn_start.configure(bg=simulation.THEMES["StartButton"],
                           fg=simulation.THEMES["MenuText"])
    
    ui.btn_stop.configure(bg=simulation.THEMES["StopQuitButtons"],
                          fg=simulation.THEMES["MenuText"])

    ui.btn_new.configure(bg=simulation.THEMES["ControlButtons"],
                         fg=simulation.THEMES["MenuText"])

    ui.btn_select.configure(bg=simulation.THEMES["ControlButtons"],
                            fg=simulation.THEMES["MenuText"])

    ui.listbox_select.configure(bg=simulation.THEMES["Labels"],
                                fg=simulation.THEMES["MenuText"])

    ui.lbl_name.configure(bg=simulation.THEMES["Labels"],
                          fg=simulation.THEMES["MenuText"])

    ui.lbl_gen.configure(bg=simulation.THEMES["Labels"],
                         fg=simulation.THEMES["MenuText"])

    ui.lbl_pop.configure(bg=simulation.THEMES["Labels"],
                         fg=simulation.THEMES["MenuText"])

    ui.btn_quit.configure(bg=simulation.THEMES["StopQuitButtons"],
                          fg=simulation.THEMES["MenuText"])

    ui.txt_display_field.configure(bg=simulation.THEMES["SimBackground"],
                                   fg=simulation.THEMES["SimText"])

    ui.lbl_themes.configure(bg=simulation.THEMES["Labels"],
                            fg=simulation.THEMES["MenuText"])  

    ui.lbl_themes_cur.configure(bg=simulation.THEMES["Labels"],
                                fg=simulation.THEMES["MenuText"])

    ui.lbl_graphics.configure(bg=simulation.THEMES["Labels"],
                           fg=simulation.THEMES["MenuText"])  

    ui.lbl_graphics_cur.configure(bg=simulation.THEMES["Labels"],
                               fg=simulation.THEMES["MenuText"])

    ui.lbl_resolution.configure(bg=simulation.THEMES["Labels"],
                                fg=simulation.THEMES["MenuText"])  

    ui.lbl_resolution_cur.configure(bg=simulation.THEMES["Labels"],
                                    fg=simulation.THEMES["MenuText"])

    ui.btn_fullscreen.configure(bg=simulation.THEMES["ControlButtons"],
                                fg=simulation.THEMES["MenuText"])   

    ui.lbl_framerate.configure(bg=simulation.THEMES["Labels"],
                                    fg=simulation.THEMES["MenuText"])  

    ui.lbl_framerate_cur.configure(bg=simulation.THEMES["Labels"],
                                   fg=simulation.THEMES["MenuText"])

    ui.btn_submit.configure(bg=simulation.THEMES["StartButton"],
                            fg=simulation.THEMES["MenuText"])
    
    ui.lbl_about_header.configure(bg=simulation.THEMES["Labels"],
                                  fg=simulation.THEMES["MenuText"])
    
    ui.lbl_about_body.configure(bg=simulation.THEMES["Labels"],
                                fg=simulation.THEMES["MenuText"])


def updateWidgetResolution(ui, simulation):
    """
    Helper Function
        -
        Updates all widgets to the current resolution configuration.
    """
    ui.root.geometry(simulation.RESOLUTION["WINDOW_SIZE"])

    ui.tab_system.select(ui.main_tab)

    measure_txt_field(ui=ui, simulation=simulation)
    submitSelection(ui=ui, simulation=simulation)
    stopSimulation(ui=ui, simulation=simulation)
    initialize_txt_field(ui=ui, simulation=simulation)

    simulation.DISPLAY = None
    simulation.SEED = None