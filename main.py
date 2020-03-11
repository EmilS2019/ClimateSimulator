import xlsxwriter
from simulation import PlanetaryGrid
from excel import printGrid

grid = PlanetaryGrid(x=25,y=25,z=4,tempAmplitude=22.0,baseTemp=3.0)
book = xlsxwriter.Workbook("out.xlsx")

#Runs the simulation for b time ticks
b = 20
for _ in range(b):
    printGrid(book, grid)
    grid.tiles = grid.timeStep()

book.close()