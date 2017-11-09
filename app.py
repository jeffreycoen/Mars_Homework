from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

conn = "mongodb://admin:tester@ds243335.mlab.com:43335/heroku_kj4scs6n"
client = PyMongo.mongo(conn)
db = client.heroku_kj4scs6n
mars = db.new_collection


@app.route("/")
def index():
    listings = mongo.db.mars.find_one()
    return render_template("index.html", mars_listings=mars_listings)


@app.route("/scrape")
def scrape():
    listings = mongo.db.listings
    listings_data = scrape_mars.scrape()
    listings.update(
        {},
        listings_data,
        upsert=True
    )
    return index


if __name__ == "__main__":
    app.run(debug=True)