from flask import Flask, render_template, request, abort
import io
import os
from google.cloud import vision

app = Flask(__name__)

# ADD OTHER SUPPORTED EXTENSIONS BY THE OCR TOO
ALLOWED_EXTENSION = ['jpg']

app.config['UPLOAD FOLDER'] = r'''C:\Users\Saurabh Gupta\Desktop\\'''

#CHECKS FOR A VALID INPUT FILE
def allowed(name):
   return ('.' in name) and (name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION)

#THE HOMEPAGE
@app.route('/')
def homepage():
    print("Main andar hoon!")
    return render_template('homepage.html')

#HOMEPAGE SUBMITS THE FILE HERE
@app.route('/output', methods = ["POST", "GET"])
def hidden():
    if(request.method == "POST"):
        f = request.files['file']
        if(allowed(f.filename)):
            path1 = app.config['UPLOAD FOLDER'] + f.filename
            f.save(os.path.join(app.config['UPLOAD FOLDER'], f.filename))
            client = vision.ImageAnnotatorClient.from_service_account_json(r'''C:\Users\Saurabh Gupta\Desktop\My First Project-80353a5f126d.json''')
            # [START vision_python_migration_text_detection]
            with io.open(path1, 'rb') as image_file:
                content = image_file.read()
            image = vision.types.Image(content=content)

            response = client.text_detection(image=image)
            texts = response.text_annotations
            return render_template('output.html', list = (texts[0].description).split('\n'))
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
