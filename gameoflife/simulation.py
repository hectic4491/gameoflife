import toml_functions as tf

class Simulation():
    """
    Singleton Class.
        -
        Used to store all of our global variables for the application.
    """
    def __init__(self):
        self.DISPLAY = None
        self.DISPLAY_SIZE = None
        self.PAUSE = False
        self.GENERATION = 0
        self.POPULATION = 0
        self.SEED = "Random"
        self.SPARSITY = 3   # to control randomness of the random type simulation

        self.THEMES_NAME = tf.readTOML_default("THEMES") # String
        self.THEMES = tf.readTOML_themes(self.THEMES_NAME) # Dict

        self.GRAPHICS_NAME = tf.readTOML_default("GRAPHICS") # String
        self.GRAPHICS = tf.readTOML_graphics(self.GRAPHICS_NAME) # Dict        

        self.RESOLUTION_NAME = tf.readTOML_default("RESOLUTION") # String
        self.RESOLUTION = tf.readTOML_resolution(self.RESOLUTION_NAME) # Dict

        self.FRAMERATE = tf.readTOML_default("FRAMERATE")

        self.FULLSCREEN = tf.readTOML_default("FULLSCREEN")