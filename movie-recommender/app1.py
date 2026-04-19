import streamlit as st
import pickle
import pandas as pd
import requests
from pympler.util.bottle import response


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    print(response)
    data = response.json()
    print(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_list = []
    recommended_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_list.append(movies.iloc[i[0]].title)
        recommended_poster.append(fetch_poster(movie_id))
    return recommended_list,recommended_poster
movies_list= pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender Systems')

option = st.selectbox('Movies list',movies['title'].values)

if st.button('Recommend'):
    recommended_list,recommended_poster = recommend(option)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_list[0])
        st.image(recommended_poster[0])
    with col2:
        st.text(recommended_list[1])
        st.image(recommended_poster[1])

    with col3:
        st.text(recommended_list[2])
        st.image(recommended_poster[2])
    with col4:
        st.text(recommended_list[3])
        st.image(recommended_poster[3])
    with col5:
        st.text(recommended_list[4])
        st.image(recommended_poster[4])
