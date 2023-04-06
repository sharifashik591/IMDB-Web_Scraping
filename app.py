from main import tvShow,Movie
import pandas as pd
# Input movie or tv show option
inp = int(input("Choose Category\n1. TV shows \n2. Movie \nChoose 1 or 2 : "))
print("Loading..............")

try:
    if inp == 1:
        df = tvShow()
        df.to_csv("TV-Shows.csv", index=False)
    elif inp == 2:
        df =Movie()
        df.to_csv("Movis.csv", index=False)
    else:
        print("Input Error")
except:
    print("Extract Error")