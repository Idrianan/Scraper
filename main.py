from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def sanctify(data):
    data = data.replace(" ","")
    start = data.find('(')
    end = data.find(")")
    if start==end==-1:
        return int(data)
    else:
        return int(data[start+1:end])
URI = "https://gogov.ru/covid-19/spb#data"
headers = {
    'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
while True:
    try:
        response = requests.get(URI,headers=headers)
        break
    except:
        print(response)
        time.sleep(5)
#print(response)
soup = BeautifulSoup(response.text, "html.parser")
stats = soup.find('table', {'class':'info-table'})
#print(stats.prettify())
counter = 1
x = []
frame = []
print(len(stats))
adv_stats = []
for row in stats:
    if row.text=='\n':
        continue
    else:
        adv_stats.append(row)
stats = adv_stats
print(len(stats))
length = len(stats)
limit = length
for row in stats:
    if row.text=='\n':
        continue
    else:
        #print(row)
        if counter == 1:
            temp = row.find_all("th")
            temp_2 = []
            for ind in temp:
                temp_2.append(ind.text)
            data = [temp_2[0],temp_2[1],temp_2[2],temp_2[3]]
            print(data)
        else:
            temp = row.find_all("td")
            temp_2 = []
            for ind in temp:
                temp_2.append(ind.text)
            data = [temp_2[0],sanctify(temp_2[1]), sanctify(temp_2[2]), sanctify(temp_2[3])]
            #print(data)
        #print(temp)
        #print(len(temp))
        #for ind in temp:
        #    print(ind.text)
        frame.append(data)
    #x.append(row.text)
    #print(row.text)
    counter+=1
    if counter>limit:
        break
#print(frame)
tmp_frame = []
tmp_frame.append(frame[0])
for i in range(len(frame)-1):
    tmp_frame.append(frame[-i-1])
#print(tmp_frame)
df = pd.DataFrame(tmp_frame[1:],columns=tmp_frame[0])
#print(type(df))
#print(frame[0])
sns.lineplot(data=df['Случаев заражения'])
plt.show()