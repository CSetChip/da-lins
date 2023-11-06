import pandas as pd
from questoes import *

def gatilho():
    cal_actor_max_movies(atores)
    avg_column_num_movies(atores)
    avg_movie_max_actor(atores)
    name_movie_max_freq(atores)

if __name__ == "__main__":

    atores = pd.read_csv("actors.csv")
    gatilho()
    print("\n****Consultas Finalizadas ****")

    