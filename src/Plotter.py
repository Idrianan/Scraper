from matplotlib.figure import Figure
import base64
from io import BytesIO

class Plotter:
    def __init__(self):
        pass
    def plot(self,frame,option):
        figure = Figure()
        ax = figure.subplots()
        ax.plot(data = frame[option])
        buf = BytesIO()
        figure.savefig(buf,format = "png")
        d = base64.b64decode(buf.getbuffer()).decode("utf-8")
        print(d)
        return None
