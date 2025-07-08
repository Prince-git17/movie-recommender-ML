import streamlit as st
import pickle
import requests

def fetch_poster(movie_title):
    response=requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey=63741676")
    data=response.json()
    if data['Response'] == 'True' and data['Poster']!='None':

        return data['Poster']
    else:#return placeholder image url
        return "https://www.bing.com/images/search?q=movie+poster+placeholder&id=42C25C09C6C8DD6C49BA2B518A65C87CF4DE9963&FORM=IQFRBA"
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from api
    for movie_title in recommended_movies:
        recommended_movies_posters.append(fetch_poster(movie_title))
    return recommended_movies,recommended_movies_posters
movies=pickle.load(open('movies.pkl','rb'))


similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Which Movie you would like to watch today!",
    movies['title'].values,
)

st.write("You selected:", selected_movie)

if st.button("Recommend"):
    names,posters=recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0], use_container_width=True)
        st.markdown(f"<div style='text-align:center'><strong>{names[0]}</strong></div>",
                    unsafe_allow_html=True)

    with col2:
        st.image(posters[1], use_container_width=True)
        st.markdown(f"<div style='text-align:center'><strong>{names[1]}</strong></div>",
                    unsafe_allow_html=True)

    with col3:
        st.image(posters[2], use_container_width=True)
        st.markdown(f"<div style='text-align:center'><strong>{names[2]}</strong></div>",
                    unsafe_allow_html=True)

    with col4:
        st.image(posters[3], use_container_width=True)
        st.markdown(f"<div style='text-align:center'><strong>{names[3]}</strong></div>",
                    unsafe_allow_html=True)

    with col5:
        st.image(posters[4], use_container_width=True)
        st.markdown(f"<div style='text-align:center'><strong>{names[4]}</strong></div>",
                    unsafe_allow_html=True)