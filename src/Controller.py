from src.Scrapper import Scrapper
from src.Extractor import Extractor
from src.Plotter import Plotter
class Controller:
    def __init__(self):
        pass
    def create_graph(self,town:str,option:str) -> bytes:
        e = Extractor()
        s = Scrapper()
        p = Plotter()
        response = s.create_response(town)
        df = e.extract_data(response)
        return p.plot(df,option)