import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
merged_df = pd.read_csv("Bike_Sharing.csv")

# Title with emoji
st.title("🚲 Bike Sharing Data Dashboard 📊")

# Sidebar filters
st.sidebar.header("Filter Data 🛠️")

# Season filter
season_options = merged_df['season_day'].unique().tolist()
season_filter = st.sidebar.multiselect("Select Season:", season_options, default=season_options)

# Weather filter
weather_options = merged_df['weathersit_day'].unique().tolist()
weather_filter = st.sidebar.multiselect("Select Weather Condition:", weather_options, default=weather_options)

# Apply filters
filtered_df = merged_df[(merged_df['season_day'].isin(season_filter)) & (merged_df['weathersit_day'].isin(weather_filter))]

# Visualization 1: Impact of Weather on Bike Rentals
st.subheader("🌦️ Impact of Weather on Bike Rentals")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=filtered_df['weathersit_day'], y=filtered_df['cnt_day'], ax=ax)
ax.set_xlabel("Weather Condition")
ax.set_ylabel("Total Bike Rentals")
ax.set_title("Impact of Weather on Bike Rentals")
st.pyplot(fig)

# Visualization 2: Hourly Bike Rental Trend
st.subheader("🕒 Hourly Bike Rental Trend")
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(x=filtered_df['hr'], y=filtered_df['cnt_hour'], estimator='mean', errorbar=None, ax=ax)
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Bike Rentals")
ax.set_title("Hourly Bike Rental Trend")
st.pyplot(fig)

# Visualization 3: Seasonal Bike Rental Patterns
st.subheader("🍂 Seasonal Bike Rental Patterns")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x=filtered_df['season_day'], y=filtered_df['cnt_day'], ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Total Bike Rentals")
ax.set_title("Seasonal Bike Rental Patterns")
st.pyplot(fig)

# Visualization 4: Total Rentals per Season and Weather Condition
st.subheader("📊 Total Rentals per Season & Weather")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=filtered_df['season_day'], y=filtered_df['cnt_day'], hue=filtered_df['weathersit_day'], ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Total Bike Rentals")
ax.set_title("Total Rentals per Season & Weather")
st.pyplot(fig)

# Footer
st.write("🚀 Dashboard Created with Streamlit & Matplotlib")
