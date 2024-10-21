import toml

# Simulation Reading Functions #
def readTOML_sim_names():
    with open(r'gameoflife\gameoflife\data\structures.toml', 'r') as f:
        sim_dict = toml.load(f)
    return sim_dict.keys()

def readTOML_cells(SEED):
    with open(r'gameoflife\gameoflife\data\structures.toml', 'r') as f:
        sim_dict = toml.load(f)
    return sim_dict[SEED]['alive_cells']


# Settings Themes Functions #
def readTOML_all_themes_name():
    with open(r'gameoflife\gameoflife\data\themes.toml', 'r') as f:
        theme_dict = toml.load(f)
    return list(theme_dict.keys())

def readTOML_themes_name(THEMES):
    with open(r'gameoflife\gameoflife\data\themes.toml', 'r') as f:
        theme_dict_name = toml.load(f)
    return theme_dict_name[THEMES]["Name"]

def readTOML_themes(THEMES_NAME):
    with open(r'gameoflife\gameoflife\data\themes.toml', 'r') as f:
        theme_dict = toml.load(f)
    return theme_dict[THEMES_NAME]


# Settings Graphics Functions #
def readTOML_all_graphics_name():
    with open(r'gameoflife\gameoflife\data\graphics.toml', 'r') as f:
        graphic_dict = toml.load(f)
    return list(graphic_dict.keys())

def readTOML_graphics_name(GRAPHICS):
    with open(r'gameoflife\gameoflife\data\graphics.toml', 'r') as f:
        graphic_dict_name = toml.load(f)
    return graphic_dict_name[GRAPHICS]["Name"]

def readTOML_graphics(GRAPHICS_NAME):
    with open(r'gameoflife\gameoflife\data\graphics.toml', 'r') as f:
        graphic_dict = toml.load(f)
    return graphic_dict[GRAPHICS_NAME]


# Settings Resolutions Functions #
def readTOML_all_resolutions_name():
    with open(r'gameoflife\gameoflife\data\resolutions.toml', 'r') as f:
        res_dict = toml.load(f)
    return list(res_dict.keys())

def readTOML_resolution(RESOLUTION_NAME):
    with open(r'gameoflife\gameoflife\data\resolutions.toml', 'r') as f:
        res_dict = toml.load(f)
    return res_dict[RESOLUTION_NAME]


# Default Functions #
def readTOML_default(arguement):
    with open(r'gameoflife\gameoflife\data\default.toml', 'r') as f:
        default = toml.load(f)
    return default['Default'][arguement]


def writeTOML_default(themes, graphics, resolution, framerate):
    with open(r'gameoflife\gameoflife\data\default.toml', 'r') as f:
        default = toml.load(f)

    default['Default']['THEMES'] = themes
    default['Default']['GRAPHICS'] = graphics
    default['Default']['RESOLUTION'] = resolution
    default['Default']['FRAMERATE'] = framerate

    with open(r'gameoflife\gameoflife\data\default.toml', 'w') as f:
        toml.dump(default, f)


def writeTOML_default_fullscreen(fullscreen):
    with open(r'gameoflife\gameoflife\data\default.toml', 'r') as f:
        default = toml.load(f)

    default['Default']['FULLSCREEN'] = fullscreen

    with open(r'gameoflife\gameoflife\data\default.toml', 'w') as f:
        toml.dump(default, f)