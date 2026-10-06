import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('june2026new.csv')

plt.style.use('ggplot')

st.title('IGCSE Edexcel Statistics June 2026')

subject = st.selectbox("Choose a subject", df['subject'])

if st.button('Plot'):

    fig, ax = plt.subplots()

    row = df.loc[df.subject == subject].iloc[0].tolist()
    row.pop(0)

    #plot
    palette = sns. color_palette("Set3", n_colors = 1)
    sns.barplot(x = df.columns[1::], y = row, palette = palette)
    plt.xlabel('grade')
    plt.ylabel('percentage')
    ax.set_title(subject)
    st.pyplot(fig)

                            


                                                
