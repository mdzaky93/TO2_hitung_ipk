#Memanggil library Flask
from flask import Flask , request
from flask import render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

from flask_jwt_extended import JWTManager #Inisialisasi JWT

#email
from flask_mail import Mail

#backgroun task
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

#queue
import os
import redis
from rq import Queue

#Untuk menjelaskan nama modul 
# yang digunakan, 
#sehingga ketika folder lain 
# memanggil folder app
# otomatis teridentifikasi.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 
jwt = JWTManager(app)
mail = Mail(app)

r = redis.Redis()
q = Queue(connection=r)

# bagian upload file
UPLOAD_FOLDER = 'app/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# seeder
seeder = FlaskSeeder()
seeder.init_app(app, db)
# model
from app.model import mahasiswa, user

#Memanggil file routes 
# (akan segera dibuat)
from app.route import routes, routeUser, route_hitung_ipk
# from app.route import  uploadFile


# # Backgrountask example
# scheduler = BackgroundScheduler()

# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
#     # pass

# scheduler.add_job(func=print_date_time, trigger="interval", minutes=3)
# scheduler.start()

# # Shut down the scheduler when exiting the app
# atexit.register(lambda: scheduler.shutdown())







# Create a working task queue  
def background_task(n):
    try:
        """ Function that 
        returns len(n) and 
        simulates a delay """

        delay = 2

        print("Task running")
        print(f"Simulating a {delay} second delay")

        time.sleep(delay)

        print(len(n))
        print("Task complete")

        return len(n)
    except Exception as e:
        print(e)
    print(f"tes {n}")
    return "tes"



@app.route("/task")
def jj():
    # try:

        banyak = 0
        if request.args.get("n"):

            job = q.enqueue(background_task, request.args.get("n"))
            # banyak = len(q)
            return f"Task ({job.id}) added to queue at {job.enqueued_at}"
        banyak = len(q)
        return f"No value for count provided {banyak}"
    # except HorseMonitorTimeoutException as e:
        print(e)
