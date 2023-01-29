import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from matplotlib.figure import Figure
import seaborn as sns
from Scrapper import Scrapper
from Extractor import Extractor
import seaborn as sns


def define(region:str) ->str:
    if not(region in regions):
        raise ValueError
    elif region == "Санкт-Петербург":
        return 'spb'
    elif region == "Москва":
        return 'msk'

if __name__ == '__main__':
    regions = ["Санкт-Петербург", "Москва"]
    region = "Санкт-Петербург"
    scrapper = Scrapper()
    response = scrapper.create_response(region)
    extractor = Extractor()
    df = extractor.extract_data(response)
    figure = Figure()
    ax = figure.subplots()
    sns.lineplot(data = df['Случаев заражения'])
    buf = BytesIO()
    figure.savefig(buf,format = "png")
    print(buf)


class Plotter:
    def __init__(self):
        pass

    def plot(frame):
        pass
