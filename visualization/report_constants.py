import os

# Filenames and pathes
STR_DATA_NAME = "Visualization\\short_test_data.xlsx"
SPEED_DATA_NAME = "Visualization\\short_speed_data.xlsx"
STR_REPORT_NAME = "Visualization\\Stratography report example"
SPEED_REPORT_NAME = "Visualization\\Speed report example"
MAP_NAME = "Visualization\\Drilling map example"
DATA_PATH = os.getcwd()
EXPORT_PATH = os.getcwd()

# Data fields
REPORT_COLUMNS = ["flow", "rpm", "wob"]
SPEED_COLUMNS = ["speed"]
WELL_ID_FIELD_NAME = "well_id"

# Plot visualization parameters
STR_PLOT_SIZE = (8.5,11)
SPEED_PLOT_HEIGHT = 5
SPEED_PLOY_ASPECT = 2.1
STR_PLOT_MAIN_TITLE = "Drilling report for stratography"
SPEED_PLOT_MAIN_TITLE = "Speed report for stratography"
STR_PLOT_XLABLE_NAME = "Stratography"
SPEED_PLOT_XLABLE_NAME = "Stratography"

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
