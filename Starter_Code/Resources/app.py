# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
# Define the path to your SQLite database file
db_path = "sqlite:///hawaii.sqlite"
# Create the SQLAlchemy engine
engine = create_engine(db_path)
#################################################
# Database Setup
#################################################
# Database setup
Base = automap_base()
Base.prepare(autoload_with=engine)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#Route 1: Homepage
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation data<br/>"
        f"/api/v1.0/stations - List of stations<br/>"
        f"/api/v1.0/tobs - Temperature observations<br/>"
        f"/api/v1.0/start_date - Temperature statistics from start date<br/>"
        f"/api/v1.0/start_date/end_date - Temperature statistics from start date to end date"
    )
# Route 2: Precipitation data for the last 12 mo
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a session
    session = Session(engine)
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(func.max(Measurement.date)).scalar()
    if last_date:
        last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
        one_year_ago = last_date - dt.timedelta(days=365)
        # Query the last year of precipitation data
        results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
        # Convert the results to a dictionary
        precipitation_data = {date: prcp for date, prcp in results}
    else:
        precipitation_data = {"error": "No data found in the database"}
 # Close the session
    session.close()
    return jsonify(precipitation_data)

# Route 3: List of stations
@app.route("/api/v1.0/stations")
def stations():
    # Create a session
    session = Session(engine)
    # Query the list of stations
    results = session.query(Station.station, Station.name).all()
    # Convert the results to a list of dictionaries
    station_list = [{"Station": station, "Name": name} for station, name in results]
 # Close the session
    session.close()
    return jsonify(station_list)
# Route 4: Temperature observations for the most active station for the previous year
@app.route("/api/v1.0/tobs")
def tobs():
    # Create a session
    session = Session(engine)
    # Find the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count().desc()).first()[0]
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(func.max(Measurement.date)).filter(Measurement.station == most_active_station).scalar()
    last_date = dt.datetime.strptime(last_date, "%Y-%m-%d")
    one_year_ago = last_date - dt.timedelta(days=365)
    # Query temperature observations for the most active station in the last year
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station, Measurement.date >= one_year_ago).all()
    # Convert the results to a list of dictionaries
    tobs_data = [{"Date": date, "Temperature": tobs} for date, tobs in results]
    # Close the session
    session.close()
    return jsonify(tobs_data)
# Route 5: Temperature statistics for a specified start date
@app.route("/api/v1.0/<start>")
def temperature_stats_start(start):
    # Create a session
    session = Session(engine)
    # Query temperature statistics for dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    # Convert the results to a list of dictionaries
    temperature_stats = [{"Min Temperature": result[0], "Avg Temperature": result[1], "Max Temperature": result[2]} for result in results]
    # Close the session
    session.close()
    return jsonify(temperature_stats)
# Route 6: Temperature statistics for a specified start and end date
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats_start_end(start, end):
    # Create a session
    session = Session(engine)
    # Query temperature statistics for dates between start and end (inclusive)
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start, Measurement.date <= end).all()
    # Convert the results to a list of dictionaries
    temperature_stats = [{"Min Temperature": result[0], "Avg Temperature": result[1], "Max Temperature": result[2]} for result in results]
    # Close the session
    session.close()
    return jsonify(temperature_stats)
# Run the application if this script is the main module
if __name__ == "__main__":
    app.run(debug=True)

