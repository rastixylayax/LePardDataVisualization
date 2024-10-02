# A Visualizations Section with charts, graphs, or tables that highlight the key insights and 
# trends from your data.

import streamlit as st
import pandas as pd
import panel as pn
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Page 2",
    page_icon=":woman_and_man_holding_hands:",
    layout="wide")

# Hero Section
st.markdown("<h3 style='text-align: center; color: #f14a16;'>HR Analytics Visualizations</h3>", unsafe_allow_html=True)

# Expander
with st.expander("Dataset Snapshots on Excel (Raw to Cleaned Data)"):
    st.image('assets/dataset_excel_pic.png', width=950)
    st.divider()
    st.image('assets/dataset_excel_pic2.png', width=650)
    st.divider()
    st.image('assets/dataset_excel_pic3.png', width=450)

# Load the dataset
df = pd.read_csv('HR_Analytics.csv')

tab1, tab2, tab3, tab4 = st.tabs(["Box Plot", "Density Plot", "Scatter Plot", "Heatmap"])

with tab1:
    # Box plot for salary distribution by job level
    fig_box = px.box(df, x="JobLevel", y="MonthlyIncome", color="JobLevel",
                 title="Monthly Income Distribution by Job Level",
                 labels={"JobLevel": "Job Level", "MonthlyIncome": "Monthly Income"})
    st.plotly_chart(fig_box)

with tab2:
    # Density plot for monthly income
    density_fig = px.histogram(df, x='MonthlyIncome', nbins=30, marginal='rug',
                           title='Density Plot for Monthly Income',
                           labels={'MonthlyIncome': 'Monthly Income', 'count': 'Density'})
    st.plotly_chart(density_fig)

with tab3:
    # Create subplots for independent variables vs Monthly Income
    independent_variables = ['JobLevel', 'Age', 'TotalWorkingYears', 'YearsAtCompany']
    y_variable = 'MonthlyIncome'

    # Define subplot dimensions
    subplot_titles = ['Job Level vs Monthly Income', 'Age vs Monthly Income', 'Total Working Years vs Monthly Income', 'Years at Company vs Monthly Income']
    shared_yaxes = True

    # Create subplots
    fig = make_subplots(rows=2, cols=2, subplot_titles=subplot_titles, shared_yaxes=shared_yaxes)

    # Define colors for regression lines
    line_colors = ['darkblue', 'green', 'red', 'purple']

    # Define legends for the plots
    legends = ['Job Level', 'Age', 'Total Working Years', 'Years at Company']

    # Add a function to calculate the R-squared value for a linear regression
    def calculate_r_squared(x, y, coefs):
        y_pred = coefs[0] * x + coefs[1]
        y_mean = np.mean(y)
        ss_total = np.sum((y - y_mean) ** 2)
        ss_res = np.sum((y - y_pred) ** 2)
        r_squared = 1 - (ss_res / ss_total)
        return r_squared

    # Loop through the independent variables and create subplots
    for i, x_var in enumerate(independent_variables):
        row = i // 2 + 1
        col = i % 2 + 1

        # Randomly sample 25% of the data for visualization
        sampled_df = df.sample(frac=0.25, random_state=42)

        # Perform linear regression on the entire dataset
        X = df[[x_var]].values
        y = df[y_variable].values
        model_coefs = np.polyfit(X.squeeze(), y, 1)

        # Calculate R-squared
        r_squared = calculate_r_squared(X.squeeze(), y, model_coefs)

        # Create a scatter plot for each variable
        scatter = go.Scatter(x=sampled_df[x_var], y=sampled_df[y_variable], mode="markers", name=f"Scatter ({legends[i]})")
        regression_line = go.Scatter(x=sampled_df[x_var], y=sampled_df[x_var] * model_coefs[0] + model_coefs[1], mode="lines", line=dict(color=line_colors[i]), name=f"Regression Line ({legends[i]})")

        # Add regression equation and R-squared to plot
        fig.add_trace(scatter, row=row, col=col)
        fig.add_trace(regression_line, row=row, col=col)

        # Calculate coordinates for annotations
        x_coord = sampled_df[x_var].min() + 0.05 * (sampled_df[x_var].max() - sampled_df[x_var].min())
        y_coord = sampled_df[y_variable].max() - 0.1 * (sampled_df[y_variable].max() - sampled_df[y_variable].min())

        # Add regression equation and R-squared to the plot
        fig.add_annotation(
            text=f'y = {model_coefs[0]:.2f}x + {model_coefs[1]:.2f}',
            x=x_coord,
            y=y_coord,
            showarrow=False,
            row=row,
            col=col
        )
        fig.add_annotation(
            text=f'R² = {r_squared:.4f}',
            x=x_coord,
            y=y_coord - 0.1 * (sampled_df[y_variable].max() - sampled_df[y_variable].min()),
            showarrow=False,
            row=row,
            col=col
        )

        # Set the x label for each subplot
        fig.update_xaxes(title_text=x_var, row=row, col=col)

        # Set the y-axis label only in the first column
        if col == 1:
            fig.update_yaxes(title_text=y_variable, row=row, col=col)
        else:
            fig.update_yaxes(showticklabels=False, row=row, col=col)

    # Update the overall figure size to make it larger
    fig.update_layout(width=1400, height=800)

    # Show the figure
    st.plotly_chart(fig)

with tab4:
    # Specify the columns you want to include in the correlation heatmap
    columns_to_include = ['Age', 'JobLevel', 'MonthlyIncome', 'TotalWorkingYears', 'YearsAtCompany']

    # Select only the specified columns
    df_selected = df[columns_to_include]

    # Correlation Heatmap of the selected columns
    corr_matrix = df_selected.corr()

    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Plasma',
        colorbar=dict(title='Correlation Coefficient')
    ))

    fig.update_layout(
        title='Correlation Heatmap',
        xaxis_title='Variables',
        yaxis_title='Variables',
        xaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns),
        yaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns),
    )

    st.plotly_chart(fig)  # Use st.plotly_chart to display the figure in Streamlit

