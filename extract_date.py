def extract_date(data):
    data = data.replace(" ","")
    start = data.find('(')
    end = data.find(")")
    if start==end==-1:
        return int(data)
    else:
        return int(data[start+1:end])