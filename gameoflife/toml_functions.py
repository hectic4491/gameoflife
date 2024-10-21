import toml
from pathlib import Path

DATA_PATH = Path('gameoflife') / 'data'

# Simulation Reading Functions #
def readTOML_sim_names():
    path = DATA_PATH.joinpath('structures.toml')
    with open(path, 'r') as f:
        sim_dict = toml.load(f)
    return sim_dict.keys()

def readTOML_cells(SEED):
    path = DATA_PATH.joinpath('structures.toml')
    with open(path, 'r') as f:
        sim_dict = toml.load(f)
    return sim_dict[SEED]['alive_cells']


# Settings Themes Functions #
def readTOML_all_themes_name():
    path = DATA_PATH.joinpath('themes.toml')
    with open(path, 'r') as f:
        theme_dict = toml.load(f)
    return list(theme_dict.keys())

def readTOML_themes_name(THEMES):
    path = DATA_PATH.joinpath('themes.toml')
    with open(path, 'r') as f:
        theme_dict_name = toml.load(f)
    return theme_dict_name[THEMES]["Name"]

def readTOML_themes(THEMES_NAME):
    path = DATA_PATH.joinpath('themes.toml')
    with open(path, 'r') as f:
        theme_dict = toml.load(f)
    return theme_dict[THEMES_NAME]


# Settings Graphics Functions #
def readTOML_all_graphics_name():
    path = DATA_PATH.joinpath('graphics.toml')
    with open(path, 'r') as f:
        graphic_dict = toml.load(f)
    return list(graphic_dict.keys())

def readTOML_graphics_name(GRAPHICS):
    path = DATA_PATH.joinpath('graphics.toml')
    with open(path, 'r') as f:
        graphic_dict_name = toml.load(f)
    return graphic_dict_name[GRAPHICS]["Name"]

def readTOML_graphics(GRAPHICS_NAME):
    path = DATA_PATH.joinpath('graphics.toml')
    with open(path, 'r') as f:
        graphic_dict = toml.load(f)
    return graphic_dict[GRAPHICS_NAME]


# Settings Resolutions Functions #
def readTOML_all_resolutions_name():
    path = DATA_PATH.joinpath('resolutions.toml')
    with open(path, 'r') as f:
        res_dict = toml.load(f)
    return list(res_dict.keys())

def readTOML_resolution(RESOLUTION_NAME):
    path = DATA_PATH.joinpath('resolutions.toml')
    with open(path, 'r') as f:
        res_dict = toml.load(f)
    return res_dict[RESOLUTION_NAME]


# Default Functions #
def readTOML_default(arguement):
    path = DATA_PATH.joinpath('default.toml')
    with open(path, 'r') as f:
        default = toml.load(f)
    return default['Default'][arguement]


def writeTOML_default(themes, graphics, resolution, framerate):
    path = DATA_PATH.joinpath('default.toml')
    with open(path, 'r') as f:
        default = toml.load(f)

    default['Default']['THEMES'] = themes
    default['Default']['GRAPHICS'] = graphics
    default['Default']['RESOLUTION'] = resolution
    default['Default']['FRAMERATE'] = framerate

    with open(path, 'w') as f:
        toml.dump(default, f)


def writeTOML_default_fullscreen(fullscreen):
    path = DATA_PATH.joinpath('default.toml')
    with open(path, 'r') as f:
        default = toml.load(f)

    default['Default']['FULLSCREEN'] = fullscreen

    with open(path, 'w') as f:
        toml.dump(default, f)