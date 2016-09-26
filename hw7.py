from netCDF4 import Dataset #access netcdf data
import os
import plotly.plotly as py
import plotly.graph_objs as go #use plotly

username = raw_input("Please enter your plotly username: ")
apikey = raw_input("Please enter your plotly API key: ")

py.sign_in(username, apikey)

with Dataset("/data/tmin.nc", "r") as tmin:
    tempMinJ = tmin.variables["tmin"][0]
    tempMinA = tmin.variables["tmin"][91]
    tempMinY = tmin.variables["tmin"][182]
    tempMinO = tmin.variables["tmin"][274] #min temps at certain days of year
#of course I would loop this through every day of the year if I wasn't just doing four for now...
#plot the heatmaps for tmin with the same zmin and zmax values
dataJ = [go.Heatmap(
    z = tempMinJ,
    zmin = -7,
    zmax = 27,
    )]

dataA = [go.Heatmap(
    z = tempMinA,
    zmin=-7,
    zmax=27,
    )]

dataY = [go.Heatmap(
    z = tempMinY,
    zmin=-7,
    zmax=27,
    )]

dataO = [go.Heatmap(
    z = tempMinO,
    zmin=-7,
    zmax=27,
    )]

py.image.save_as(dataJ, "dataJtmin.png")
py.image.save_as(dataA, "dataAtmin.png")
py.image.save_as(dataY, "dataYtmin.png")
py.image.save_as(dataO, "dataOtmin.png")
