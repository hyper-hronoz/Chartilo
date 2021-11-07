# Chartilo
## _Cool chart drawer for pyqt5 with candle support_

Chartilo is the open-source library which allow you to draw charts on qtpainter with support for lines, candles, bars or heiken-ashi.

- install library
- type 6 lines of python code
- enjoy result

## Features

- easy installation
- The ability to create your own drawing based modules on the current
- The ability to create your own color theme
- Scalable architecture

## Tech

Chartilo uses a number of open source projects to work properly:

- [PyQt5](https://pypi.org/project/PyQt5/) - HTML


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

First of all, you must have a qtframe in order to insert a painter there.

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

Second step is to create setting of library

```python
# this is how you can import drawers from chartilo library
from chartilo.drawers import GridDrawer, CandleChartDrawer, LineChartDrawer, LineDrawer, MaxMinValuesDrawer, Drawer
```
> Note: `Drawer` is required if you wanna build your own drawer.


```python
# this is how you can import models from chartilo library
from chartilo.models import Line, Candle
```
> Note: `models` is setting the type of vertexes and you can create your own models to draw them in your own drawers using base drawer class for calculation.
```python
# this is how you can import themes, the default is Dark
from chartilo.themes import Light, Dark, Theme
```
> Note: `Theme` is required if you wanna create your own theme.




this is how you can implement drawers, models, themes from chartilo library
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

The last step:

```python
		# setting data, states and running library
		self._chartilo.setData(data)
		self._chartilo.setStates(states)
		self._chartilo.updateCanvas()
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
