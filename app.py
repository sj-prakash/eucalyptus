from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("search.html")

@app.route("/search")
def search():
    query = request.args.get("query")
    results = []
    if query:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
        response = requests.get(url)
        data = response.json()
        results = data.get("items", [])
    else:
        results = [] 
    return render_template("search.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)


