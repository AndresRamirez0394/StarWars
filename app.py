import os
from flask import Flask
from services import list_movies, movie_characters

from flask import jsonify

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)


@app.route("/", methods=['GET'])
@app.route("/films", methods=['GET'])
def movielist():
    movies = list_movies()
    return jsonify(movies)

@app.route("/characters/<int:movie_id>", methods=['GET'])
def moviecharacters(movie_id):
    char_names = movie_characters(movie_id)
    return jsonify({"characters": char_names})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
