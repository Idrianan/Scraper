
from importlib.metadata import requires
from urllib import request
from flask import Flask,render_template,request, Response, session
from src.Controller import Controller
from matplotlib.figure import Figure
from matplotlib.backends.backend_svg import FigureCanvasSVG
app = Flask(__name__)
town_list = ["Санкт-Петербург", "Москва"]

@app.route("/",methods=["GET","POST"])
def hello():
    town = ''
    if request.method == 'POST':
        town = request.form.get('town')
        option = request.form.get('option')
    if town in town_list:
        c = Controller()
        graph = c.create_graph(town,option)
        return Response(graph)
    return render_template('task.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader = False)