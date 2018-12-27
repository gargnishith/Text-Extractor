from flask import Flask, render_template, request, abort

app = Flask(__name__)

# ADD OTHER SUPPORTED EXTENSIONS BY THE OCR TOO
ALLOWED_EXTENSION = ['jpeg', 'jpg', 'png']

#CHECKS FOR A VALID INPUT FILE
def allowed(name):
   return ('.' in name) and (name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION)

#THE HOMEPAGE
@app.route('/')
def homepage():
	return render_template('homepage.html')

#HOMEPAGE SUBMITS THE FILE HERE
@app.route('/hidden', methods = ["POST", "GET"])
def hidden():
	if(request.method == "POST"):
		f = request.files['file']
		if(allowed(f.filename)):
			# CALL OCR SERVICE USING f
			a = 2
		else:
			abort(400)

#ERROR HANDLING FOR BAD INPUT
@app.errorhandler(400)
def bad_input(e):
	#CONTAINS LINK BACK TO HOMEPAGE
	return render_template('400.html', ext = ALLOWED_EXTENSION), 400

#ERROR HANDLING OF ERROR 404
@app.errorhandler(404)
def not_found(e):
	#CONTAINS A LINK BACK TO THE HOMEPAGE
	return render_template('404.html') , 404


if(__name__ == '__main__'):
	app.run(debug = True)

