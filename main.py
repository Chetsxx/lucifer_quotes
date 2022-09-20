import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/random_quote", methods=['GET', 'POST'])
def quote():
    get_quote = True
    while get_quote:
        response = requests.get(url='https://lucifer-quotes.vercel.app/api/quotes')
        data = response.json()
        for dic in data:
            quote = dic["quote"]
            author = dic["author"]
        return render_template('q.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)