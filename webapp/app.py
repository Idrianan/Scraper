import sys
import io
#from importlib import reload
#reload(sys)
#sys.setdefaultencoding('utf-8')
from urllib import request
sys.path.append('../')
from flask import Flask,render_template,request, Response
from flask import send_file
from src.Extractor import Extractor
from src.Scrapper import Scrapper
from src.Plotter import Plotter
import base64
from io import BytesIO
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_svg import FigureCanvasSVG
import seaborn as sns
app = Flask(__name__)
town_list = ["Санкт-Петербург", "Москва"]

@app.route("/",methods=["GET","POST"])
def hello():
    town = ''
    if request.method == 'POST':
        town = request.form.get('town')
    if town in town_list:
        print('a')
        e = Extractor()
        s = Scrapper()
        p = Plotter()
        response = s.create_response(town)
        df = e.extract_data(response)
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        df.info()
        axis.plot(df['id'], df['Случаев заражения'])
        axis.set_xlabel("День с начала пандемии")
        axis.set_ylabel("Количество зараженных")
        output = io.BytesIO()
        FigureCanvasSVG(fig).print_svg(output)
        return Response(output.getvalue())
    return render_template('task.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader = False)