# An Exploration Section with charts, graphs, or tables that highlight the key insights and 
# data distributions in the dataset.

import streamlit as st
import pandas as pd
import panel as pn
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pathlib as Path

# st.set_page_config(
#     page_title="Le Pard | Visualization",
#     page_icon="📈",
#     layout="centered")

def app():
    # --- LOAD CSS ---
    current_dir = Path.Path(__file__).parent if "__file__" in locals() else Path.Path.cwd()
    css_file = current_dir /"styles" / "main.css"
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    # Hero Section
    st.markdown("<h3 '>HR Analytics Visualizations</h3>", unsafe_allow_html=True)

    # Load the dataset (CSV file)
    df = pd.read_csv('HR_Analytics.csv')
    # XLSX file
    excel_file = 'HR_Analytics.xlsx'

    sheet_name = '(clean w Outlier)HR_Analytics'
    df_sheet = pd.read_excel(excel_file, sheet_name=sheet_name)

    sheet_name2 = '(FINAL)HR_Analytics'
    df_sheet2 = pd.read_excel(excel_file, sheet_name=sheet_name)

    
    # Expander
    with st.expander("Dataset Snapshots on Excel (Raw Data to Clean Data)"):
        st.subheader("Raw Data")
        st.dataframe(df)
        st.divider()
        st.subheader("Cleaned Data with Outliers")
        st.dataframe(df_sheet)
        st.divider()
        st.subheader("Final Cleaned Data")
        st.dataframe(df_sheet2)


    tab1, tab2, tab3, tab4 = st.tabs(["Pie Chart", "Box Plot", "Density Plot", "Heatmap"])

    with tab1:
        with st.container(border=True):
            # Create two columns to limit width
            col1, col2, col3 = st.columns([0.5, 3, 0.5])  # Adjust the proportions as needed
            with col2:  # Center column for the plot
            
                # Count the number of employees in each Job Level
                job_level_counts = df['JobLevel'].value_counts().reset_index()
                job_level_counts.columns = ['JobLevel', 'Count']

                # Create a pie chart
                fig_pie = px.pie(job_level_counts, values='Count', names='JobLevel',
                                title='Distribution of Employees by Job Level',
                                color_discrete_sequence=px.colors.sequential.RdBu)

                # Display the pie chart
                st.plotly_chart(fig_pie, use_container_width=True)

            # Add insights below the plot
        st.markdown("""
        The pie chart shows that 36.8% of employees occupy Job Level 1, while 36.4% are at Job Level 2, indicating a strong presence of entry-level and mid-level staff. In contrast, only 4.66% and 7.23% hold positions at Job Levels 4 and 5, suggesting limited representation in higher roles. This distribution highlights the need for enhanced career advancement opportunities and talent development strategies to encourage employees to pursue senior-level positions.
        """)

    with tab2:
        with st.container(border=True):
            # Create two columns to limit width
            col1, col2, col3 = st.columns([0.5, 3, 0.5])  # Adjust the proportions as needed
            with col2:  # Center column for the plot
                # Box plot for salary distribution by job level
                fig_box = px.box(df, x="JobLevel", y="MonthlyIncome", color="JobLevel",
                                title="Monthly Income Distribution by Job Level",
                                labels={"JobLevel": "Job Level", "MonthlyIncome": "Monthly Income"})

                # Display the box plot
                st.plotly_chart(fig_box, use_container_width=True)

        # Add insights below the plot
        st.markdown("""
        The graph shows a clear positive relationship between job level and monthly income. As job levels increase from 1 to 5, median income rises significantly. Lower job levels (1 and 2) have a more compact income distribution with less variability, while higher levels (3 to 5) show broader income ranges and higher pay. The trend highlights a structured salary progression, with stable but higher pay at senior job levels. There are a few outliers in lower levels, indicating some variation in income.
        """)

    with tab3:
        with st.container(border=True):
            # Create two columns to limit width
            col1, col2, col3 = st.columns([0.5, 3, 0.5])  # Adjust the proportions as needed
            with col2:  # Center column for the plot
                # Density plot for monthly income (full-width)
                density_fig = px.histogram(df, x='MonthlyIncome', nbins=30, marginal='rug',
                                        title='Density Plot for Monthly Income',
                                        labels={'MonthlyIncome': 'Monthly Income', 'count': 'Density'})
                # Change the color of the bars
                density_fig.update_traces(marker_color='#E67644')  # Set your desired color
                
                # Display the density plot with full width
                st.plotly_chart(density_fig, use_container_width=True)

        # Add insights below the plot
        st.markdown("""
        The density plot shows that the monthly income distribution is skewed to the right, with most employees earning lower salaries and a few outliers earning significantly higher incomes. The peak of the distribution is around 5k, indicating that this salary range is the most common. The overall range of monthly income is from 0 to 20k.
        """)

    with tab4:
        with st.container(border=True):
            # Create two columns to limit width
            col1, col2, col3 = st.columns([0.5, 3, 0.5])  # Adjust the proportions as needed
            with col2:  # Center column for the plot
                # Specify the columns you want to include in the correlation heatmap
                columns_to_include = ['Age', 'JobLevel', 'MonthlyIncome', 'TotalWorkingYears', 'YearsAtCompany']

                # Select only the specified columns
                df_selected = df[columns_to_include]

                # Correlation Heatmap of the selected columns
                corr_matrix = df_selected.corr()

                # Update figure size and centering it
                fig = go.Figure(data=go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    colorscale='Plasma',
                ))

                 # Update the layout for better size and centering
                fig.update_layout(
                    title='HR Analytics Correlation Heatmap',
                    xaxis_title='Variables',
                    yaxis_title='Variables',
                    xaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns),
                    yaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns),
                    width=800,  # Increased width
                    height=600,  # Increased height
                    autosize=False,
                    margin=dict(l=100, r=100, t=100, b=100),
                    title_x=0,  # Left align the title
                    title_y=0.95  # Adjust the vertical position if needed
                )

                # Show the heatmap
                st.plotly_chart(fig, use_container_width=True)  # Use the full container width to center

        # Add insights below the heatmap
        st.markdown("""
        The heatmap confirms the findings from the previous scatter plots, highlighting the strong relationships between job level and monthly income, as well as the positive associations between total working years, years at company, and monthly income. Age appears to have a limited influence on these variables.
        """)
