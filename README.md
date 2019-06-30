# The repo contains Selenium-Python simple example - it tests a webpage title for specific contain and get a screenshot of the webpage.
## Requirements
### Install [Python](https://www.python.org/)
### Install PIP - a tool for installing and managing Python packages.
#### Clone the repo
```
git clone https://github.com/chavo1/selenium-python-scr.git
cd selenium-python-scr
```
#### Install Python package [selenium](https://pypi.org/project/selenium/)
```
pip install selenium
```
#### Just execute screenshot.py 
```
python3 screenshot.py
```
#### The test will check whether the page title contain [Consul](https://www.consul.io/) or [Google](https://www.google.com/).
#### The result from Python [unittest](https://docs.python.org/3/library/unittest.html) should be as follow:
```
selenium-python-scr (master) $ python3 screenshot.py 
testPageTitle (__main__.ConsulTestCase) ... ok
testPageTitle (__main__.GoogleTestCase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 15.981s

OK
```
#### If [unittest](https://docs.python.org/3/library/unittest.html) fails the particular python class will fail and screenshot for the web pages will not be saved.