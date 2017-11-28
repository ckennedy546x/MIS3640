"""
Simple "Hello, World" application using Flask
"""

from flask import Flask, render_template, request
from mbta_helper import get_lat_long, get_nearest_station, find_stop_near
app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/neareststation/', methods=['GET, POST'])
def nearStation():
    if request.method == 'POST':
        address = str(request.form['address'])
        latitude, longitude = get_lat_long(address)
        stop_name, distance = find_stop_near(address)


        return render_template('station_result.html', address=address)
    return render_template('address_form.html', error=None)
if __name__ == '__main__':
    app.run()
