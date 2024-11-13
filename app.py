import streamlit as st
import pandas as pd
import plotly.express as px


vehicles = pd.read_csv('vehicles_us.csv')
vehicles['manufacturer'] = vehicles['model'].apply(lambda x: x.split()[0])


st.header('Data Viewer')
st.dataframe(vehicles)


st.header('Vehicle fuel types by engine size')
fig = px.histogram(vehicles, x='cylinders', color='fuel')
st.write(fig)


fig = px.scatter(
    vehicles,
    x='type', 
    y='cylinders', 
    size_max=5,
    width=500,
)
st.write(fig)


st.header('Compare Engine Size between Vehicle Types')


model_list = sorted(vehicles['model'].unique())


model_1 = st.selectbox(
                              label='Select model 1', # title of the select box
                              options=model_list, # options listed in the select box
                              index=model_list.index('chevrolet corvette') # default pre-selected option
                              )


model_2 = st.selectbox(
                              label='Select model 2',
                              options=model_list, 
                              index=model_list.index('ford mustang')
                              )


mask_filter = (vehicles['model'] == model_1) | (vehicles['model'] == model_2)
vehicles_filtered = vehicles[mask_filter]


normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None


fig = px.histogram(vehicles_filtered,
                      x='cylinders',
                      nbins=30,
                      color='model',
                      histnorm=histnorm,
                      barmode='overlay')


st.write(fig)