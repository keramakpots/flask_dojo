from flask import Flask, request, render_template
from classes import Post


app = Flask(__name__, template_folder='templates')

@app.route('/request_counter', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        y = Post()
        x = Post.x
        y.safe_to_db()
        return render_template('index.html', x=x)
    else:
        y = Post()
        x = Post.x
        y.safe_to_db()
        return render_template('index.html', x=x)












if __name__ == '__main__':
    app.run(debug=True)
