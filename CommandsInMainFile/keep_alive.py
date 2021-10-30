"""
This should only be needed if you are using replit.com and uptimerobot.com
"""
from flask import Flask
from threading import Thread

app = Flask("My Discord.py Bot")

@app.route("/")
def home():
  return "This bot now has hosting!"
def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()
