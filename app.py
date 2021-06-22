from flask import Flask
from flask import redirect
from waitress import serve
import pandas as pd

from datetime import datetime


LOG_FILE = ("log.csv")
app = Flask(__name__)

@app.route("/")
def index():
        return "<p>root path</p>"

@app.route("/code/<id>")
def codeScanned(id):
     
        #record time stamp.
        now = datetime.now()
        timestampStr = now.strftime("%H:%M:%S.%f - %b %d %Y")

        #record code.
        code = id

        #create log.
        log = "{c}, {t}\n".format(t=timestampStr, c=code)

        #log to file.
        f = open(LOG_FILE, "a")
        f.write(log)
        f.close()

        #Redirect to information page.
        return redirect("https://bondplaneteers2021.wixsite.com/bond-planeteers", code=302)

@app.route("/log")
def viewLogs():
        
        #read file
        columns = ['code', 'timestamp']
        df = pd.read_csv(LOG_FILE, names=columns)
        tableHtml = df.to_html()
        return tableHtml

#if __name__ == "__main__":
        #serve(app, host='0.0.0.0', port=8080)
