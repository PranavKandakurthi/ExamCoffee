#Correlation between marks of the students vs their attendance
import plotly. express as px
import csv

with open("exam.csv") as csv_file:
  df = csv.DictReader(csv_file)
  fig = px.scatter(df,x="Marks In Percentage", y="Days Present",)
fig.show()

import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Marks In Percentage"]))
            cold_drink_sales.append(float(row["Days Present"]))

    return {"x" : ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between marks of the students vs their attendance :-  \n--->",correlation[0,1])

data_path  = "exam.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)

#Correlation between coffee consumed vs their sleep duration
import plotly. express as px
import csv

with open("coffee.csv") as csv_file:
  df = csv.DictReader(csv_file)
  fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
fig.show()

import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Coffee in ml"]))
            cold_drink_sales.append(float(row["sleep in hours"]))

    return {"x" : ice_cream_sales, "y": cold_drink_sales}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee consumed vs their sleep duration :-  \n--->",correlation[0,1])

data_path  = "coffee.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)