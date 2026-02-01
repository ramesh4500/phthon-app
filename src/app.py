#!/usr/bin/env python3
# The api end points used in the application are defined below.
#'api/v1/details' = To get the details of the application
#'api/v1/healthz' = To get the health status of the application

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask, jsonify
# Additional module for getting current time
import datetime 
import socket
# Flask constructor takes the name of 
# current module (__name__) as argument.

app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/api/v1/details')
# ‘/api/v1/details’ URL is bound with details() function.
def details():
#   return jsonify({
#        'time': datetime.datetime.now().strftime("%I:%M:%S:%p on %B %d, %Y"),
    now = datetime.datetime.now()
    # Format the time as H:M:S (24-hour format)
    # Use %I:%M:%S %p for 12-hour format with AM/PM
    current_time = datetime.datetime.now().strftime("%I:%M:%S:%p on %B %d, %Y") 
    return jsonify({
        'time': current_time,
        'hostname': socket.gethostname()
        'message': "Your Application is running great"
    })

@app.route('/api/v1/healthz')
# ‘/api/v1/details’ URL is bound with health() function.
def health():
    return jsonify({'status': "OK"}), 200

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
     app.run(host="0.0.0.0")
     
