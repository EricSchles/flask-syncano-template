from flask import Flask, render_template, request
import os
import datetime
from syncano import client
SyncanoApi = client.SyncanoApi
app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
	if request.headers.getlist("X-Forwarded-For"):
   		ip = request.headers.getlist("X-Forwarded-For")[0]
	elif request.access_route:
		ip = request.access_route
	else:
   		ip = request.remote_addr
	syncano = SyncanoApi("white-sun-672290","92f4c3ae210cee23a24c03f892574fa9957cdf30")
	project_id = "3964"
	collection_id = "12784"
	syncano.data_new(project_id,collection_id=collection_id,title=ip,text=str(datatime.datetime.now()))
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)
