"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chab3uak728r887t0mh0-a.oregon-postgres.render.com",
        database="todo_9fvg",
        user="todo_9fvg_user",
        password="PdElfE1FENlvB9g007ucyvUi3ty5btCh")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
