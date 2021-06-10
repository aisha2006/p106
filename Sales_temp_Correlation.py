import csv 
import plotly.express as px
import numpy as np

def showFig(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x = "Temperature", y= "Ice-cream Sales( â‚¹ )")
        fig.show()

def openPath(data_path):
    temp = []
    Icecream_sales = []
    with open(data_path)as f:
        with open("./data/IcecreamSales.csv") as f:
            df = csv.DictReader(f)
            for i in df:
                temp.append(float(i["Temperature"]))
                Icecream_sales.append(float(i["Ice-cream Sales( â‚¹ )"]))
    return {"x":temp,"y":Icecream_sales}

def getCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between temperature and ice cream sales: \n",correlation[0,1])

def setup():
    data_path = "./data/IcecreamSales.csv"
    data_source = openPath(data_path)
    getCorrelation(data_source)
    showFig(data_path)

setup()