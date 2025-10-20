#https://www.google.com/search?q=creating+a+personalized+response+to+a+form+on+html+and+python
#https://www.google.com/search?q=how+to+create+lists+on+python+for+detailed+form+app+questions+with+various+responses
#https://www.google.com/search?q=how+to+create+python+lists+with+responses+from+form
#https://www.google.com/search?q=creating+short+lists+for+form+questions+in+python
#https://www.google.com/search?q=creating+short+lists+for+form+questions+in+python
#https://www.google.com/search?q=how+to+create+for+if+statements+in+python+for+form
#https://www.google.com/search?q=how+to+create+if+not+return+in+python+for+a+form
#https://www.google.com/search?q=how+to+create+return+in+python+for+form+data
#https://www.google.com/search?q=how+to+create+if+return+in+python+with+data+from+form+response
#https://www.google.com/search?q=using+%40app.route+in+python+for+form
#https://www.google.com/search?q=using+def+in+python+for+if+return+and+return+statements+for+a+form
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

# Options for form selects
GENRES = ['Shoegaze', 'Metal', 'Emo']
LISTENED_OPTIONS = ['Pop', 'Classic Rock', 'Indie', 'Jazz', 'Hip-Hop', 'Electronic', 'Blues', 'Country']
MOODS = ['Calm', 'Energetic', 'Melancholic', 'Aggressive', 'Happy', 'Reflective']
INSTRUMENTS = ['Guitar', 'Synthesizer', 'Drums', 'Bass', 'Vocals', 'Piano', 'Electronic Sounds']
DECADES = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Artist recommendations database (simple example)
ARTIST_RECS = {
    'Shoegaze': [
        "Slowdive",
        "My Bloody Valentine",
        "Superheaven"
    ],
    'Metal': [
        "Cannibal Corpse",
        "Meshuggah",
        "Paleface Swiss"
    ],
    'Emo': [
        "Pierce the Veil",
        "Evanescence",
        "Sleeping With Sirens"
    ],
    'Calm': ["Bon Iver", "Beach House", "Sufjan Stevens"],
    'Energetic': ["Foo Fighters", "Metallica", "Paramore"],
    'Melancholic': ["Radiohead", "The National", "Joy Division"],
    'Aggressive': ["Slipknot", "Rage Against The Machine", "Bring Me The Horizon"],
    'Happy': ["Pharrell Williams", "Katy Perry", "Earth, Wind & Fire"],
    'Reflective': ["Nick Drake", "Leonard Cohen", "Elliott Smith"],
    'Guitar': ["Jimi Hendrix", "John Mayer", "Slash"],
    'Synthesizer': ["Depeche Mode", "Kraftwerk", "CHVRCHES"],
    'Drums': ["Led Zeppelin", "The Who", "Dave Grohl"],
    'Bass': ["Flea", "Geddy Lee", "Victor Wooten"],
    'Vocals': ["Freddie Mercury", "Adele", "Chris Cornell"],
    'Piano': ["Elton John", "Billy Joel", "Tori Amos"],
    'Electronic Sounds': ["Deadmau5", "Aphex Twin", "Daft Punk"],
    '1990s': ["Nirvana", "Alanis Morissette", "Green Day"],
    '2000s': ["Linkin Park", "Coldplay", "Evanescence"],
    '2010s': ["Imagine Dragons", "Billie Eilish", "Tame Impala"],
    '2020s': ["Olivia Rodrigo", "The Weeknd", "Dua Lipa"],
}

def recommend_artists(form_data):
    recs = set()

    # Recommend artists based on liked genres
    for genre in form_data.get('liked_genres', []):
        recs.update(ARTIST_RECS.get(genre, []))

    # Recommend artists based on mood
    mood = form_data.get('mood')
    if mood and mood in ARTIST_RECS:
        recs.update(ARTIST_RECS[mood])

    # Recommend artists based on favorite instrument
    instrument = form_data.get('instrument')
    if instrument and instrument in ARTIST_RECS:
        recs.update(ARTIST_RECS[instrument])

    # Recommend artists based on favorite decade
    decade = form_data.get('decade')
    if decade and decade in ARTIST_RECS:
        recs.update(ARTIST_RECS[decade])

    # Optionally, recommend based on compelling artists entered (basic matching)
    compelling_text = form_data.get('compelling_artists', '').lower()
    if compelling_text:
        # Simple keyword check for known artists in database (just a demo)
        for genre_artists in ARTIST_RECS.values():
            for artist in genre_artists:
                if artist.lower() in compelling_text:
                    recs.add(artist + " (because you mentioned them!)")

    if not recs:
        return ["Try exploring Shoegaze, Metal, or Emo genres!"]

    return sorted(recs)

@app.route("/", methods=['GET', 'POST'])
def home():
    recommendations = []
    form_data = {
        'liked_genres': [],
        'compelling_artists': '',
        'listened_genres': [],
        'mood': '',
        'instrument': '',
        'decade': '',
    }

    if request.method == 'POST':
        form_data['liked_genres'] = request.form.getlist('liked_genres')
        form_data['compelling_artists'] = request.form.get('compelling_artists', '').strip()
        form_data['listened_genres'] = request.form.getlist('listened_genres')
        form_data['mood'] = request.form.get('mood', '')
        form_data['instrument'] = request.form.get('instrument', '')
        form_data['decade'] = request.form.get('decade', '')

        recommendations = recommend_artists(form_data)

    return render_template(
        "home.html",
        genres=GENRES,
        listened_options=LISTENED_OPTIONS,
        moods=MOODS,
        instruments=INSTRUMENTS,
        decades=DECADES,
        recommendations=recommendations,
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(debug=True)
