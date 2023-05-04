import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Read file path

agg_trans = pd.read_csv("agg_trans_good_idddd.csv")
map_trans = pd.read_csv("map_trans_id.csv")
top_trans = pd.read_csv("top_trans_id.csv")
map_user = pd.read_csv("map_user_id.csv")
avg_amo = pd.read_csv("avg_merge_1.csv")

#function block
def indiamap():
    c= map_trans.groupby(["state","year"]).sum()
    c.reset_index(inplace = True)
    return c 
def transName():
    p= agg_trans.groupby(["state","year","transaction_name"]).sum()
    p.reset_index(inplace = True)
    return p

def mapUser():
    u= map_user.groupby(["state","year"]).sum()
    u.reset_index(inplace = True)
    return u


def aggTrans(option1,option2,option3):
    a= agg_trans[(agg_trans.state == option1) & (agg_trans.year == option2) & (agg_trans.quarter == option3)]
    a.reset_index(inplace = True)
    return a

def mapTrans(option1,option2,option3):
    mt= map_trans[(map_trans.state == option1) & (map_trans.year == option2) & (map_trans.quarter == option3)]
    mt.reset_index(inplace = True)
    return mt

def mapUserState(option1,option2,option3):
    au= map_user[(map_user.state == option1) & (map_user.year == option2) & (map_user.quarter == option3)]
    au.reset_index(inplace = True)
    return au

def comp2state(option5,option6):
    b= agg_trans[(agg_trans.state == option5) | (agg_trans.state == option6)]
    b= b.groupby(["state","year"]).sum()
    b.reset_index(inplace = True)
    return b

def c2state(option5,option6):
    bt= agg_trans[(agg_trans.state == option5) | (agg_trans.state == option6)]
    bt= bt.groupby(["state","year","transaction_name"]).sum()
    bt.reset_index(inplace = True)
    return bt

def User2state(option5,option6):
    comp_user= map_user[(map_user.state == option5) | (map_user.state == option6)]
    comp_user= comp_user.groupby(["state","year"]).sum()
    comp_user.reset_index(inplace = True)
    return comp_user

def avg_amounts():
    avg= avg_amo
    avg.reset_index(inplace = True)
    return avg

# Add image
#st.image("1_9jXREk1HTzopG-R75Xo48w.png")
st.title("Phonepe Analytics Dashboard")


# Add option menu
with st.sidebar:
  selected = option_menu(menu_title=None, options=["India Map","State Data","Compare 2 states","averge amount/app Opens"], icons=["clipboard-data","award","capslock-fill","coin"], orientation="horizontal")

# Code or map page
  if selected=="India Map":
    radio_button = ["About Transaction","About User"]
    option = st.radio("what visualisation you need ?", radio_button, index=1)
    
    if option == "About Transaction":
     option8 = st.selectbox(
      'Transaction Count or Amount?',("count","total_amount"))
    
    if option == "About User":
      option8 = st.selectbox(
      'Reg User or Number of times App open?',("reg_user","app_open"))

# Code for statewise page
  if selected=="State Data":
    radio_button = ["About Transaction","About User"]
    option = st.radio("what visualisation you need for the state?", radio_button, index=1)

    if option == "About Transaction":
     option1 = st.selectbox(
     'State u need?',
     ('Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))
    
     option2 = st.selectbox(
     'Year u need?',(2018, 2019, 2020, 2021, 2022))

     option3 = st.selectbox(
     'Quarter u need?',("Q1", "Q2", "Q3", "Q4"))

     option4 = st.selectbox(
     'Transaction count or amount?',("count","total_amount"))

    if option == "About User":
      option1 = st.selectbox(
      'State u need?',
      ('Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))
    
      option2 = st.selectbox(
      'Year u need?',(2018, 2019, 2020, 2021, 2022))

      option3 = st.selectbox(
      'Quarter u need?',("Q1", "Q2", "Q3", "Q4"))

      option4 = st.selectbox(
      'Reg User or Number of times App open?',("reg_user","app_open"))

# Code for compare 2 states page
  if selected=="Compare 2 states":
    radio_button = ["About Transaction","About User"]
    option = st.radio("what visualisation you need for the state?", radio_button, index=1)

    if option == "About Transaction":

     option5 = st.selectbox(
     'State:1 u need?',
     ('Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))
    
     option6 = st.selectbox(
     'State:2 u need?',
     ('Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))

     option7 = st.selectbox(
     'Transaction count or amount?',("count","total_amount"))

    if option == "About User":

     option5 = st.selectbox(
     'State:1 u need?',
     ('Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))
    
     option6 = st.selectbox(
     'State:2 u need?',
     ('Andaman & Nicobar','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadara & Nagar Havelli','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'))

     option7 = st.selectbox(
     'Reg User or Number of times App open?',("reg_user","app_open"))
  
  

#Button for statewise
if selected=="State Data":
  if option == "About Transaction":
   a= aggTrans(option1,option2,option3)
   mt= mapTrans(option1,option2,option3)

   if st.sidebar.button("show"):
      fig = px.choropleth(
       a,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color=option4,
       color_continuous_scale='ice'
      )


      fig.update_geos(fitbounds="locations", visible=False)
      
      st.write("total transaction")
      st.write(fig)

      fi = px.bar(mt, x='district', y=option4)
      st.write("About User district wise")
      st.write(fi)

  if option == "About User":
   au= mapUserState(option1,option2,option3)

   if st.sidebar.button("show"):
      fig = px.choropleth(
       au,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color=option4,
       color_continuous_scale='ice'
      )


      fig.update_geos(fitbounds="locations", visible=False)
      
      st.write("About User")
      st.write(fig)  

      fi = px.bar(au, x='district', y=option4)
      st.write("About User district wise")
      st.write(fi)


      

#Button for compare 2 state
if selected=="Compare 2 states":
  if option == "About Transaction":
   b= comp2state(option5,option6)

   bt= c2state(option5,option6)

   if st.sidebar.button("show"):
      fig = px.choropleth(
       b,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color=option7,
       animation_frame='year',
       color_continuous_scale='ice'
      )


      fig.update_geos(fitbounds="locations", visible=False)
      
      st.write("total transaction")
      st.write(fig)

      pi = px.bar(bt, x="state", y=option7, color="transaction_name",animation_frame="year", title="Transaction type and its Contribution with respect to State",width=900,height=700)
      st.write("State wise with Transaction type")
      st.write(pi)

  if option == "About User":
   comp_user= User2state(option5,option6)

   if st.sidebar.button("show"):
      fig = px.choropleth(
       comp_user,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color=option7,
       animation_frame='year',
       color_continuous_scale='ice'
      )


      fig.update_geos(fitbounds="locations", visible=False)
      
      st.write("About User in particular 2 State")
      st.write(fig)

#Button for Indian Map
if selected=="India Map":
  if option == "About Transaction":
   c = indiamap()
   p = transName()  
   if st.sidebar.button("show"):
      #india
      fig=px.choropleth(
       c,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color=option8,
       animation_frame='year',
       color_continuous_scale='ice',
       height=500,
       width=800
      )
      
      fig.update_geos(fitbounds="locations", visible=False)

      st.write("About Transaction")
      st.write(fig)

      pi = px.bar(p, x="state", y=option8, color="transaction_name",animation_frame="year", title="Transaction type and its Contribution with respect to State",width=900,height=700)
      st.write("State wise with Transaction type")
      st.write(pi)


  if option == "About User":
   u = mapUser()
  
   if st.sidebar.button("show"):
      #india
      fig=px.choropleth(
       u,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color=option8,
       animation_frame='year',
       color_continuous_scale='ice',
       height=500,
       width=800
      )
      
      fig.update_geos(fitbounds="locations", visible=False)

      st.write("About User")
      st.write(fig)

if selected=="averge amount/app Opens":
   avg = avg_amounts()

   if st.sidebar.button("show"):
      fig = px.choropleth(
       avg,
       geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
       featureidkey='properties.ST_NM',
       locations='state',
       color='avg_amount',
       animation_frame='year',
       color_continuous_scale='ice'
      )


      fig.update_geos(fitbounds="locations", visible=False)
      
      st.write("Averge amount transaction per AppOpens")
      st.write(fig)