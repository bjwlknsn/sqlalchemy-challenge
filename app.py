import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import datetime as dt

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station


app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Available Routes:<br/><br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/2016-08-23'>/api/v1.0/&lt;start date &gt;</a> use date format:YYYY-MM-DD <br>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/2016-08-23/2017-08-23'>/api/v1.0/&lt;start date &gt;/&lt;end date&gt;</a> use date format:YYYY-MM-DD"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date = dt.date(2017, 8 ,23)
    year_ago = last_date - dt.timedelta(days=365)
    session = Session(engine)
    date_prcp = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date.between(year_ago, last_date)).all()
    session.close()
    date_precipitation = {date: prcp for date, prcp in date_prcp}
    return jsonify(date_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    all_stations = session.query(Station.station).all()
    session.close()
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    last_date = dt.date(2017, 8 ,23)
    year_ago = last_date - dt.timedelta(days=365)
    session = Session(engine)
    date_tobs = session.query(Measurement.tobs).\
        filter(Measurement.station == "USC00519281").\
        filter(Measurement.date.between(year_ago, last_date)).all()
    session.close()
    return jsonify(date_tobs)

@app.route("/api/v1.0/<start>")
def start(start = None):
    last_date = dt.date(2017, 8 ,23)
    session = Session(engine)
    tobs_start_only = session.query(Measurement.tobs).filter(Measurement.date.between(start, last_date)).all()
    session.close()
    tobs_start_only_df = pd.DataFrame(tobs_start_only)
    tmin = tobs_start_only_df["tobs"].min()
    tmax = tobs_start_only_df["tobs"].max()
    tavg = tobs_start_only_df["tobs"].mean()
    return jsonify(tmin, tmax, tavg)

@app.route("/api/v1.0/<start>/<end>")
def startend(start = None, end = None):
    session = Session(engine)
    tobs_start_only = session.query(Measurement.tobs).filter(Measurement.date.between(start, end)).all()
    session.close()
    tobs_start_only_df = pd.DataFrame(tobs_start_only)
    tmin = tobs_start_only_df["tobs"].min()
    tmax = tobs_start_only_df["tobs"].max()
    tavg = tobs_start_only_df["tobs"].mean()
    return jsonify(tmin, tmax, tavg)

if __name__ == "__main__":
    app.run(debug=True)