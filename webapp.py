from flask import Flask, render_template, request

app = Flask(__name__)

# Existing genre routes
@app.route("/shoegaze")
def shoegaze():
    return render_template("page1.html")

@app.route("/metal")
def metal():
    return render_template("page2.html")

@app.route("/emo")
def emo():
    return render_template("page3.html")

# Constants for form options
GENRES = ['Shoegaze', 'Metal', 'Emo']
LISTENED_OPTIONS = ['Pop', 'Classic Rock', 'Indie', 'Jazz', 'Hip-Hop', 'Electronic']

def recommend_artists_or_genres(liked_genres, listened_genres):
    recommendations = []

    if liked_genres:
        recommendations.extend([f"Check out more {genre} artists!" for genre in liked_genres])
    else:
        main_six = ['Pop', 'Classic Rock', 'Indie', 'Jazz', 'Hip-Hop', 'Electronic']
        intersection = set(listened_genres).intersection(main_six)
        if intersection:
            for genre in intersection:
                recommendations.append(f"You might enjoy exploring more {genre} music.")
        else:
            recommendations.append("Explore other genres like Blues, Country, or World Music!")

    return recommendations

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        liked_genres = request.form.getlist('liked_genres')
        compelling_artists = request.form.get('compelling_artists')  # Currently not used in recommendations
        listened_genres = request.form.getlist('listened_genres')

        recommendations = recommend_artists_or_genres(liked_genres, listened_genres)

        return render_template("home.html",
                               genres=GENRES,
                               listened_options=LISTENED_OPTIONS,
                               recommendations=recommendations)
    else:
        return render_template("home.html",
                               genres=GENRES,
                               listened_options=LISTENED_OPTIONS,
                               recommendations=None)

if __name__ == "__main__":
    app.run(debug=True)
