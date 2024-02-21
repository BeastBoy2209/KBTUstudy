# Dictionary of movies

movies = [{
        "name": "Usual Suspects", 
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]
# leng =len(movies)
# print(leng)
#1----------------------------------------------------------------------------------
def imdb55checker(movies):
    ConfiramtionYN = input("Do you want to use [single movie and returns True if its IMDB score is above 5.5]?(Y/N)")
    if ConfiramtionYN.lower() == "n":
        return
    Moviename = input("Write the name of the movie:")
    imdb55 = False
    for i in movies:
        if Moviename.lower() == i["name"].lower():
            if i["imdb"] >= 5.5:
                imdb55 = True

    if imdb55 == True:
        print("True")
    else:
        print("False")
imdb55checker(movies)
#2----------------------------------------------------------------------------------
def imdb55list(movies):
    ConfiramtionYN = input("Do you want to use [sublist of movies with an IMDB score above 5.5]?(Y/N)")
    if ConfiramtionYN.lower() == "n":
        return
    for i in movies:
        if i["imdb"] >= 5.5:
            print(i["name"],i["imdb"],i["category"])
imdb55list(movies)
#3----------------------------------------------------------------------------------
def category(movies):
    ConfiramtionYN = input("Do you want to use [category name and returns just those movies under that category]?(Y/N)")
    if ConfiramtionYN.lower() == "n":
        return
    cat=input("Iput category:")
    for i in movies:
        if i["category"].lower() == cat.lower():
            print(i["name"])
category(movies)

#4----------------------------------------------------------------------------------
def avIMDB(movies):
    ConfiramtionYN = input("Do you want to use [calculating list of movies and computes the average IMDB score]?(Y/N)")
    if ConfiramtionYN.lower() == "n":
        return
    imdbSUM=0
    countFilms=0
    for i in movies:
        imdbSUM += i["imdb"]
        countFilms +=1
    avimdb = imdbSUM/countFilms
    print("Average IMDB score:", avimdb)
avIMDB(movies)
#5----------------------------------------------------------------------------------
def avIMDBcategory(movies):
    ConfiramtionYN = input("Do you want to use [calculating category and computes the average IMDB score]?(Y/N)")
    if ConfiramtionYN.lower() == "n":
        return
    imdbSUM=0
    countFilms=0
    avimdb =0 
    category =input("Iput category:")
    for i in movies:
        if i["category"].lower() == category.lower():
            imdbSUM += i["imdb"]
            countFilms +=1
    if countFilms != 0:
        avimdb = imdbSUM/countFilms
    print("Average IMDB score:", avimdb)
avIMDBcategory(movies)