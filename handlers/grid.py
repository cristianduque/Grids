from tkinter import *
import sys


class Grid:

    coord = [[]]

    def __init__(self, horSize, verSize):
        self.horSize = horSize
        self.verSize = verSize

    def create(self):
        self.coord = [[0 for xCoord in range(self.horSize)] for yCoord in range(self.verSize)]

    def getHorizontalSize(self):
        return self.horSize

    def getVerticalSize(self):
        return self.verSize