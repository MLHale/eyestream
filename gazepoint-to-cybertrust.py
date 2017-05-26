import os
import time

from Gazepoint2JSON import Gazepoint2JSON

debug = True
tracker = Gazepoint2JSON(debug=debug, api_endpoint='http://localhost:8000/api/eyetrackerevents', api_user='1')

# Calibrate the tracker.
# tracker.calibrate()

# Start recording data.
tracker.start_recording()
tracker.log("START=%d" % (round(time.time()*1000)))

# Collect data for a bit.
for i in range(5):
    tracker.log("STEP %d: %d" % (i+1, round(time.time()*1000)))
    print 'on: ' + str(i)
    time.sleep(1.0)

# Stop recording.
tracker.log("STOP=%d" % (round(time.time()*1000)))
tracker.stop_recording()
tracker.close()
