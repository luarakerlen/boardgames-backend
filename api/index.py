from flask_openapi3 import OpenAPI, Info, Tag

app = OpenAPI(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'