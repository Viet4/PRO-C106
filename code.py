import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path, x, y):
    Xvalue = []
    Yvalue = []

    with open(data_path) as f:
        df = csv.DictReader(f)
        
        for row in df:
            Xvalue.append(float(row[x]))
            Yvalue.append(float(row[y]))
    
    return{"x": Xvalue, "y": Yvalue}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def plotFigure(data_path, Xvalue, Yvalue):
    with open(data_path) as f:
        df = csv.DictReader(f)
    
        fig = px.scatter(df, x=Xvalue, y=Yvalue)
        fig.show()

def setup():
    data_path = input("Enter data path: ")
    x = input("Enter X value: ")
    y = input("Enter Y value: ")
    data_source = getDataSource(data_path, x, y)
    findCorrelation(data_source)
    plotFigure(data_path, x, y)

setup()

# cups of coffee vs hours of sleep.csv
# Coffee in ml
# sleep in hours

# Student Marks vs Days Present.csv
# Marks In Percentage
# Days Present
