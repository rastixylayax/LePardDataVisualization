# A Visualizations Section with charts, graphs, or tables that highlight the key insights and 
# trends from your data.

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


    tab1, tab2, tab3, tab4 = st.tabs(["Box Plot", "Density Plot", "Scatter Plot", "Heatmap"])

    with tab1:
        # Box plot for salary distribution by job level (full-width)
        fig_box = px.box(df, x="JobLevel", y="MonthlyIncome", color="JobLevel",
                        title="Monthly Income Distribution by Job Level",
                        labels={"JobLevel": "Job Level", "MonthlyIncome": "Monthly Income"})

        # Display the box plot with full width
        st.plotly_chart(fig_box, use_container_width=True)

        # Add insights below the plot
        st.markdown("""
        The graph shows a clear positive relationship between job level and monthly income. As job levels increase from 1 to 5, median income rises significantly. Lower job levels (1 and 2) have a more compact income distribution with less variability, while higher levels (3 to 5) show broader income ranges and higher pay. The trend highlights a structured salary progression, with stable but higher pay at senior job levels. There are a few outliers in lower levels, indicating some variation in income.
        """)

    with tab2:
        # Density plot for monthly income (full-width)
        density_fig = px.histogram(df, x='MonthlyIncome', nbins=30, marginal='rug',
                                title='Density Plot for Monthly Income',
                                labels={'MonthlyIncome': 'Monthly Income', 'count': 'Density'})
        
        # Display the density plot with full width
        st.plotly_chart(density_fig, use_container_width=True)

        # Add insights below the plot
        st.markdown("""
        The density plot shows that the monthly income distribution is skewed to the right, with most employees earning lower salaries and a few outliers earning significantly higher incomes. The peak of the distribution is around 5k, indicating that this salary range is the most common. The overall range of monthly income is from 0 to 20k.
        """)

    with tab3:
        # Dropdown for selecting the scatter plot
        scatter_plot_type = st.selectbox("Choose Scatter Plot", ["Job Level vs Monthly Income", "Age vs Monthly Income", "Total Working Years vs Monthly Income", "Years at Company vs Monthly Income"])

        # Create a dictionary to map the dropdown options to the corresponding independent variables
        scatter_plot_mapping = {
            "Job Level vs Monthly Income": "JobLevel",
            "Age vs Monthly Income": "Age",
            "Total Working Years vs Monthly Income": "TotalWorkingYears",
            "Years at Company vs Monthly Income": "YearsAtCompany"
        }

        # Create a dictionary to map each graph type to a specific color
        color_mapping = {
            "Job Level vs Monthly Income": "darkblue",
            "Age vs Monthly Income": "green",
            "Total Working Years vs Monthly Income": "red",
            "Years at Company vs Monthly Income": "purple"
        }

        # Get the selected independent variable and color
        selected_variable = scatter_plot_mapping[scatter_plot_type]
        selected_color = color_mapping[scatter_plot_type]

        # Perform linear regression on the entire dataset
        X = df[[selected_variable]].values
        y = df['MonthlyIncome'].values
        model_coefs = np.polyfit(X.squeeze(), y, 1)

        # Calculate R-squared
        def calculate_r_squared(x, y, coefs):
            y_pred = coefs[0] * x + coefs[1]
            y_mean = np.mean(y)
            ss_total = np.sum((y - y_mean) ** 2)
            ss_res = np.sum((y - y_pred) ** 2)
            r_squared = 1 - (ss_res / ss_total)
            return r_squared

        r_squared = calculate_r_squared(X.squeeze(), y, model_coefs)

        # Randomly sample 25% of the data for visualization
        sampled_df = df.sample(frac=0.25, random_state=42)

        # Create a scatter plot for the selected variable
        scatter = go.Scatter(
            x=sampled_df[selected_variable], 
            y=sampled_df['MonthlyIncome'], 
            mode="markers", 
            marker=dict(color=selected_color), 
            name=f"Dependent Variable"
        )
        regression_line = go.Scatter(
            x=sampled_df[selected_variable], 
            y=sampled_df[selected_variable] * model_coefs[0] + model_coefs[1], 
            mode="lines", 
            line=dict(color=selected_color), 
            name=(
                f"Regression Line"
            )
        )

        # Create the figure
        fig = go.Figure()
        fig.add_trace(scatter)
        fig.add_trace(regression_line)

        # Calculate coordinates for annotations
        x_coord = sampled_df[selected_variable].min() + 0.05 * (sampled_df[selected_variable].max() - sampled_df[selected_variable].min())
        y_coord = sampled_df['MonthlyIncome'].max() - 0.1 * (sampled_df['MonthlyIncome'].max() - sampled_df['MonthlyIncome'].min())

        # Add regression equation and R-squared to the plot
        fig.add_annotation(
            text=f'y = {model_coefs[0]:.2f}x + {model_coefs[1]:.2f}',
            x=x_coord,
            y=y_coord,
            showarrow=False
        )
        fig.add_annotation(
            text=f'R² = {r_squared:.4f}',
            x=x_coord,
            y=y_coord - 0.1 * (sampled_df['MonthlyIncome'].max() - sampled_df['MonthlyIncome'].min()),
            showarrow=False
        )

        # Set the x and y labels
        fig.update_xaxes(title_text=selected_variable)
        fig.update_yaxes(title_text='MonthlyIncome')

        # Update the overall figure size to make it larger
        fig.update_layout(width=800, height=600)

        # Show the figure
        st.plotly_chart(fig)

        # Display different markdown text for each selected scatter plot
        if scatter_plot_type == "Job Level vs Monthly Income":
            st.markdown(
                """
            The scatter plot shows a strong positive relationship between Job Level and Monthly Income. The regression line \(y = 4038.15x - 1833.24\) and the R-squared value of 0.9022 indicate that Job Level is a significant predictor of Monthly Income, explaining about 90% of the variation.
            """
            )
        elif scatter_plot_type == "Age vs Monthly Income":
            st.markdown(
                """
            The scatter plot shows a weak positive relationship between Age and Monthly Income. The regression line \(y = 256.15x - 2951.58\) and the R-squared value of 0.2475 suggest that Age is not a strong predictor of Monthly Income, explaining only about 25% of the variation.
            """
            )
        elif scatter_plot_type == "Total Working Years vs Monthly Income":
            st.markdown(
                """
            The scatter plot shows a moderate positive relationship between Total Working Years and Monthly Income. The regression line \(y = 466.83x + 1238.30\) and the R-squared value of 0.5957 suggest that Total Working Years is a reasonably strong predictor, explaining about 60% of the variation in Monthly Income.
            """
            )
        elif scatter_plot_type == "Years at Company vs Monthly Income":
            st.markdown(
                """
            The scatter plot shows a weak positive relationship between Years at Company and Monthly Income. The regression line \(y = 395.25x + 3734.47\) and the R-squared value of 0.2647 indicate that Years at Company has a weak effect on Monthly Income, explaining only about 26% of the variation.
            """
            )

    with tab4:
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
            colorbar=dict(title='Correlation Coefficient')
        ))

        # Update the layout for better size and centering
        fig.update_layout(
            title='Correlation Heatmap',
            xaxis_title='Variables',
            yaxis_title='Variables',
            xaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns),
            yaxis=dict(tickvals=list(range(len(corr_matrix.columns))), ticktext=corr_matrix.columns),
            width=800,  # Increased width
            height=600,  # Increased height
            autosize=False,
            margin=dict(l=100, r=100, t=100, b=100),
            title_x=0.5  # Center the title
        )

        # Show the heatmap
        st.plotly_chart(fig, use_container_width=True)  # Use the full container width to center

        # Add insights below the heatmap
        st.markdown("""
        The heatmap confirms the findings from the previous scatter plots, highlighting the strong relationships between job level and monthly income, as well as the positive associations between total working years, years at company, and monthly income. Age appears to have a limited influence on these variables.
        """)

