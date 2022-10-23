# -*- coding: utf-8 -*-
"""Book Recommendation System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XwPLQI4bD7POLbabAE3-XzLq45zAb3wp

By Arieska Restu Harpian Dwika

# Import Library
"""

import re
import nltk
import random
import warnings
import requests
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
warnings.filterwarnings("ignore")

"""# Data Understanding"""

# Download dataset
# !wget --no-check-certificate -o /content/dataset.zip https://drive.google.com/u/0/uc?id=1cELMx_FGlR8O0mM6_SLb7PiFfXotHQ13&export=download

# Unzip dataset
!unzip /content/dataset.zip

# Mendefinisikan lokasi dataset
books_dir = "/content/Books.csv"
ratings_dir = "/content/Ratings.csv"
users_dir = "/content/Users.csv"

# Melakukan data loading
books = pd.read_csv(books_dir)
ratings = pd.read_csv(ratings_dir)
users = pd.read_csv(users_dir)

# Menampilkan informasi pada setiap data books
print('Informasi pada data books : \n')
books.info()

# Menampilkan informasi pada setiap data ratings
print('Informasi pada data ratings : \n')
ratings.info()

# Menampilkan informasi pada setiap data users
print('Informasi pada data users : \n')
users.info()

# Menampilkan deskripsi statistik dari setiap data books
print('Deskripsi statistik pada data books : ')
books.describe()

# Menampilkan deskripsi statistik dari setiap data ratings
print('Deskripsi statistik pada data ratings : ')
ratings.describe()

# Menampilkan deskripsi statistik dari setiap data users
print('Deskripsi statistik pada data users : ')
users.describe()

# Menampilkan jumlah data dan kolom pada tiap dataset
print("Books Shape \t: " ,books.shape )
print("Ratings Shape \t: " ,ratings.shape )
print("Users Shape \t: " ,users.shape )

# Menampilkan jumlah data yg kosong pada tiap dataset
print("Any null values in Books :\n" ,books.isnull().sum())
print()
print("Any null values in Ratings :\n ", ratings.isnull().sum())
print()
print("Any null values in Users :\n",users.isnull().sum())
print()

"""# Data Preparation"""

# Menggabungkan data books dan data ratings berdasarkan ISBN
books_data=books.merge(ratings,on="ISBN")
df=books_data.copy()

# Remove missing values
df.dropna(inplace=True)

# Reset index dan menghapus kolom index yg ada
df.reset_index(drop=True,inplace=True)

# Menghapus kolom ISBN, Year-Of-Publication, Image-URL-S, Image-URL-M
df.drop(columns=["ISBN","Year-Of-Publication","Image-URL-S","Image-URL-M"],axis=1,inplace=True)

# Menghapus sample yang memiliki nilai book rating = 0
df.drop(index=df[df["Book-Rating"]==0].index,inplace=True)

# Menghapus satu atau lebih karakter non-alfanumerik dalam kolom book title
df["Book-Title"]=df["Book-Title"].apply(lambda x: re.sub("[\W_]+"," ",x).strip())

"""# Modeling"""

def book_recommendations(bookTitle):
    bookTitle=str(bookTitle)
    if bookTitle in df["Book-Title"].values:
        rating_count = pd.DataFrame(df["Book-Title"].value_counts())
        rare_books = rating_count[rating_count["Book-Title"]<=200].index
        common_books = df[~df["Book-Title"].isin(rare_books)]

        if bookTitle in rare_books:
            most_common = pd.Series(common_books["Book-Title"].unique()).sample(3).values
            print("No Recommendations for this Book ☹️ \n ")
            print("YOU MAY TRY: \n ")
            print("{}".format(most_common[0]), "\n")
            print("{}".format(most_common[1]), "\n")
            print("{}".format(most_common[2]), "\n")
        else:
            common_books = common_books.drop_duplicates(subset=["Book-Title"])
            common_books.reset_index(inplace=True)
            common_books["index"] = [i for i in range(common_books.shape[0])]

            targets = ["Book-Title","Book-Author","Publisher"]
            common_books["all_features"] = [" ".join(common_books[targets].iloc[i,].values) for i in range(common_books[targets].shape[0])]

            vectorizer = CountVectorizer()
            common_booksVector = vectorizer.fit_transform(common_books["all_features"])
            similarity = cosine_similarity(common_booksVector)
            index = common_books[common_books["Book-Title"]==bookTitle]["index"].values[0]

            similar_books = list(enumerate(similarity[index]))
            similar_booksSorted = sorted(similar_books,key=lambda x:x[1],reverse=True)[1:6]   # hanya diambil nilai indeks ke 1-5

            books=[]
            for i in range(len(similar_booksSorted)):
                books.append(common_books[common_books["index"]==similar_booksSorted[i][0]]["Book-Title"].item())   # yg diambil judul bukunya
            fig,ax = plt.subplots(1,5,figsize=(17,5))
            fig.suptitle("YOU MAY ALSO LIKE THESE BOOKS",fontsize=40,color="black")

            for i in range(len(books)):
                url = common_books.loc[common_books["Book-Title"]==books[i],"Image-URL-L"][:1].values[0]
                img = Image.open(requests.get(url,stream=True).raw)
                ax[i].imshow(img)
                ax[i].axis("off")
                ax[i].set_title("RATING : {}".format(round(df[df["Book-Title"]==books[i]]["Book-Rating"].mean(),1)),y=-0.20,color="blue",fontsize=22)
                fig.set_facecolor('#ffffff')
                fig.show()
    else:
        print("❌ COULD NOT FIND ❌")

"""# Evaluation"""

# Mendapatkan rekomendasi buku yang mirip dengan The Five People You Meet in Heaven
book_recommendations("The Five People You Meet in Heaven")

# Mendapatkan rekomendasi buku yang mirip dengan The Angel Is Near
book_recommendations("The Angel Is Near")

# Mendapatkan rekomendasi buku yang mirip dengan Tuesdays with Morrie An Old Man a Young Man and Life s Greatest Lesson
book_recommendations("Tuesdays with Morrie An Old Man a Young Man and Life s Greatest Lesson")

# Mendapatkan rekomendasi buku yang mirip dengan A Soldier of the Great War
book_recommendations("A Soldier of the Great War")

# Mendapatkan rekomendasi buku yang mirip dengan Life of Pi
book_recommendations("Life of Pi")