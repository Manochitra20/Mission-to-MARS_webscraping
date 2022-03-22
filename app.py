from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__,template_folder='templates')

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_scrape = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_scrape=mars_scrape)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    #mars_scrape = mongo.db.mars_scrape
    # Run the scrape function
    mars_scrape = scrape_mars.scrape_info()

    # Insert the record
    mongo.db.collection.update_one({}, {"$set": mars_scrape}, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)