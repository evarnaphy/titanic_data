import pandas as pd
import streamlit as st
import plotly.express as px


st.write("TITANIC DATA ANALYSIS")

@st.cache_data
def load_data(url):
    df=pd.read_csv(url)
    return df

df=pd.read_csv("Titanic csv.csv")
st.dataframe(df)
passenger_counts = df.groupby('PassengerId').size().reset_index(name='Number_of_Passenger')
df = pd.merge(df, passenger_counts, on='PassengerId')
df= df.dropna()
embarked_mapping = {
    'C': 'Cherbourg',
    'Q': 'Queenstown',
    'S': 'Southampton'
}
df['Embarked'] = df['Embarked'].map(embarked_mapping)
df.head(5)
st.button("Rerun")

st.write("Passengers by class bar chart")
st.bar_chart(
    df,
    x="Pclass",
    y="Number_of_Passenger",
)


st.write("no. of passengers by family size")
st.bar_chart(
    df,
    x="SibSp",
    y="Number_of_Passenger"
)

fig= px.pie(df, values='Number_of_Passenger', names='Sex',
             title="Gender Distribution",
             color_discrete_map={'Male': '#636EFA', 'Female': '#EF553B'},
              hover_data=['Number_of_Passenger'])
st.plotly_chart(fig, use_container_width=True)

st.write("Embarked Distribution")
st.bar_chart(
    df,
    x="Embarked",
    y="Number_of_Passenger",
)

fig=px.pie(df, values='Number_of_Passenger', names='Survived',
             title="Survival status",
             color_discrete_map={'Male': '#636EFA', 'Female': '#EF553B'})
st.plotly_chart(fig, use_container_width=True)
