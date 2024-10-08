import pandas as pd
import streamlit as st
import numpy as np
st.write("Our first dataframe")
df= pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[5,6,7,8]
})

st.write("Our second dataframe")
dataframe= np.random.randn(10,20)
st.dataframe(dataframe)

st.write("line chart")
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])

st.line_chart(chart_data)

st.write("map data")
map_data =pd.DataFrame(
    np.random.randn(1000,2) / (50,50) + [37.76, -122.4],
    columns=['lat','lon'])
st.map(map_data)

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
    
left, middle, right = st.columns(3)
if left.button("Plain button", use_container_width=True):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji button", icon="😃", use_container_width=True):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:", use_container_width=True):
    right.markdown("You clicked the Material button.")