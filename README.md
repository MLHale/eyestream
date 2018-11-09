# Eyestream: Gazepoint Websockets
This project converts eye tracker data collected from a Gazepoint GP3 to simple JSON and then sends collected events to an experimentation platform, such as the Cybertrust phishing research platform, using websockets.

## Hardware Requirements
* Gazepoint GP3 HD (https://www.gazept.com/product-category/gp3-hd/)
* Gazepoint Control v3.5.0 +

## Software Requirements
* Python 2, >= 2.7.9 See: https://www.python.org/downloads
* python pip (https://pypi.python.org/pypi/pip)
<!-- * ntplib for time Synchronization (https://pypi.python.org/pypi/ntplib/) -->
* PyOpenGaze (https://github.com/esdalmaijer/PyOpenGaze)
* Django channels (https://github.com/django/channels)
* Docker (https://www.docker.com)

## Installation
### Hardware
Follow the GP3 setup guide, connecting the data USB port to a USB3 port.
Install the Gazepoint remote and control server using the Gasepoint Installer located here (https://www.gazept.com/downloads/), using valid access credentials provided with purchase of the GP3.

### Software
First install python, pip. and docker. Then:

```
pip install pypiwin32
pip install channels
pip install asgi_redis
git clone https://github.com/MLHale/gazepoint-websockets
cd gazepoint-web-socket-backend
docker pull redis
```

## Getting Started
```bash
docker run -it -p 6379:6379 redis
daphne chat.asgi:channel_layer --port 8888
python manage.py runworker
```

## Starting a client-side websocket
The Gazepoint websocket server can be invoked using a client-side web socket invoked as follows:

```js
socket = new WebSocket("ws://" + window.location.host + "/gazepoint/");
socket.onmessage = function(e) {
    console.log(e.data);//log received messages
		//implement your client-side hooks here on e
}
socket.onopen = function() {
		//send username to server so it can append to the generated tracker events
		socket.send(JSON.stringify({
  		username: 'testname'
		}));
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();
```

This will start the websocket server process to:
* Start the gazepoint controller in its own thread.
* Initiate the eye tracker logging mechanisms and infinitely loop to capture eye events
* wait for the socket to close, at which point the loop terminates, the logger shuts down, and the gazepoint controller is killed.

## License
Eyestream: Gazepoint Websockets converts eye tracker data collected from a Gazepoint GP3 to simple JSON and then sends collected events to an experimentation platform, such as the Cybertrust phishing research platform, using websockets.

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
