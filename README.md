# Spotify Data Analysis 🟢

This project involves a detailed analysis of a Spotify dataset to uncover trends, relationships, and insights about tracks, artists, and their popularity. Using Python libraries such as Pandas, Matplotlib, and Seaborn, we explore the data to create visualizations and answer key analytical questions.

---

## Table of Contents
- [Dataset](#dataset)
- [Features](#features)
- [Analysis Workflow](#analysis-workflow)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Visualizations and Outputs](#visualizations-and-outputs)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

---

## Dataset

The dataset used in this project contains the following columns:
- **Artist**: Name of the artist.
- **Track Name**: Name of the track.
- **Popularity**: Popularity score of the track (integer, 0–100).
- **Duration (ms)**: Track duration in milliseconds.
- **Track ID**: Unique identifier for each track.

The dataset was cleaned to handle duplicate rows and checked for missing values.

---

## Features

The analysis aims to answer the following key questions:
1. **Data Quality Check**  
   - Handle missing values and duplicate rows.

2. **Popularity Distribution**  
   - Visualize the distribution of track popularity using a histogram.

3. **Popularity vs Duration**  
   - Explore relationships between popularity and track duration via scatter plots.

4. **Top Artists**  
   - Identify the artist with the highest number of tracks and display counts using a count plot.

5. **Least Popular Tracks**  
   - Find and list the 5 least popular tracks by artist and track name.

6. **Top Artists by Popularity**  
   - Calculate and compare the average popularity of the top 5 most prolific artists.

7. **Top Tracks for Popular Artists**  
   - List the most popular track for each of the top 5 artists.

8. **Pair Plot**  
   - Visualize relationships between numerical features (e.g., popularity and duration).

9. **Duration Across Artists**  
   - Compare track durations across artists using box plots or violin plots.

10. **Popularity Distribution**  
   - Explore popularity distributions for top artists using violin or swarm plots.

---

## Analysis Workflow

The analysis is conducted in the following steps:
1. **Loading the Data**: Read and inspect the dataset.
2. **Data Cleaning**: Handle missing values and duplicates.
3. **Exploratory Data Analysis (EDA)**: Use descriptive statistics and visualizations.
4. **Insight Extraction**: Address specific questions and provide results.
5. **Visualization**: Generate clear and intuitive plots for each question.

---

## Dependencies

This project requires the following Python libraries:
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

## Visualizations and Outputs

### Example Visualizations
- **Popularity Distribution**: Histogram showing the frequency of popularity scores.
- **Popularity vs Duration**: Scatter plot showing the relationship between track duration and popularity.
- **Top Artists**: Count plot of the top 10 artists with the most tracks.
- **Duration Comparison**: Box/Violin plots comparing track durations across top artists.

### Example Outputs
- List of the 5 least popular tracks (artist and track name).
- Average popularity scores for the top 5 artists.
- Most popular track for each top artist.

---

## Future Enhancements

- Include more features like genre, release year, and album information for deeper insights.
- Predict track popularity using machine learning models.
- Develop an interactive dashboard for real-time data exploration.

---

## Contributors

- **Gaurav Mahajan** - Data Analysis, Visualization, and Documentation  
  [GitHub Profile](http://github.cm/Gaurav1641)  
  [LinkedIn Profile](linkedin.com/in/gaurav-mahajan-49783622b)

