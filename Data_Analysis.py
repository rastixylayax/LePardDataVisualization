# An Analysis Section with charts, graphs, or tables that highlight the results of
# the analysis performed (regression, kmeans, dbscan) on the dataset.

import streamlit as st
import pandas as pd
import panel as pn
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pathlib as Path
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import panel as pn
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import pathlib as Path
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

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
    st.markdown("<h3>Data Analysis and Insights</h3>", unsafe_allow_html=True)

    # Load the dataset (CSV file)
    df = pd.read_csv('HR_Analytics.csv')
    # XLSX file
    excel_file = 'HR_Analytics.xlsx'

    sheet_name = '(clean w Outlier)HR_Analytics'
    df_sheet = pd.read_excel(excel_file, sheet_name=sheet_name)

    sheet_name2 = '(FINAL)HR_Analytics'
    df_sheet2 = pd.read_excel(excel_file, sheet_name=sheet_name)


    tab1, tab2, tab3 = st.tabs(["Linear Regression Analysis", "K-Means Clustering", "DBSCAN Clustering"])

    with tab1:
            with st.container(border=True):
                # Dropdown for selecting the scatter plot
                scatter_plot_type = st.selectbox("Choose Scatter Plot", ["Job Level vs Monthly Income", "Age vs Monthly Income", "Total Working Years vs Monthly Income", "Years at Company vs Monthly Income"])
                # Create two columns to limit width
                col1, col2, col3 = st.columns([0.5, 4, 0.5]) 
                with col2:  # Center column for the plot
                    

                    # Create a dictionary to map the dropdown options to the corresponding independent variables
                    scatter_plot_mapping = {
                        "Job Level vs Monthly Income": "JobLevel",
                        "Age vs Monthly Income": "Age",
                        "Total Working Years vs Monthly Income": "TotalWorkingYears",
                        "Years at Company vs Monthly Income": "YearsAtCompany"
                    }

                    # Create a dictionary to map each graph type to a specific color
                    color_mapping = {
                        "Job Level vs Monthly Income": "lightpink",
                        "Age vs Monthly Income": "aquamarine",
                        "Total Working Years vs Monthly Income": "coral",
                        "Years at Company vs Monthly Income": "plum"
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
                The scatter plot shows a strong positive relationship between Job Level and Monthly Income. The regression line \(y = 4038.15x - 1833.24\) and the R-squared value of 0.9022 indicate that Job Level has a significant strong effect on Monthly Income, explaining about 90% of the variation.
                """
                )
            elif scatter_plot_type == "Age vs Monthly Income":
                st.markdown(
                    """
                The scatter plot shows a weak positive relationship between Age and Monthly Income. The regression line \(y = 256.15x - 2951.58\) and the R-squared value of 0.2475 suggest that Age has a weak effect on Monthly Income, explaining only about 25% of the variation.
                """
                )
            elif scatter_plot_type == "Total Working Years vs Monthly Income":
                st.markdown(
                    """
                The scatter plot shows a moderate positive relationship between Total Working Years and Monthly Income. The regression line \(y = 466.83x + 1238.30\) and the R-squared value of 0.5957 suggest that Total Working Years has a reasonably strong effect on Monthly Income, explaining about 60% of the variation in Monthly Income.
                """
                )
            elif scatter_plot_type == "Years at Company vs Monthly Income":
                st.markdown(
                    """
                The scatter plot shows a weak positive relationship between Years at Company and Monthly Income. The regression line \(y = 395.25x + 3734.47\) and the R-squared value of 0.2647 indicate that Years at Company has a weak effect on Monthly Income, explaining only about 26% of the variation.
                """
                )
    with tab2:
        with st.expander("Elbow Method for K-Means Clustering"):

            df = pd.read_csv('HR_Analytics (Clean).csv')

            # Select relevant features for clustering
            features = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'JobLevel']
            X = df[features]

            # Standardize the features
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            # Determine the optimal number of clusters using the elbow method
            inertia = []
            for k in range(1, 11):
                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(X_scaled)
                inertia.append(kmeans.inertia_)

            # Data for elbow curve
            elbow_data = pd.DataFrame({'Number of Clusters': range(1, 11), 'Inertia': inertia})

            # Elbow method plot using Altair
            elbow_chart = alt.Chart(elbow_data).mark_line(point=True).encode(
                x=alt.X('Number of Clusters:Q', title='Number of Clusters'),
                y=alt.Y('Inertia:Q', title='Inertia'),
                tooltip=['Number of Clusters', 'Inertia']
            ).properties(
                title='Elbow Method',
                width=700,
                height=400
            )

            st.altair_chart(elbow_chart, use_container_width=True)

        # Apply K-means clustering
        optimal_k = st.slider("Select the number of clusters (k):", min_value=2, max_value=10, value=3, step=1)
        st.divider()
        kmeans = KMeans(n_clusters=optimal_k, random_state=42)
        df['Cluster'] = kmeans.fit_predict(X_scaled)

        # Add the cluster centers
        cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)

        # Scatter plot for Age vs. MonthlyIncome
        scatter_chart = alt.Chart(df).mark_circle(size=60).encode(
            x=alt.X('Age:Q', scale=alt.Scale(domain=[df['Age'].min(), df['Age'].max()])),
            y=alt.Y('MonthlyIncome:Q', title='Monthly Income'),
            color=alt.Color('Cluster:N', legend=alt.Legend(title='Cluster'), scale=alt.Scale(scheme='set1')),
            tooltip=['Age', 'MonthlyIncome', 'Cluster']
        ).properties(
            title='Age vs. Monthly Income (k=3)',
            width=700,
            height=400
        )

        # Overlay cluster centers
        centers_df = pd.DataFrame(cluster_centers, columns=features)
        centers_df['Cluster'] = range(optimal_k)

        centers_chart = alt.Chart(centers_df).mark_point(size=150, filled=True, color='cyan').encode(
            x='Age:Q',
            y='MonthlyIncome:Q',
            tooltip=['Age', 'MonthlyIncome']
        )

        final_chart = scatter_chart + centers_chart
        st.altair_chart(final_chart, use_container_width=True)
        st.markdown(
            """
        The scatter plot shows the results of K-Means clustering on the HR Analytics dataset, comparing Age (x-axis) and Monthly Income (y-axis). Different clusters are represented by distinct colors, with <span style="color: cyan;">***cyan-colored***</span> data points indicating ***cluster centers***. It highlights patterns in income distribution across age groups, providing insights into cluster formation.
        """, unsafe_allow_html=True)
        st.divider()

        # PCA transformation
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)

        # Add PCA components to DataFrame
        df['PCA1'] = X_pca[:, 0]
        df['PCA2'] = X_pca[:, 1]

        # Scatter plot for PCA-reduced data
        pca_chart = alt.Chart(df).mark_circle(size=60).encode(
            x=alt.X('PCA1:Q', title='PCA Component 1'),
            y=alt.Y('PCA2:Q', title='PCA Component 2'),
            color=alt.Color('Cluster:N', legend=alt.Legend(title='Cluster'), scale=alt.Scale(scheme='set1')),
            tooltip=['PCA1', 'PCA2', 'Cluster']
        ).properties(
            title='PCA-reduced Clusters',
            width=700,
            height=400
        )

        st.altair_chart(pca_chart, use_container_width=True)
        st.markdown(
            """
        The scatter plot represents clusters projected into two dimensions using PCA (Principal Component Analysis). The x-axis (PCA Component 1) and y-axis (PCA Component 2) highlight distinct groupings ***(num of clusters == num of k selected)*** based on their features. Each cluster is represented by a unique color, providing a simplified view of high-dimensional data relationships.
        """)
        st.divider()

        st.markdown("<h4> K-Means: Silhouette Score</h4>", unsafe_allow_html=True)
        if optimal_k > 1:
            score = silhouette_score(X_scaled, kmeans.labels_)
            st.write(f"Silhouette Score: **{score:.2f}**")
        else:
            st.write("Silhouette Score cannot be calculated for k=1.")

    with tab3:

        # Apply DBSCAN
        dbscan = DBSCAN(eps=1, min_samples=10)  # Tune eps and min_samples
        df['Cluster_DBSCAN'] = dbscan.fit_predict(X_scaled)

        # Create Altair chart
        chart = alt.Chart(df).mark_circle(size=30).encode(
            x=alt.X('Age:Q', scale=alt.Scale(domain=[df['Age'].min(), df['Age'].max()])),
            y='MonthlyIncome',
            color=alt.Color('Cluster_DBSCAN:N', scale=alt.Scale(scheme='set1'), legend=alt.Legend(title='Cluster')),
            tooltip=['Age', 'MonthlyIncome', 'Cluster_DBSCAN'],
            opacity=alt.value(0.8)
        ).properties(
            title='DBSCAN Clustering: Age vs. Monthly Income',
            width=400,
            height=400
        )

        # Display chart in Streamlit
        st.altair_chart(chart, use_container_width=True)
        st.markdown(
            """
        The scatter plot shows the results of DBSCAN clustering on the HR Analytics dataset, comparing Age (x-axis) and Monthly Income (y-axis). Different clusters are represented by distinct colors, with -1 indicating noise points. It highlights patterns in income distribution across age groups, providing insights into cluster formation and outliers.
        """)