from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/resume', methods=['GET'])
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)