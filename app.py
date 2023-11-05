import streamlit as st 
import pickle
import requests
import pandas as pd
def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/51324?api_key=96a6b47f1cddc88ffc1d5695448230a0')
    data=response.json
    st.write(type(data))
    return "https://image.tmdb.org/t/p/w500" +data['poster_path']

def recommend(movie):
    movie_index= final_df[final_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True, key= lambda x: x[1])[1:6]
    l=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id= movie_names.iloc[i[0]].title
        # fetch poster from id
        recommended_movies_posters.append(fetch_poster(movie_id))

        l.append(final_df.iloc[i[0]].title)
    return l,recommended_movies_posters

final_df= pickle.load(open('movies.pkl','rb'))
movie_names=final_df.title.values
similarity= pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommender System")
selected_movie = st.selectbox(
    'Select a Movie Name :',
    (movie_names))

st.write('You selected:', selected_movie)

if st.button('Recommend'):
    recommend_movies_list,recommend_movies_poster=recommend(selected_movie)
    print(recommend_movies_poster)
    col1, col2, col3, col4, col5  = st.columns(5)

    with col1:
        st.header(recommend_movies_list[0])
        st.image(recommend_movies_poster[0])

    with col2:
        st.header(recommend_movies_list[0])
        st.image(recommend_movies_poster[0]) 

    with col3:
        st.header(recommend_movies_list[0])
        st.image(recommend_movies_poster[0])    
    
    with col4:
        st.header(recommend_movies_list[0])
        st.image(recommend_movies_poster[0])

    with col5:
        st.header(recommend_movies_list[0])
        st.image(recommend_movies_poster[0])