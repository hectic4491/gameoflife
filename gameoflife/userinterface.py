import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class UserInterface():

    def __init__(self, simulation):

    ### Main Window ###
        self.root = tk.Tk()
        self.root.title("Conway's Game of Life")
        if simulation.FULLSCREEN == True:
            self.root.attributes("-fullscreen", True)
        else:
            self.root.geometry(simulation.RESOLUTION["WINDOW_SIZE"])
        self.root.resizable(width=False, height=False)     

    ### Fonts ###
        self.field_font = ("courier new", 8)
        self.menu_font = ("courier new", 12)

    ### Tab System ###
        self.tab_system = ttk.Notebook(master=self.root)

    ## Make Tabs ##
        self.main_tab = tk.Frame(master=self.root,
                                 bg=simulation.THEMES["Frame"])
        self.settings_tab = tk.Frame(master=self.root,
                                     bg=simulation.THEMES["Frame"])
        self.about_tab = tk.Frame(master=self.root,
                                  bg=simulation.THEMES["Frame"])

    ## Attach Tabs ##
        self.tab_system.add(self.main_tab,
                            text="Main")
        self.tab_system.add(self.settings_tab,
                            text="Settings")
        self.tab_system.add(self.about_tab,
                            text="About")

        self.tab_system.pack(fill="both",
                        expand=True)


    ### Main Tab Frame ###
    ## Configure Grid ##
        self.main_tab.rowconfigure([n for n in range(4)], weight=5)
        self.main_tab.rowconfigure(4, weight=32)
        self.main_tab.rowconfigure([n for n in range(5, 8)], weight=3)

        self.main_tab.columnconfigure(0, weight=1)
        self.main_tab.columnconfigure(1, weight = 20)

    ## Make and Place Widgets ##
        self.btn_start = tk.Button(master=self.main_tab,
                                   font=self.menu_font,
                                   text="Start",
                                   bg=simulation.THEMES["StartButton"],
                                   fg=simulation.THEMES["MenuText"])
        self.btn_start.grid(row=0,
                            column=0,
                            sticky="nsew",
                            padx=5,
                            pady=5)

        self.btn_stop = tk.Button(master=self.main_tab,
                                  font=self.menu_font,
                                  text="Stop",
                                  bg=simulation.THEMES["StopQuitButtons"],
                                  fg=simulation.THEMES["MenuText"])
        self.btn_stop.grid(row=1,
                           column=0,
                           sticky="nsew",
                           padx=5,
                           pady=5)

        self.btn_new = tk.Button(master=self.main_tab,
                                font=self.menu_font,
                                text="New",
                                bg=simulation.THEMES["ControlButtons"],
                                fg=simulation.THEMES["MenuText"])
        self.btn_new.grid(row=2,
                          column=0,
                          sticky="nsew",
                          padx=5,
                          pady=5)

        self.btn_select = tk.Button(master=self.main_tab,
                                    font=self.menu_font,
                                    text="Select",
                                    bg=simulation.THEMES["ControlButtons"],
                                    fg=simulation.THEMES["MenuText"])
        self.btn_select.grid(row=3,
                             column=0,
                             sticky="nsew",
                             padx=5,
                             pady=5)

        self.listbox_select = tk.Listbox(master=self.main_tab,
                                         font=self.menu_font,
                                         bg=simulation.THEMES["Labels"],
                                         fg=simulation.THEMES["MenuText"],
                                         selectmode="single")
        self.listbox_select.grid(row=4,
                                 column=0,
                                 sticky="nsew",
                                 padx=5,
                                 pady=5)

        self.lbl_name = tk.Label(master=self.main_tab,
                                 font=self.menu_font,
                                 text="Name: Random",
                                 bg=simulation.THEMES["Labels"],
                                 fg=simulation.THEMES["MenuText"])
        self.lbl_name.grid(row=5,
                           column=0,
                           sticky="nsew",
                           padx=5,
                           pady=(5, 0))

        self.lbl_gen = tk.Label(master=self.main_tab,
                                font=self.menu_font,
                                text=f"Gen: {simulation.GENERATION}",
                                bg=simulation.THEMES["Labels"],
                                fg=simulation.THEMES["MenuText"])
        self.lbl_gen.grid(row=6,
                          column=0,
                          sticky="nsew",
                          padx=5)

        self.lbl_pop = tk.Label(master=self.main_tab,
                                font=self.menu_font,
                                text=f"Pop: {simulation.POPULATION}",
                                bg=simulation.THEMES["Labels"],
                                fg=simulation.THEMES["MenuText"])
        self.lbl_pop.grid(row=7,
                          column=0,
                          sticky="nsew",
                          padx=5,
                          pady=(0, 5))

        self.btn_quit = tk.Button(master=self.main_tab,
                                  font=self.menu_font,
                                  text="Quit",
                                  bg=simulation.THEMES["StopQuitButtons"],
                                  fg=simulation.THEMES["MenuText"])
        self.btn_quit.grid(row=8,
                           column=0,
                           sticky="nsew",
                           padx=5,
                           pady=5)

    ## Display Field ##
    # Make display field #
        self.txt_display_field = tk.Text(master=self.main_tab,
                                            font=self.field_font,
                                            bg=simulation.THEMES["SimBackground"],
                                            fg=simulation.THEMES["SimText"])

        self.txt_display_field.grid(row=0,
                                column=1,
                                rowspan=9,
                                sticky="nsew")
        

    ### Settings Tab Frame ###
    ## Configure Grid ##
        self.settings_tab.rowconfigure([n for n in range(3)], weight=1)
        self.settings_tab.rowconfigure(3, weight=6)
        self.settings_tab.rowconfigure(4, weight=2)

        self.settings_tab.columnconfigure([n for n in range(4)], weight=1)

    ## Make and Place Widgets ##
        self.lbl_themes = tk.Label(master=self.settings_tab,
                                   font=self.menu_font,
                                   text="Themes",
                                   bg=simulation.THEMES["Labels"],
                                   fg=simulation.THEMES["MenuText"])
        self.lbl_themes.grid(row=0,
                        column=0,
                        sticky="nsew",
                        padx=5,
                        pady=5)

        self.lbl_themes_cur = tk.Label(master=self.settings_tab,
                                       font=self.menu_font,
                                       text=f"Current: {simulation.THEMES_NAME}",
                                       bg=simulation.THEMES["Labels"],
                                       fg=simulation.THEMES["MenuText"])
        self.lbl_themes_cur.grid(row=1,
                                 column=0,
                                 sticky="nsew",
                                 padx=5,
                                 pady=5)

        selected_themes = tk.StringVar()
        self.cmbbx_themes = ttk.Combobox(master=self.settings_tab,
                                         font=self.menu_font,
                                         textvariable=selected_themes,
                                         state='readonly')
        self.cmbbx_themes.grid(row=3,
                                column=0,
                                sticky="new",
                                padx=5,
                                pady=5)


        self.lbl_graphics = tk.Label(master=self.settings_tab,
                            font=self.menu_font,
                            text="Cells",
                            bg=simulation.THEMES["Labels"],
                            fg=simulation.THEMES["MenuText"])
        self.lbl_graphics.grid(row=0,
                            column=1,
                            sticky="nsew",
                            padx=5,
                            pady=5)

        self.lbl_graphics_cur = tk.Label(master=self.settings_tab,
                                      font=self.menu_font,
                                      text=f"Current: {simulation.GRAPHICS_NAME}",
                                      bg=simulation.THEMES["Labels"],
                                      fg=simulation.THEMES["MenuText"])
        self.lbl_graphics_cur.grid(row=1,
                                column=1,
                                sticky="nsew",
                                padx=5,
                                pady=5)

        selected_graphics = tk.StringVar()
        self.cmbbx_graphics = ttk.Combobox(master=self.settings_tab,
                                        font=self.menu_font,
                                        textvariable=selected_graphics,
                                        state='readonly')
        self.cmbbx_graphics.grid(row=3,
                              column=1,
                              sticky="new",
                              padx=5,
                              pady=5)


        self.lbl_resolution = tk.Label(master=self.settings_tab,
                                       font=self.menu_font,
                                       text="Resolution",
                                       bg=simulation.THEMES["Labels"],
                                       fg=simulation.THEMES["MenuText"])
        self.lbl_resolution.grid(row=0,
                                 column=2,
                                 sticky="nsew",
                                 padx=5,
                                 pady=5)

        self.lbl_resolution_cur = tk.Label(master=self.settings_tab,
                                          font=self.menu_font,
                                          text=f"Current: {simulation.RESOLUTION["WINDOW_SIZE"]}",
                                          bg=simulation.THEMES["Labels"],
                                          fg=simulation.THEMES["MenuText"])
        self.lbl_resolution_cur.grid(row=1,
                                    column=2,
                                    sticky="nsew",
                                    padx=5,
                                    pady=5)
        
        if simulation.FULLSCREEN == False:
            selected_resolution = tk.StringVar()
            self.cmbbx_resolution = ttk.Combobox(master=self.settings_tab,
                                                font=self.menu_font,
                                                textvariable=selected_resolution,
                                                state='readonly')
            self.cmbbx_resolution.grid(row=3,
                                    column=2,
                                    sticky="new",
                                    padx=5,
                                    pady=5)
        
        self.btn_fullscreen = tk.Button(master=self.settings_tab,
                                        font=self.menu_font,
                                        bg=simulation.THEMES["Labels"],
                                        fg=simulation.THEMES["MenuText"])
        if simulation.FULLSCREEN == False:
            self.btn_fullscreen.configure(text="Fullscreen")
        else:
            self.btn_fullscreen.configure(text="Windowed")

        self.btn_fullscreen.grid(row=2,
                                 column=2,
                                 sticky="ew",
                                 padx=5,
                                 pady=5)


        self.lbl_framerate = tk.Label(master=self.settings_tab,
                                      font=self.menu_font,
                                      text="Framerate",
                                      bg=simulation.THEMES["Labels"],
                                      fg=simulation.THEMES["MenuText"])
        self.lbl_framerate.grid(row=0,
                                column=3,
                                sticky="nsew",
                                padx=5,
                                pady=5)

        self.lbl_framerate_cur = tk.Label(master=self.settings_tab,
                                          font=self.menu_font,
                                          text=f"Current: {simulation.FRAMERATE}",
                                          bg=simulation.THEMES["Labels"],
                                          fg=simulation.THEMES["MenuText"])
        self.lbl_framerate_cur.grid(row=1,
                                    column=3,
                                    sticky="nsew",
                                    padx=5,
                                    pady=5)

        selected_framerate = tk.StringVar()
        self.cmbbx_framerate = ttk.Combobox(master=self.settings_tab,
                                            font=self.menu_font,
                                            textvariable=selected_framerate,
                                            state='readonly')
        self.cmbbx_framerate.grid(row=3,
                                  column=3,
                                  sticky="new",
                                  padx=5,
                                  pady=5)


        self.btn_submit = tk.Button(master=self.settings_tab,
                                    font=self.menu_font,
                                    text="Submit Settings",
                                    bg=simulation.THEMES["StartButton"],
                                    fg=simulation.THEMES["MenuText"])

        self.btn_submit.grid(row=4,
                        column=1,
                        columnspan=2)