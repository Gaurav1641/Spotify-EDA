# -*- coding: utf-8 -*-
"""Spotify EDA .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rSCvCK5lqNTNWzhMCdvG8J_iP0iqVfvb
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from your specified file path
spotify_df = pd.read_csv(r"C:\Users\gaura\Downloads\spotify.csv")

# Step 1: Data Quality Check
print("Initial Dataset Shape:", spotify_df.shape)
missing_values = spotify_df.isnull().sum()
print("Missing Values:\n", missing_values)
duplicate_rows = spotify_df.duplicated().sum()
print("Duplicate Rows:", duplicate_rows)

# Remove duplicates
spotify_df = spotify_df.drop_duplicates()
print("Dataset Shape After Removing Duplicates:", spotify_df.shape)

# Step 2: Distribution of Popularity
plt.figure(figsize=(10, 6))
sns.histplot(spotify_df['Popularity'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Track Popularity', fontsize=16)
plt.xlabel('Popularity', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Step 3: Popularity vs Duration
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Duration (ms)', y='Popularity', data=spotify_df, alpha=0.7)
plt.title('Popularity vs Duration of Tracks', fontsize=16)
plt.xlabel('Duration (ms)', fontsize=14)
plt.ylabel('Popularity', fontsize=14)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.show()

# Step 4: Artist with Most Tracks
plt.figure(figsize=(12, 8))
sns.countplot(y='Artist', data=spotify_df, order=spotify_df['Artist'].value_counts().index[:10])
plt.title('Top Artists by Number of Tracks', fontsize=16)
plt.xlabel('Count', fontsize=14)
plt.ylabel('Artist', fontsize=14)
plt.show()

# Step 5: Top 5 Least Popular Tracks
least_popular = spotify_df.nsmallest(5, 'Popularity')[['Artist', 'Track Name', 'Popularity']]
print("Top 5 Least Popular Tracks:")
print(least_popular)

# Step 6: Top Artists by Average Popularity
top_artists = spotify_df['Artist'].value_counts().head(5).index
average_popularity = spotify_df[spotify_df['Artist'].isin(top_artists)].groupby('Artist')['Popularity'].mean()
print("Top 5 Artists by Average Popularity:")
print(average_popularity)

# Step 7: Most Popular Tracks for Top Artists
most_popular_tracks = spotify_df[spotify_df['Artist'].isin(top_artists)].sort_values(by=['Artist', 'Popularity'], ascending=[True, False])
most_popular_tracks = most_popular_tracks.groupby('Artist').first()[['Track Name', 'Popularity']]
print("Most Popular Tracks for Top Artists:")
print(most_popular_tracks)

# Step 8: Pair Plot for Numerical Variables
sns.pairplot(spotify_df[['Popularity', 'Duration (ms)']])
plt.show()

# Step 9: Duration of Tracks Across Artists
plt.figure(figsize=(12, 8))
sns.boxplot(x='Artist', y='Duration (ms)', data=spotify_df[spotify_df['Artist'].isin(top_artists)])
plt.title('Track Duration Across Artists', fontsize=16)
plt.xlabel('Artist', fontsize=14)
plt.ylabel('Duration (ms)', fontsize=14)
plt.xticks(rotation=45)
plt.show()

# Step 10: Popularity Distribution for Artists
plt.figure(figsize=(12, 8))
sns.violinplot(x='Artist', y='Popularity', data=spotify_df[spotify_df['Artist'].isin(top_artists)], inner='point')
plt.title('Popularity Distribution for Top Artists', fontsize=16)
plt.xlabel('Artist', fontsize=14)
plt.ylabel('Popularity', fontsize=14)
plt.xticks(rotation=45)
plt.show()

