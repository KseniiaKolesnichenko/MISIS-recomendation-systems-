import os

# Filenames and pathes
DATA_NAME = "short_test_data.xlsx"
REPORT_NAME = "Drilling report example"
MAP_NAME = "Drilling map example"
DATA_PATH = os.getcwd()
EXPORT_PATH = os.getcwd()

# Data fields
REPORT_COLUMNS = ["flow", "mse", "rpm", "dexp", "rop", "wob"]
WELL_ID_FIELD_NAME = "well_id"

# Plot visualization parameters
PLOT_SIZE = (8.5,11)
PLOT_MAIN_TITLE = "Drilling report for horizons"
PLOT_XLABLE_NAME = "Horizons"

# Coordinates generator parameters
IS_RANDOM_SEED_ACTIVE = True          # Switch off to real randomization
RANDOM_SEED = 2022
RANDOM_COORDS_THRESHOLD = 0.15        # "Window" for generator to select new coordinate
THRESHOLD_MODIFYER = 2                # Compensate differences between latitude and longtitude

# Basic map parameters
MAP_CENTER = [66.07241960912883, 57.355682449016605]
ZOOM_START = 10
TILES_TYPE = "Stamen Terrain"
MAP_TITLE = "Region wells map"
ICON_SIZE = (150,36)
ICON_ANCHOR = (7,20)
TARGET_COLOR = "red"
OTHERS_COLOR = "black"
