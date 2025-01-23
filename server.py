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

#TODO: Fix chatacter ID and HTML
@app.route("/movie/<id>/quote")
def quotes(id):
    results = api_call(f"movie/{id}/quote")
    results = results["docs"]
    return render_template("quotes.html", results=results)

@app.route("/characters")
def characters():
    page = request.args.get('page', 1, type=int)
    results_per_page = 9  # Antall resultater per side

    results = api_call("character")
    results = results["docs"]  # Få resultatene fra API-kallet

    total_results = len(results)
    total_pages = (total_results + results_per_page - 1) // results_per_page
    
    # Hente ut den aktuelle siden med resultater
    start = (page - 1) * results_per_page
    end = start + results_per_page
    paged_results = results[start:end]

    # Beregn verdier for minimum og maksimum
    min_page = max(2, page - 1)  # Minimum side for visning
    max_page = min(page + 2, total_pages)  # Maksimum side for visning
    
    return render_template("characters.html", results=paged_results, page=page, total_pages=total_pages, min_page=min_page, max_page=max_page)


if __name__ == "__main__":
    app.run(debug = True)