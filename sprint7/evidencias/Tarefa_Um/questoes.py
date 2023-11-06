def cal_actor_max_movies(atores):
    cal_actor_max_movies = atores[atores['Number of Movies'] == atores['Number of Movies'].max()].iloc[0]
    print(cal_actor_max_movies['Actor'], "tem o maior número de filmes", cal_actor_max_movies['Number of Movies'])

def avg_column_num_movies(atores):
    avg_column_num_movies = atores['Number of Movies'].mean()
    print("Média do número de filmes:", avg_column_num_movies)

def avg_movie_max_actor(atores):
    avg_movie_max_actor = atores[atores['Average per Movie'] == atores['Average per Movie'].max()].iloc[0]
    print("Ator/atriza com maior média por filme:", avg_movie_max_actor['Actor'])

def name_movie_max_freq(atores):
    movie_freq, num_freq  = atores['#1 Movie'].value_counts().idxmax(), atores['#1 Movie'].value_counts().max()
    print(movie_freq, "é o filme mais frequente aparecendo", num_freq, "vezes")