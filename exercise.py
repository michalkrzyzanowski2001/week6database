import sqlite3
from sqlite3 import Error
import sqlalchemy
from sqlalchemy import Table, Column, String, MetaData, FLOAT
from sqlalchemy import create_engine

engine = create_engine('sqlite:///stations.db')
meta = MetaData()
stations = Table(
   'stations', meta,
   Column('station', String, primary_key=True),
   Column('latitude', FLOAT),
   Column('longitude', FLOAT),
   Column('elevation', FLOAT),
   Column('name', String),
   Column('country', String),
   Column('state', String),
)
meta.create_all(engine)
conn = engine.connect()
ins = stations.insert()
conn.execute(ins, [
   {'station': 'USC00519397', 'latitude': 21.2716, 'longitude': -157.817, 'elevation': 3, 'name': 'WAIKIKI 717.2', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00513117', 'latitude': 21.4234, 'longitude': -157.802, 'elevation': 14.6, 'name': 'KANEOHE 838.1', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00514830', 'latitude': 21.5213, 'longitude': -157.837, 'elevation': 7, 'name': 'KUALOA RANCH HEADQUATERS 886.9', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00517948', 'latitude': 21.3924, 'longitude': -157.975, 'elevation': 11.9, 'name': 'PEARL CITY', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00518838', 'latitude': 21.4992, 'longitude': -158.011, 'elevation': 306.6, 'name': 'UPPER WAHAIAWA 874.3', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00519523', 'latitude': 21.33556, 'longitude': -157.711, 'elevation': 19.5, 'name': 'WAIMANALO EXPERIMENTAL FARM', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00519281', 'latitude': 21.45167, 'longitude': -157.849, 'elevation': 32.9, 'name': 'WAIHEE 837.5', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00511918', 'latitude': 21.3152, 'longitude': -157.999, 'elevation': 0.9, 'name': 'HONOLULU OBSERVATORY 702.2', 'country': 'US', 'state': 'HI'},
   {'station': 'USC00516128', 'latitude': 21.3331, 'longitude': -157.803, 'elevation': 152.4, 'name': 'MANOA LYON ABRO 785.2', 'country': 'US', 'state': 'HI'}])


