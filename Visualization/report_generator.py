import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import folium
import random
import report_constants as c



def generate_horizon_drill_image(data,
                                 export_path=c.EXPORT_PATH,
                                 export_name=c.REPORT_NAME,
                                 columns=c.REPORT_COLUMNS):
    """Generates and saves image from input data using selected columns.

    Args:
        data (pd.DataFrame): Input data with parameters to visualize
        export_path (str, optional): Directory to save image. Defaults to c.EXPORT_PATH.
        export_name (str, optional): Report name. Defaults to c.REPORT_NAME.
        columns (list, optional): Names of parameters to visualize. Defaults to c.REPORT_COLUMNS.
    """
    assert isinstance(data, pd.DataFrame), \
        "Data must be pd.DataFrame type!"
    for column in columns:
        assert column in data.columns, \
            f"No {column} in data"

    sns.set()
    fig, axes = plt.subplots(len(columns),
                             1,
                             sharex=True,
                             figsize=c.PLOT_SIZE)

    fig.suptitle(c.PLOT_MAIN_TITLE)
    for num, column_name in enumerate(columns):
        sns.lineplot(ax=axes[num],
                    x=data[column_name].index,
                    y=data[column_name].values)
        axes[num].set_title(column_name)
    plt.xlabel(c.PLOT_XLABLE_NAME)

    report_full_path = f"{os.path.join(export_path, export_name)}.png"
    fig.savefig(report_full_path)
    print(f"Drilling report exported to:\n{report_full_path}")


def generate_random_coordinates(center, threshold, number):
    """Helps to generate random coordinates.
    For demonstration purposes only.

    Args:
        center (tuple): Latitiude and longtitute
        threshold (float): Adjust size of zones to lat and long
        number (int): Number of coordinates to generate

    Returns:
        list: Coordinates as tuples with shape of 2: (lat, long)
    """
    assert number >= 1, \
        "Number must be more or equial 1"
    assert len(center) == 2, \
        "Wrong center coordinates shape (must be 2 - lat and long)"
    for coordinate in center:
        assert coordinate > 0.0, \
            "One of the coordinate is less than zero."

    if c.IS_RANDOM_SEED_ACTIVE:
        random.seed(c.RANDOM_SEED)

    coordinates = []
    for _ in range(number):
        random_latitude = random.uniform(center[0]-threshold,
                                         center[0]+threshold)
        random_longtitude = random.uniform(center[1]-threshold*c.THRESHOLD_MODIFYER,
                                           center[1]+threshold*c.THRESHOLD_MODIFYER)
        coordinates.append((random_latitude, random_longtitude))
    return coordinates


def save_map(data,
             target_well_label,
             export_path=c.EXPORT_PATH,
             export_name=c.MAP_NAME):
    """Generates and saves map with objects.
    Target object will be marked with specific color

    Args:
        data (pd.DataFrmae): Dataframe withh all objects
        target_well_label (int/str): Lable of object o highlight from others
        export_path (str, optional): Directory to save map. Defaults to c.EXPORT_PATH.
        export_name (str, optional): Map name. Defaults to c.MAP_NAME.
    """
    well_map = folium.Map(location=c.MAP_CENTER,
                     #width=500,
                     #height=500,
                     zoom_start=c.ZOOM_START,
                     tiles=c.TILES_TYPE)

    coordinates = generate_random_coordinates(
        center=c.MAP_CENTER,
        threshold=c.RANDOM_COORDS_THRESHOLD,
        number=len(data[c.WELL_ID_FIELD_NAME].unique()),
    )

    for well_id, coordinate in zip(data[c.WELL_ID_FIELD_NAME].unique(),
                                   coordinates):
        lat, long = coordinate

        if str(well_id) == str(target_well_label):
            color = c.TARGET_COLOR
        else:
            color = c.OTHERS_COLOR

        icon = folium.DivIcon(
            icon_size=c.ICON_SIZE,
            icon_anchor=c.ICON_ANCHOR,
            html=f'<div style="font-size: 18pt; color : {color}">{well_id}</div>',
        )
        folium.Marker([lat, long], icon=icon).add_to(well_map)

    title_html = f"""<h3 style="font-size:20px"><b>{c.MAP_TITLE}</b></h3>"""
    well_map.get_root().html.add_child(folium.Element(title_html))

    map_export_path = f"{os.path.join(export_path, export_name)}.html"
    well_map.save(outfile=map_export_path)
    print(f"Drilling map exported to:\n{map_export_path}")


if __name__ == "__main__":
    full_data_path = os.path.join(c.DATA_PATH, c.DATA_NAME)
    wells_data = pd.read_excel(full_data_path)

    best_well_label = 1

    best_well_data = \
        wells_data[wells_data[c.WELL_ID_FIELD_NAME]==best_well_label]

    generate_horizon_drill_image(data=best_well_data,
                                 export_path=c.EXPORT_PATH,
                                 export_name=c.REPORT_NAME,
                                 columns=c.REPORT_COLUMNS)

    save_map(data=wells_data,
             target_well_label=best_well_label)

    exit()
