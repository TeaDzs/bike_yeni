import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Mapping weekday values to labels
weekday_map = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday",
               4: "Thursday", 5: "Friday", 6: "Saturday"}
day_df["weekday_label"] = day_df["weekday"].map(weekday_map)

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")
st.sidebar.write("Analisis data peminjaman sepeda")

# Header
st.title("🚲 Bike Sharing Dashboard")
st.write("Dashboard interaktif untuk menganalisis pola peminjaman sepeda.")

# 1. Tren peminjaman berdasarkan musim
st.header("Tren Peminjaman Berdasarkan Musim")
season_trend = day_df.groupby("season")["cnt"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="season", y="cnt", data=season_trend, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# 2. Pola penggunaan berdasarkan hari dalam seminggu
st.header("Pola Peminjaman Berdasarkan Hari")
weekday_trend = day_df.groupby("weekday_label")["cnt"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="weekday_label", y="cnt", data=weekday_trend, palette="viridis", ax=ax)
ax.set_xlabel("Hari")
ax.set_ylabel("Jumlah Peminjaman")
plt.xticks(rotation=30)
st.pyplot(fig)

# 3. Hubungan suhu dan peminjaman
st.header("Hubungan Suhu dan Peminjaman Sepeda")
fig, ax = plt.subplots()
sns.scatterplot(x="temp", y="cnt", data=day_df, alpha=0.5, color="blue", ax=ax)
sns.regplot(x="temp", y="cnt", data=day_df, scatter=False, color="red", ax=ax)
ax.set_xlabel("Suhu (0-1)")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# 4. Waktu puncak peminjaman dalam sehari
st.header("Waktu Puncak Peminjaman Sepeda")
hourly_trend = hour_df.groupby("hr")["cnt"].sum().reset_index()
fig, ax = plt.subplots()
sns.lineplot(x="hr", y="cnt", data=hourly_trend, marker="o", color="blue", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# 5. Perbandingan hari kerja vs akhir pekan
st.header("Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")
day_df["is_weekend"] = day_df["weekday"].isin([0, 6])
weekend_vs_weekday = day_df.groupby("is_weekend")["cnt"].mean().reset_index()
weekend_vs_weekday["is_weekend"] = weekend_vs_weekday["is_weekend"].map({True: "Weekend", False: "Weekday"})
fig, ax = plt.subplots()
sns.barplot(x="is_weekend", y="cnt", data=weekend_vs_weekday, palette="coolwarm", ax=ax)
ax.set_xlabel("Kategori Hari")
ax.set_ylabel("Rata-rata Peminjaman")
st.pyplot(fig)

st.write("Dashboard ini dibuat menggunakan Streamlit. 🚀")
