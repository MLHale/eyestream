###############################################################################
# Gazepoint2Json: coverts and time-synchronously integrates eye tracker data
# collected from a Gazepoint GP3 with a JSON-based experimentation platform API,
# such as the Cybertrust phishing research platform..
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
import json
import requests

from opengaze import OpenGazeTracker

class Gazepoint2JSON(OpenGazeTracker):
    def __init__(self, ip='127.0.0.1', port=4242, logfile='default.tsv', \
		debug=False, api_user='', api_password='', api_endpoint='http://localhost:8000/api/'):
        OpenGazeTracker.__init__(self, ip, port, logfile, debug)
        self._api_user = api_user
        self._api_endpoint = api_endpoint
        r = requests.post(self._api_endpoint+'session/', {'username':api_user,'password':api_password})
        print r.json()
        self._cookies = r.cookies
    # Accepts a sample as a list of keys and returns a JSON object
    def sampleToJSON(self, sample):
        # append apiuser variable
        sample['apiuser'] = self._api_user
        return json.dumps(sample, sort_keys=True, ensure_ascii=True,)

    # Method is invoked by a PyOpenGaze logging thread to process an incoming sample data point from the Gazepoint API
    # Overridden to convert to JSON and issue a corresponding API request
    def _log_sample(self, sample):
        json_sample = self.sampleToJSON(sample);
        self.POSTSample(json_sample)
        # Sample is a dictionary of key/value pairs gathered from the Gazepoint API server

        # for varname in sample.keys():
		# 	# Check if this is a logable variable.
		# 	if varname in self._logheader:
		# 		# Find the appropriate index in the line
		# 		line[self._logheader.index(varname)] = sample[varname]
		# self._logfile.write('\t'.join(line) + '\n')

    # Issue POST request with given data, to the specified API
    def POSTSample(self, json_obj):
        if self._debug:
            print 'Sending Request to: ' + self._api_endpoint+'eyetrackerevents/eyetrackerintegration'  + '\n'
            # print json_obj
        try:
            r = requests.post(self._api_endpoint+'eyetrackerevents/eyetrackerintegration', data=json_obj, cookies=self._cookies, headers={'Content-Type': 'application/json'})
            print r.text
            print '---------------------------------------------\n'
        except Exception as e:
            print e
