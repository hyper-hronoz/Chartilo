import sys

from PyQt5.QtWidgets import QApplication, QBoxLayout, QMainWindow, QVBoxLayout, QWidget
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from chartilo import Chartilo

from chartilo.drawers import GridDrawer, CandleChartDrawer, LineChartDrawer

from ast import literal_eval

from chartilo.drawers.lineDrawer import LineDrawer
from chartilo.drawers.maxMinValuesDrawer import MaxMinValuesDrawer
from chartilo.models import Line, Candle
from chartilo.themes import Light, Dark


class MyWidget(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('untitled.ui', self)

		# adding canvas to frame
		self._chartilo = Chartilo()
		layout = QVBoxLayout()
		layout.addWidget(self._chartilo)
		self.frame.setLayout(layout)

		# setting states
		states = {
			"type" : Candle, 
			"theme": Dark,
			"drawers" : {
				"grid" : GridDrawer,
				"lineChart" : CandleChartDrawer,
				"line" : LineDrawer,
				"maxMinDrawer" : MaxMinValuesDrawer
			},
		}

		# getting data
		file = open("data.txt", "r")
		data = literal_eval(file.read())

		# setting data, states and running library
		self._chartilo.setData(data)
		self._chartilo.setStates(states)
		self._chartilo.updateCanvas()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWidget()
	ex.show()
	sys.exit(app.exec_())

