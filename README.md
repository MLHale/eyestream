# Eyestream: Gazepoint Websockets
This project converts eye tracker data collected from a Gazepoint GP3 to simple JSON and then sends collected events to an experimentation platform, such as the Cybertrust phishing research platform, using websockets.

## Hardware Requirements
* Gazepoint GP3 HD (https://www.gazept.com/product-category/gp3-hd/)
* Gazepoint Control v3.5.0 +

> Please note that due to the GP3 drivers and hardware APIs only supporting Windows, Eyestream only works on Windows. Eyestream was tested on Windows 10 enterprise edition (July 2018), but should work on any version of Windows 8 or above.

## Software Requirements
* Python 2, we suggest the python 2 LTS See: https://www.python.org/downloads
* python pip (https://pypi.python.org/pypi/pip)
<!-- * ntplib for time Synchronization (https://pypi.python.org/pypi/ntplib/) -->
* PyOpenGaze (https://github.com/esdalmaijer/PyOpenGaze)
* Django channels (https://github.com/django/channels), latest LTS 1.x.x version)
* Docker (https://www.docker.com)

> Please note that Eyestream is written for Python 2 and has not been tested for Python 3.

## Installation
### Hardware
Follow the GP3 setup guide, connecting the data USB port to a USB3 port.
Install the Gazepoint remote and control server using the Gasepoint Installer located here (https://www.gazept.com/downloads/), using valid access credentials provided with purchase of the GP3.

### Software
First install python, pip. and docker. 

> Note windows 10 pro, enterprise, and education users should use [docker desktop](https://docs.docker.com/docker-for-windows/install/), Windows 10 home users must install docker using [docker toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/). As part of the docker toolbox setup, you may also need to forward port 80 from the container to the host. To do so, open virtual box, click settings, click network, click advanced, click port forwarding, and then forward port 6379 from guest to host, using 127.0.0.1 as the host ip.

Then:

```
pip install django-picklefield
pip install pypiwin32
pip install channels==1.1.8
pip install asgi_redis
git clone https://github.com/MLHale/eyestream
docker pull redis
```

## Getting Started
```bash 
cd <path-to-eyestream>/scripts
start startserver.bat
```

This will start the websocket server to make it listen for incoming websocket creation requests.
:


## Basic Manual Testing


### Server starts when called upon to do so via websocket open message. 
#### Running the test: Starting a client-side websocket
The Gazepoint websocket server can be invoked using a client-side web socket invoked as follows:
```js
socket = new WebSocket("ws://" + window.location.host + "/gazepoint/");
socket.onmessage = function(event) {
    console.log(event.data);//log received messages
    //implement your client-side hooks here on event
}
socket.onopen = function() {
    //send username to server so it can append it to the generated tracker events
    socket.send(JSON.stringify({
  	username: 'testname'
    }));
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();
```
#### Expected outcomes
- Server process launchs the gazepoint hardware controller
- Server turns on the gazepoint device and beginning to stream captured eye data to the websocket which instantiated the channel.
* Start the gazepoint controller in its own thread.
* Initiate the eye tracker logging mechanisms and infinitely loop to capture eye events
* wait for the socket to close, at which point the loop terminates, the logger shuts down, and the gazepoint controller is killed.

### Server streams data captured by the hardware to open websocket clients
#### Running the test: inspect an open websocket using the prior onmessage function
Using a browser opened in the same session as the websocket client launching code from the prior test, open the developer console tab. Develop Console in chrome can be launched via the Ctrl+Shift+J hotkey (on Windows).

#### Expected outcomes
- server streams data captured by the hardware to the websocket client as long as the websocket is open
- valid hardware events will contain eyetracker telemetry information


### server ends a session when called upon to do so via a websocket close event or if the websocket times out.
#### Running the test: send end event
To end the websocket and terminate, from the same browser opened to the developer console, invoke the following code:
```js
socket.close()
```

#### Expected outcomes
- Data collection terminates
- Websocket handling process gracefully shuts down the eye tracker hardware and controller, join the threads supporting the data capture process, and end server processing related to the websocket.

## License
Eyestream: Converts and serializes eye tracker data collected from a Gazepoint GP3 into a simple JSON format before streaming it to an application of choice at frequencies of up to 150hz. Eyestreams works for a variety of real-time eye tracker needs such as eye-driven UI, experimentation platforms, or medical apps.

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
