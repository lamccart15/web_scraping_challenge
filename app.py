# Import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create instance of Flask app
app = Flask(__name__)

# Establish Mongo connection
uri="mongodb://localhost:27017/mars_db"
mongo=PyMongo(app, uri=uri)

# Create route that renders index.html template
@app.route('/')
def index(): 
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", data=mars_data)

@app.route('/scrape')
def scrape(): 

    #Run scrape function
    post = scrape_mars.scrape_info()

    # Update Mongo database using update and upsert=True
    mongo.db.mars_data.update({}, post, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)