from matplotlib.figure import Figure
from matplotlib.backends.backend_svg import FigureCanvasSVG
import io
import pandas
class Plotter:
    def __init__(self):
        pass

    def label_name(self, option:str) -> str:
        return {
            'Случаев заражения': 'Количество зараженных',
            'Умерло': 'Количество погибших',
            'Выздоровело': 'Количество выздоровевших'

        }[option]

    def plot(self, frame: pandas.DataFrame, option:str) -> bytes:
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.plot(frame['id'], frame[option])
        axis.set_xlabel("День с начала пандемии")
        axis.set_ylabel(self.label_name(option))
        output = io.BytesIO()
        FigureCanvasSVG(fig).print_svg(output)
        x = output.getvalue()
        return x
