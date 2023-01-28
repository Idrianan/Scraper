from msilib.schema import ComboBox
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Scrapper import Scrapper
from Extractor import Extractor
from tkinter import *
from tkinter.ttk import Combobox  



def define(region:str) ->str:
    if not(region in regions):
        raise ValueError
    elif region == "Санкт-Петербург":
        return 'spb'
    elif region == "Москва":
        return 'msk'

def clicked():
    plt.close()
    current = combo.get()
    try:
        region = define(current)
    except ValueError:
        print("Пожалуйста, выберите регион из списка")
    scrapper = Scrapper()
    response = scrapper.create_response(region)
    extractor = Extractor()
    frame = extractor.extract_data(response)
    df = pd.DataFrame(frame[1:],columns=frame[0])
    plt.figure()
    sns.lineplot(data=df['Случаев заражения'])
    plt.show()
    
if __name__ == '__main__':
    window = Tk()
    window.title("Приложение для постройки графиков короновируса в РФ")
    window.geometry('700x700')
    combo = Combobox(window)
    regions = ('Санкт-Петербург', 'Москва')
    combo['values']=regions
    combo.grid(column=0, row=0)  
    btn = Button(window, text="Клик!", command=clicked)  
    btn.grid(column=1, row=0)  
    window.mainloop()