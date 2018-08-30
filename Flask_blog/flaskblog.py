from flask import Flask,render_template,url_for

app=Flask(__name__)

posts=[
{
	'author':'Rakshit Malhotra',
	'title':'Purchase a 1 bhk in boston',
	'content':'1st post content',
	'date_posted':'30-August-2018',
},
{
	'author':'Adit kumar pabbi',
	'title':'Purchase a 1 bhk ',
	'content':'2nd post content',
	'date_posted':'31-August-2018',
}


]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title='About')

if  __name__ =='__main__':	
	app.run(debug=True)

