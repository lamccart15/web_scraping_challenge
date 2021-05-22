# Import libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape_info

# Create instance of Flask app
app = Flask(__name__)

# Establish Mongo connection
uri="mongodb://localhost:27017/mars"
mongo=PyMongo(app, uri=uri)

# Create route that renders index.html template
@app.route('/')
def index(): 
    post = db.posts.find_one({})
    return render_template("index.html", post=post)

@app.route('/scrape')
def scrape(): 

    #Run scrape function
    post = scrape()

    # Update Mongo database using update and upsert=True
    mongo.db.post.update({}, post, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)