from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Come\nCome\nCome\nCome\nCome\nCome\nCome\nwe have posessed CafeBot<br>Hi uh I guess we need to chat here now lolol but uhh what else should we add to the footer I made 4 servers in 1 day I don't think they gonne join CafeBot Support anyways but eh idk"

def run():
    app.run(host="0.0.0.0", port="8080")

def keep_alive():
    server = Thread(target=run)
    server.start()