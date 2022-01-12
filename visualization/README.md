# Visualization system
by Artyom Filippenko
MISIS Classification Project, Team 2
jan 2022


Module for data visualization.
![изображение](https://github.com/KseniiaKolesnichenko/MISIS-recomendation-systems-/blob/main/visualization/Map%20image%20example.png)
![изображение](https://github.com/KseniiaKolesnichenko/MISIS-recomendation-systems-/blob/main/visualization/Speed%20report%20example.png)
![изображение](https://github.com/KseniiaKolesnichenko/MISIS-recomendation-systems-/blob/main/visualization/Stratography%20report%20example.png)


## Functions in report generator:
### generate_horizon_drill_image(data, export_path, export_name, columns)
Generates and saves image from input data using selected columns.
It creates multiple subplots for every pd.Series object in DataFrame.

Args:
- data (pd.DataFrame): Input data with parameters to visualize
- export_path (str, optional): Directory to save image. Defaults to c.EXPORT_PATH.
- export_name (str, optional): Report name. Defaults to c.STR_REPORT_NAME.
- columns (list, optional): Names of parameters to visualize. Defaults to c.REPORT_COLUMNS.

### generate_stratography_speed_lineplot(data, export_path, export_name, columns)
Saves plot of speed for different wells as image

Args:
- data (pd.DataFrame): Input data with parameters to visualize
- export_path (str, optional): Directory to save image. Defaults to c.EXPORT_PATH.
- export_name (str, optional): Report name. Defaults to c.SPEED_REPORT_NAME.
- columns (list, optional): Names of parameters to visualize. Defaults to c.REPORT_COLUMNS.


### generate_random_coordinates(center, threshold, number)
Helps to generate random coordinates.
For demonstration purposes only.

Args:
- center (tuple): Latitiude and longtitute
- threshold (float): Adjust size of zones to lat and long
- number (int): Number of coordinates to generate

Returns:
- list: Coordinates as tuples with shape of 2: (lat, long)

### save_map(data, target_well_label, export_path, export_name)
Generates and saves map with objects.
Target object will be marked with specific color

Args:
- data (pd.DataFrame): Dataframe withh all objects
- target_well_label (int/str): Lable of object o highlight from others
- export_path (str, optional): Directory to save map. Defaults to c.EXPORT_PATH.
- export_name (str, optional): Map name. Defaults to c.MAP_NAME.

## Constants
- Check report_constants.py

## Run
- Import as a module
- Standalone: python .\visualization\report_generator.py

## TODO
- Add real data
- Add new types of diagrams

## Future features
- Compile reports into .pdf

## Examples
Reports generated from "short_test_data.xlsx"
- Drilling map example.html
- Speed report example.png
- Stratography report example.png

## Hints
To install dependencies:
- pip3 install -r report_requirements.txt
