from django.shortcuts import render
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import requests
from django.conf import settings

# Load data and model at server start
csv_path = os.path.join(settings.BASE_DIR, 'Tmdb movie dataset(filtered).csv')
movies = pd.read_csv(csv_path, encoding='latin1')
cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vector)

TMDB_API_KEY = 'your_tmdb_api_key'

def get_poster_url(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0]['poster_path']
        full_poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_poster_url
    return ""

def get_recommendations(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = [(movies.iloc[i[0]].title, get_poster_url(movies.iloc[i[0]].title)) for i in distances[1:6]]
        return recommended_movies
    except IndexError:
        return [("Movie not found!", "")]

def index(request):
    movie_data = [{'title': title} for title in movies['title']]
    return render(request, 'recommender/index.html', {'movie_data': movie_data})

def recommend(request):
    if request.method == 'POST':
        movie = request.POST.get('movie')
        recommendations = get_recommendations(movie)
        selected_movie = {'title': movie, 'poster_url': get_poster_url(movie)}
        return render(request, 'recommender/recommend.html', {'recommendations': recommendations, 'selected_movie': selected_movie})
    return render(request, 'recommender/index.html')
