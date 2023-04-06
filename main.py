# Import dependencis
from http.client import ImproperConnectionState
from operator import imod
from bs4 import BeautifulSoup
import requests
import pandas as pd

# scraping tv shows data
def tvShow():
    # create dataframe to store data
    df_tvShow = pd.DataFrame(data=None, columns=['Rank',"Name",'Year','Rating'])
    
    try:
        source = requests.get("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250")
        source.raise_for_status()
        # get all sources
        soup = BeautifulSoup(source.text, "html.parser")
        shows = soup.find("tbody", class_="lister-list")
        shows = shows.find_all("tr")

        for show in shows:
            rank = show.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
            name = show.find("td", class_="titleColumn").a.text
            rel_yer = show.find("td", class_="titleColumn").span.text.strip("()")
            rating = show.find("td", class_="ratingColumn imdbRating").strong.text
            # break
            # print(rank,name,rel_yer,rating)
            
            # append df using loc methods
            df_tvShow.loc[len(df_tvShow)] = [rank,name,rel_yer,rating]

    except Exception as e:
        print(e)
    print(df_tvShow)
    return df_tvShow

# scraping Movie data
def Movie():
    # create dataframe to store data
    df_movie = pd.DataFrame(data=None, columns=['Rank',"Name",'Year','Rating'])
    
    try:
        source = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
        source.raise_for_status()
        # get all sources
        soup = BeautifulSoup(source.text, "html.parser")
        movies = soup.find("tbody", class_="lister-list")
        movies = movies.find_all("tr")

        for movie in movies:
            rank = movie.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
            name = movie.find("td", class_="titleColumn").a.text
            rel_yer = movie.find("td", class_="titleColumn").span.text.strip("()")
            rating = movie.find("td", class_="ratingColumn imdbRating").strong.text
            # break
            # print(rank,name,rel_yer,rating)
            
            # append df using loc methods
            df_movie.loc[len(df_movie)] = [rank,name,rel_yer,rating]

    except Exception as e:
        print(e)
    return df_movie


    print(df_movie)