import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration for wide mode
st.set_page_config(
    page_title="GitHub Repositories Dashboard",
    layout="wide"
)

# Load the dataset from a CSV file
@st.cache_data
def load_data():
    return pd.read_csv('github_dataset.csv')  # Change to your actual file path

def style_dataframe(df):
    # Style the DataFrame with a background gradient and format numbers
    return df.style.background_gradient(cmap='viridis').format(
        na_rep='NaN', 
        precision=0
    )

# Main function to run the Streamlit app
def main():
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Choose an option", ["Overview", "Visualizations"])
    
    # Load data
    data = load_data()

    if options == "Overview":
        st.title("🌟 Streamlit Dashboard")
        
        # Display instructions for full-screen
        st.write("To view this dashboard in full-screen mode, press **F11** on your keyboard.")
        
        # Display dataset
        st.subheader("Dataset Overview")
        st.dataframe(style_dataframe(data), use_container_width=True)  # Styled table

        # Show basic stats
        st.subheader("Basic Statistics")
        st.write(data.describe())
        
    elif options == "Visualizations":
        st.title("📊 Visualizations")

        # Filter out rows with NULL values in 'language' column for visualizations
        filtered_data = data[data['language'].notnull()]

        # Bar chart for star counts by language
        st.subheader("Total Stars Count by Language")
        stars_by_language = filtered_data.groupby('language')['stars_count'].sum().reset_index()
        fig = px.bar(
            stars_by_language, 
            x='language', 
            y='stars_count', 
            color='stars_count',
            color_continuous_scale=px.colors.sequential.Viridis,
            title='Total Stars Count by Language',
            labels={'stars_count': 'Total Stars'}
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Scatter plot for forks vs stars
        st.subheader("Scatter Plot: Forks vs Stars")
        fig2 = px.scatter(
            filtered_data,  # Use filtered data to avoid plotting null values
            x='forks_count', 
            y='stars_count', 
            title='Forks vs Stars',
            labels={'forks_count': 'Number of Forks', 'stars_count': 'Number of Stars'},
            hover_name='repositories',
            color='language',
            color_discrete_sequence=px.colors.qualitative.Plotly,
            size='stars_count',
            size_max=20
        )
        st.plotly_chart(fig2, use_container_width=True)

        # Insights
        st.subheader("Insights")
        st.write("This dashboard visualizes key metrics of GitHub repositories.")
        st.write("The bar chart shows the total stars count grouped by programming language.")
        st.write("The scatter plot illustrates the relationship between forks and stars, indicating the popularity of repositories.")

if __name__ == "__main__":
    main()
