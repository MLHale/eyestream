import os
import time
import json
from GazepointAnalysis import Gazepoint2JSON
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

    tracker = Gazepoint2JSON(api_user=message_json['username'], socket=message, socketsend=message.reply_channel.send)

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
