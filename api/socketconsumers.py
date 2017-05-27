###############################################################################
# GazepointWebsockets: This project converts eye tracker data collected from a
# Gazepoint GP3 to simple JSON and then sends collected events to an
# experimentation platform, such as the Cybertrust phishing research platform,
# using websockets.
#
# Author: Matthew L. Hale
# Email: mlhale@unomaha.edu
# Copyright (C) 2017 Dr. Matthew L. Hale
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see http://www.gnu.org/licenses/.
# Based on PyOpenGaze by Edwin Dalmaijer (edwin.dalmaijer@psy.ox.ac.uk)
###############################################################################
import os
import time
import json
from GazepointAnalysis import GazepointWebsockets
import threading
from channels.sessions import channel_session
from api.models import *

@channel_session
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({
        "text": 'Starting Gazepoint',
    })
    message_json = json.loads(message.content['text'])
    # print message_json
    gazepoint_controller_thread = threading.Thread(target=startGazepoint)
    gazepoint_controller_thread.daemon = True
    gazepoint_controller_thread.start()
    print os.getpid()
    print 'Gazepoint controller starting...'
    time.sleep(3) # give it some time to start
    # message.channel_session['gazepoint_thread'] = t1
    message.channel_session['do_capture'] = True

    session = EyeTrackerSession.objects.all()
    try:
        # add type checking
        if session.first():
            session = session.first()
            session.args = message.channel_session

        else:
            print 'Creating session...'
            session = EyeTrackerSession(args=message.channel_session)
        session.save()
    except Exception as e:
        print e

    # print session.args['do_capture']
    print 'Starting Gazepoint data capture...'

    tracker = GazepointWebsockets(api_user=message_json['username'], socket=message, socketsend=message.reply_channel.send)

    # Calibrate the tracker.
    # tracker.calibrate()

    # Start recording data.
    tracker.start_recording()
    tracker.log("START=%d" % (round(time.time()*1000)))

    # Collect data for a bit.
    i=0
    while session.args['do_capture'] == True:
        session = EyeTrackerSession.objects.all().first()
        # print session.args['do_capture']
        tracker.log("STEP %d: %d" % (i+1, round(time.time()*1000)))
        print 'on: ' + str(i)
        i = i+1
        time.sleep(1.0)

    # Stop recording.
    tracker.log("STOP=%d" % (round(time.time()*1000)))
    tracker.stop_recording()
    tracker.close()
    print 'Gazepoint collection stopped...'
    print 'Killing Gazepoint Controller...'
    os.system("taskkill /im Gazepoint.exe")
    gazepoint_controller_thread.join()

@channel_session
def ws_disconnect(message):
    message.channel_session['do_capture'] = False
    print 'Gazepoint client socket disconnected: Stopping capture...'
    session = EyeTrackerSession.objects.all()
    try:
        # add type checking
        if session.first():
            session = session.first()
            session.args = message.channel_session

        else:
            print 'Creating session...'
            session = EyeTrackerSession(args=message.channel_session)
        session.save()
    except Exception as e:
        print e

def startGazepoint():
    try:
        os.system('\"C:\\Program Files (x86)\\Gazepoint\\Gazepoint\\bin\\Gazepoint.exe\"')
    except:
        print 'Error starting Gazepoint.'
