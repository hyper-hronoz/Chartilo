# Chartilo
## _Cool chart drawer for pyqt5 with candle support_

Chartilo is the open-source library which allow you to draw charts on qtpainter with support for lines, candles, bars or heiken-ashi.

- install library
- type 17 lines of python code
- enjoy result

## Features

- easy installation
- The ability to create your own drawing based modules on the current
- The ability to create your own color theme
- Scalable architecture

## Tech

Chartilo uses a number of open source projects to work properly:

- [PyQt5](https://pypi.org/project/PyQt5/) - app build framework


And of course Chartilo itself is open source with a [public repository](https://github.com/hyper-hronoz/Chartilo)
 on GitHub.

## Installation

Chatrilo requires [python](https://www.python.org/) v3+ to run.



If you didn't install PyQt5...

```sh
pip install pyqt5
```

Install the dependency.

```sh
pip install chartilo
```



## Development

Ready to code? Great!

Make a change in your file and instantaneously see your updates!

Open your favorite code editor and paste these code lines.

The base sctructure likes this, you can browse demo version [here](https://github.com/hyper-hronoz/test_my_library_yandexlyceum)

```python
import sys

from PyQt5.QtWidgets import QApplication, QBoxLayout, QMainWindow, QVBoxLayout, QWidget
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow

from chartilo import Chartilo

from chartilo.drawers import GridDrawer, CandleChartDrawer, LineChartDrawer, LineDrawer, MaxMinValuesDrawer

from ast import literal_eval

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


```

First of all, you must have a qtframe in order to insert a painter there:

```python
class MyWidget(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('uifile.ui', self)

		# adding painter to frame
		self._chartilo = Chartilo()
		layout = QVBoxLayout()
		layout.addWidget(self._chartilo)
		self.frame.setLayout(layout)

```




Second step is to create setting of library:

this is how you can implement drawers, models, themes from chartilo library:
```python
		# setting states
		states = {
			"type" : Candle, # the type of chart(liner or candler)
			"theme": Dark, # theme of chart (light or dark)
			"drawers" : {
				"grid" : GridDrawer, # class is used to draw grid for chart
				"lineChart" : CandleChartDrawer, # class is used to draw candles
				"line" : LineDrawer, # showing curren price line
				"maxMinDrawer" : MaxMinValuesDrawer # showing maximum and minimum of chart
			},
		}
```
> Note: `Type of vertexes and type of vertexes darwer` should be same for proper work.
> Note: `you can remove some of the classes to get the functionality you want`


```python
# this is how you can import drawers from chartilo library
from chartilo.drawers import GridDrawer, CandleChartDrawer, LineChartDrawer, LineDrawer, MaxMinValuesDrawer, Drawer
```
> Note: `Drawer` is required if you wanna build your own drawer.


```python
# this is how you can import models from chartilo library:
from chartilo.models import Line, Candle
```
> Note: `models` is setting the type of vertexes and you can create your own models to draw them in your own drawers using base drawer class for calculation.

this is how line generates

```python
class Line:
	width = 8 

	def __init__(self, data):
		self.closeTime = data[0] # NOT REQUIRED close time
		self.openPrice = float(data[1]) # open price
		self.closePrice = float(data[4]) # close price
```

this is how candle generates


```python
from . import Line


class Candle(Line):
	width = 8 

	def __init__(self, data):
		super().__init__(data); # open and close price look above
		self.maximalPrice = float(data[2]) # maximal price
		self.minimalPrice = float(data[3]) # minimal price
```

```python
# this is how you can import themes, the default is Dark
from chartilo.themes import Light, Dark, Theme
```
> Note: `Theme` is required if you wanna create your own theme.

The last step:

```python
		# setting data, states and running library
		self._chartilo.setData(data)
		self._chartilo.setStates(states)
		self._chartilo.updateCanvas()
```
> Note: `data` must be a two-dimensional array [[closeTime, openPrice, maximalPrice, minimalPrice, closePrice], [closeTime, openPrice, maximalPrice, minimalPrice, closePrice]] example [here](https://github.com/hyper-hronoz/test_my_library_yandexlyceum/blob/master/data.txt) another fields are not required yet.

*This is all have a nice day*

if this is not enougth you can browse crypto-meneger-project [here](https://github.com/seldish-og/Crypto-Manager-Desktop-App)

## License

MIT

**Free Software, Hell Yeah!**
