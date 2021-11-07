import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
	name='dokr',  
	version='0.1',
	scripts=['dokr'] ,
	author="Vladislav Moryakov",
	author_email="vlad_moryakov_prog@mail.ru",
	description="library for offset in yandexlyceum, which allows you to build graphs in linear and candlestick form, with a scalable architecture",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/hyper-hronoz/Chartilo",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
 )