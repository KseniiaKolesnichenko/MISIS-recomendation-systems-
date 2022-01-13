#Коментарии по CLI: 1. Формат CLI выглядит как:
# "название_скрипта --- есть
# папка_с_данными_для_обучения --- есть
# список_параметров_из_первичного_датасета --- есть
# расположение_файла_для рекомендационной_системы --- есть
# расположение_конечного_файла_выгруженных_данных" --- есть

import click
import pandas as pd

list_param = str('Depth_m, Litology, Bit_load_tonnes, Rotor_speed, Inlet_density_g/cc, Inlet_flow_litres/sec, D_bit_mm, D_well_mm, Complication_code, Stratigraphy_code, Markers_horizon_code, Oil_well, Aver_mech_speed_m/h')
#list_param_ru = str('Глубина, Литология, Нагрузка на долото, Скорость ротора, Плотность на входе, Расход на входе (л/сек), Диаметр долота (мм), Диаметр скважины (мм), Код осложнений, Код стратиграфии, Код маркеров горизонта, № скважины, Средняя механическая скорость (м/ч)')

@click.command()

@click.option(
    "--d",
    "-d",
    "data",
    required=True,
    help="Папка с данными для обучения",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
)

@click.option(
    "--p",
    "-p",
    "param",
    default=list_param,
    # либо list_param_ru
    help="Список параметров:"+list_param,
    type=click.STRING,
)

@click.option(
    "--in",
    "-i",
    "in_file",
    required=True,
    help="Расположение_файла_для_рекомендационной_системы",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)

@click.option(
    "--out-file",
    "-o",
    default="./output.xlsx",
    help="Путь к файлу excel для сохранения результата.",
    type=click.Path(dir_okay=False),
)

def process(in_file, out_file, data, param):

    input = pd.read_csv(in_file)
    output = pd.DataFrame(input)
    write_excel = output.to_excel(out_file)
if __name__ == "__main__":
    process()


