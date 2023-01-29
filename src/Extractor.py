from unicodedata import normalize
from bs4 import BeautifulSoup
import requests
import pandas as pd
class Extractor:
    def __init__(self):
        pass

    def extract_num(self, data:str) -> int:
        data = data.replace(" ","")
        start = data.find('(')
        end = data.find(")")
        if start==end==-1:
            return int(data)
        else:
            return int(data[start+1:end])

    def extract_data(self,response:requests.Response) -> pd.DataFrame():
        soup = BeautifulSoup(response.text, "html.parser")
        stats = soup.find('table', {'class':'info-table'})
        counter = 1
        frame = []
        tmp = []
        for row in stats:
            if row.text=='\n':
                continue
            else:
                tmp.append(row)
        stats = tmp.copy()
        del(tmp)
        length = len(stats)
        limit = length
        i = 0
        for row in stats:
            if row.text=='\n':
                continue
            else:
                if counter == 1:
                    temp = row.find_all("th")
                    temp_2 = []
                    for ind in temp:
                        temp_2.append(ind.text)
                    data = [temp_2[0],temp_2[1],temp_2[2],temp_2[3],'id']
                else:
                    temp = row.find_all("td")
                    temp_2 = []
                    for ind in temp:
                        temp_2.append(ind.text)
                    data = [temp_2[0],self.extract_num(temp_2[1]), self.extract_num(temp_2[2]), self.extract_num(temp_2[3]),limit-i]

                frame.append(data)
                i+=1

            counter+=1
            if counter>limit:
                return pd.DataFrame(frame[1:],columns=frame[0])