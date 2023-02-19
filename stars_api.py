from flask import Flask, jsonify, request;
from data import data

#creating an app object out of the flask class
app = Flask(__name__)

#app.route specifies the endpoint that user opens on the browser
@app.route("/")
def index():
    #this will return data to browser and display it
    #using jsonify because data is returned in json format
    return jsonify({
        "data":data,
        "message":"success"
    }),200

#to get a specific planet
@app.route("/star")
def star():
    #this is used to get the name from the user
    name = request.args.get("name")
    #next function is used to create and iterate and find a dictionary
    #here it should satisfy the condition, which is the name should match
    star_data = next(item for item in data if item["name"]==name)
    #this will return data to browser and display it
    #using jsonify because data is returned in json format
    return jsonify({
        "data":star_data,
        "message":"success"
    }),200

if __name__ == '__main__':
    app.run()
    