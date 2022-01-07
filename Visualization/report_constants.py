import os


DATA_NAME = "short_test_data.xlsx"
REPORT_NAME = "Drilling report example"
MAP_NAME = "Drilling map example"

DATA_PATH = os.getcwd()
EXPORT_PATH = os.getcwd()

REPORT_COLUMNS = ["flow", "mse", "rpm", "dexp", "rop", "wob"]
WELL_ID_FIELD_NAME = 'well_id'

PLOT_SIZE = (8.5,11)
PLOT_MAIN_TITLE = 'Drilling report for horizons'
PLOT_XLABLE_NAME = 'Horizons'

IS_RANDOM_SEED_ACTIVE = True
RANDOM_SEED = 2022
RANDOM_COORDS_THRESHOLD = 0.15
THRESHOLD_MODIFYER = 2

MAP_CENTER = [66.07241960912883, 57.355682449016605]
ZOOM_START = 10
TILES_TYPE = "Stamen Terrain"
MAP_TITLE = "Region wells map"
ICON_SIZE = (150,36)
ICON_ANCHOR = (7,20)
TARGET_COLOR = 'red'
OTHERS_COLOR = 'black'
