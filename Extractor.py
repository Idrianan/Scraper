from unicodedata import normalize
from bs4 import BeautifulSoup
from extract_date import extract_date
import requests

class Extractor:
    def __init__(self):
        pass
    def extract_data(self,response:requests.Response) -> list:
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
        for row in stats:
            if row.text=='\n':
                continue
            else:
                if counter == 1:
                    temp = row.find_all("th")
                    temp_2 = []
                    for ind in temp:
                        temp_2.append(ind.text)
                    data = [temp_2[0],temp_2[1],temp_2[2],temp_2[3]]
                else:
                    temp = row.find_all("td")
                    temp_2 = []
                    for ind in temp:
                        temp_2.append(ind.text)
                    data = [temp_2[0],extract_date(temp_2[1]), extract_date(temp_2[2]), extract_date(temp_2[3])]

                frame.append(data)

            counter+=1
            if counter>limit:
                return self.normilize_frame(frame)

    def normilize_frame(self,frame:list) -> list:
        tmp_frame = []
        tmp_frame.append(frame[0])
        for i in range(len(frame)-1):
            tmp_frame.append(frame[-i-1])
        return tmp_frame