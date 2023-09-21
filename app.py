# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Hitesh wadhwani" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def firstflask():
    return render_template("father.html",Relation="father",name="Jack",age="40")
# define the route to mother webpage
@app.route("/mother")
def seconflask():
    return render_template("mother.html",Relation="mother",name="kirti",age="38")

# define the route to friends webpage
@app.route("/friend")
def thirdflask():
    return render_template("friend.html",Relation="friend",name="Joy",age="13")

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
