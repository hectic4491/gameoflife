from simulation import Simulation
from userinterface import UserInterface
from cell import Cell
import userinterface_functions as uif

from functools import partial


def main():


    ## Initialize Singletons ##
    simulation = Simulation()
    ui = UserInterface(simulation=simulation)

    ## Initialize Graphics
    Cell.setGraphics(simulation=simulation)

    ## Initialize txt_field ##
    uif.measure_txt_field(ui=ui, simulation=simulation)
    uif.initialize_txt_field(ui=ui, simulation=simulation)


    ## Configure Commands ##
    ui.btn_start.configure(command=partial(uif.startSimulation,
                                           ui=ui,
                                           simulation=simulation))
    
    ui.btn_stop.configure(command=partial(uif.stopSimulation,
                                          ui=ui,
                                          simulation=simulation))
    
    ui.btn_new.configure(command=partial(uif.newSimulation,
                                         ui=ui,
                                         simulation=simulation))
    
    ui.btn_select.configure(command=partial(uif.submitSelection,
                                            ui=ui,
                                            simulation=simulation))
    
    ui.btn_quit.configure(command=partial(uif.quitApplication,
                                          ui=ui))
    
    ui.btn_submit.configure(command=partial(uif.submitSettings,
                                            ui=ui,
                                            simulation=simulation))
    
    ui.btn_fullscreen.configure(command=partial(uif.toggleFullscreen,
                                                ui=ui,
                                                simulation=simulation))
    
    ui.tab_system.bind("<<NotebookTabChanged>>", lambda _: uif.stopSimulation(ui=ui,
                                                                              simulation=simulation))
    


    ## Insert Fields ##
    # Menu Selection Field #
    uif.insertSimInitializations(ui=ui)


    # Setting Fields #
    uif.insertThemes(ui=ui)
    uif.insertGraphics(ui=ui)
    if simulation.FULLSCREEN == False:
        uif.insertResolutionSizes(ui=ui)
    uif.insertFramerates(ui=ui)


    ## Center Application ##
    ui.root.update()
    uif.center_window(ui=ui)

    ## GUI Main Loop ##
    ui.root.mainloop()