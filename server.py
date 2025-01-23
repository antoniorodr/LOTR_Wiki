from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from src.api import api_call

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books")
def books():
    results = api_call("book")
    results = results["docs"]
    return render_template("books.html", results = results)

@app.route("/book/<id>/chapter")
def chapter(id):
    results = api_call(f"book/{id}/chapter")
    results = results["docs"]
    return render_template("chapters.html", results=results)

@app.route("/movies")
def movies():
    results = api_call("movie")
    results = results["docs"][2:]
    return render_template("movies.html", results = results)

@app.route("/movie/<id>/quote")
def quotes(id):
    results = api_call(f"movie/{id}/quote")
    results = results["docs"]
    return render_template("quotes.html", results=results)

@app.route("/characters")
def characters():
    page = request.args.get("page", 1, type=int)
    results_per_page = 9
    results = api_call("character")
    results = results["docs"]
    total_results = len(results)
    total_pages = (total_results + results_per_page - 1) // results_per_page
    start = (page - 1) * results_per_page
    end = start + results_per_page
    paged_results = results[start:end]
    for character in paged_results:
        character["has_quotes"] = len(api_call(f"character/{character['_id']}/quote")["docs"]) > 0
    return render_template("characters.html", results=paged_results, page=page, total_pages=total_pages)

@app.route("/character/<id>/quote")
def char_quotes(id):
    results = api_call(f"character/{id}/quote")
    results = results["docs"]
    return render_template("char_quotes.html", results=results)


if __name__ == "__main__":
    app.run(debug = True)