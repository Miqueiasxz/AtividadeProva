import numpy as np #linear algebra
import pandas as pd # data processing, CSV file 1/0 (e.g. pd.read_csv)
import streamlit as st
import matplotlib.pyplot as plt

# pip install streamlit panda numpy matplotlib seaborn
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#link do local dos dados
# https://www.kaggle.com/datasets/suraj520/music-dataset-song-information-and-lyrics?resource=download

import seaborn as sns

data = pd.read_csv("songs.csv")

st.dataframe(data)

sns.histplot(data, x='Popularity', kde=True, color='g')

#SideBar
st.sidebar.title("Apresentação dos Dados")

#Titulo
st.title("Analíse de Dados do DataSet de Músicas")
