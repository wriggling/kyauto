from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return '<meta http-equiv="refresh" content="0; URL=https://phantom.is-a.dev/support"/>'

def run():
    app.run(host="162.220.253.253", port=45554)

def keep_alive():
    server = Thread(target=run)
    server.start()
