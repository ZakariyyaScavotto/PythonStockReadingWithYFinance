from flask import Flask, render_template, make_response
import base64
import readApple, readDow, readFacebook, readGoogle, readTesla, readUber
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def navindex():
    return render_template('index.html')

@app.route('/apple.html')
def apple():
    return render_template('apple.html')

@app.route('/dowjones.html')
def dowjones():
    return render_template('dowjones.html')

@app.route('/facebook.html')
def facebook():
    return render_template('facebook.html')

@app.route('/google.html')
def google():
    return render_template('google.html')
    
@app.route('/tesla.html')
def tesla():
    return render_template('tesla.html')
    
@app.route('/uber.html')
def uber():
    return render_template('uber.html')
    

# script calls, based on https://stackoverflow.com/questions/63921787/display-image-from-flask-send-file-ajax-response-into-the-image-tag
@app.route('/apple/getApple')
def getApple():
    appleData = readApple.main()
    with open("apple.png", "rb") as f:
        image_binary = f.read()
        response = make_response(base64.b64encode(image_binary))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='image.png')
        return response

@app.route('/dowjones/getDow')
def getDow():
    dowData = readDow.main()
    with open("dow.png", "rb") as f:
        image_binary = f.read()
        response = make_response(base64.b64encode(image_binary))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='image.png')
        return response

@app.route('/facebook/getFacebook')
def getFacebook():
    facebookData = readFacebook.main()
    with open("facebook.png", "rb") as f:
        image_binary = f.read()
        response = make_response(base64.b64encode(image_binary))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='image.png')
        return response

@app.route('/google/getGoogle')
def getGoogle():
    googleData = readGoogle.main()
    with open("google.png", "rb") as f:
        image_binary = f.read()
        response = make_response(base64.b64encode(image_binary))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='image.png')
        return response

@app.route('/tesla/getTesla')
def getTesla():
    teslaData = readTesla.main()
    with open("tesla.png", "rb") as f:
        image_binary = f.read()
        response = make_response(base64.b64encode(image_binary))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='image.png')
        return response

@app.route('/uber/getUber')
def getUber():
    uberData = readUber.main()
    with open("uber.png", "rb") as f:
        image_binary = f.read()
        response = make_response(base64.b64encode(image_binary))
        response.headers.set('Content-Type', 'image/png')
        response.headers.set('Content-Disposition', 'attachment', filename='image.png')
        return response

app.run()