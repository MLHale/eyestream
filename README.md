# Gazepoint2Json
This project coverts and time-synchronously integrates eye tracker data collected from a Gazepoint GP3 with a JSON-based experimentation platform API, such as the Cybertrust phishing research platform.

## Hardware Requirements
* Gazepoint GP3 HD (https://www.gazept.com/product-category/gp3-hd/)
* Gazepoint Control v3.5.0 +

## Software Requirements
* Python 2, >= 2.7.9 See: https://www.python.org/downloads
* python pip (https://pypi.python.org/pypi/pip)
* lxml (https://pypi.python.org/pypi/lxml/3.4.4)
* requests (http://docs.python-requests.org/en/master/)
* ntplib for time Synchronization (https://pypi.python.org/pypi/ntplib/) 
* PyOpenGaze (https://github.com/esdalmaijer/PyOpenGaze)

## Installation
### Hardware
Follow the GP3 setup guide, connecting the data USB port to a USB3 port.
Install the Gazepoint remote and control server using the Gasepoint Installer located here (https://www.gazept.com/downloads/), using valid access credentials provided with purchase of the GP3.

### Software
First install python and pip. Then:

```
pip install lxml
pip install requests
git clone https://github.com/MLHale/Cybertrust-gaze
cd Cybertrust-gaze
```

## Getting Started
Included in this project is an example script that works with the extended PyOpenGaze environment to not only log Gazepoint GP3 data locally, but also to log it to an API of your choice.

The example code issues a GET POST request using the requests library every time a sample is recorded by PyOpenGaze and the Gazepoint open API.

## License
Gazepoint2Json - coverts and time-synchronously integrates eye tracker data collected from a Gazepoint GP3 with a JSON-based experimentation platform API, such as the Cybertrust phishing research platform.

Copyright (C) 2017 Dr. Matthew L. Hale, unless otherwise indicated.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
