# streamlit-dashboard

## Overview

This project is a Streamlit application that visualizes key metrics of GitHub repositories using a dataset in CSV format. The dashboard provides insights through an overview of the dataset and various visualizations, helping users analyze the popularity of repositories based on programming languages.

## Features

- **Dataset Overview**: Displays the entire dataset with styled tables for better readability.
- **Basic Statistics**: Provides summary statistics of the dataset.
- **Visualizations**:
  - Total stars count grouped by programming language (Bar Chart).
  - Relationship between forks and stars (Scatter Plot).
- **User-Friendly Interface**: Navigation sidebar for easy access to different sections.

## Requirements

### Using `requirements.txt`

This project requires the following Python libraries:

- `streamlit`
- `pandas`
- `plotly`

You can install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt

