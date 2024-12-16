Analysis Plan
This plan outlines the process and steps taken for the analysis of educational attainment and crime rates in five major U.S. cities. It provides a roadmap to ensure transparency, organization, and reproducibility throughout the project.

Objective
To analyze the relationship between educational attainment and crime rates across five major U.S. cities (New York City, Los Angeles, Chicago, Houston, and Phoenix). Specifically, the project aims to:

Determine whether cities with higher educational attainment exhibit lower crime rates.
Identify trends over time for both crime rates and educational outcomes.
Highlight any significant variations or patterns across cities.
Steps
1. Data Collection
Educational Data:

Source: Census.gov
Process: Initially attempted to scrape data using Selenium and Playwright but encountered issues with dynamic content and anti-scraping measures.
Resolution: Manually downloaded CSV files for educational attainment percentages (high school diploma and bachelor's degree) for all five cities.
Files: Educational_Attainment_Combined.csv (Cleaned data).
Crime Data:

Source: FBI Crime Data Explorer and open city portals.
Process: Crime data for New York, Los Angeles, Chicago, Phoenix, and Houston was downloaded individually.
Files: Combined into a single raw file (Final_Combined_Raw_Crime_Data.csv) and further cleaned into Cleaned_Crime_Data.csv.
2. Data Cleaning and Preparation
Educational Data:

Combined multiple educational data files into a unified dataset.
Cleaned and standardized the data by removing unnecessary characters and ensuring consistency in city names.
Key Columns: city, year, and value.
Crime Data:

Merged individual city-level crime data into a single dataset.
Cleaned data to standardize city names and convert columns to appropriate formats.
Key Columns: city, year, and value.
Output:

Cleaned educational data: Educational_Attainment_Combined.csv.
Cleaned crime data: Cleaned_Crime_Data.csv.
3. Exploratory Data Analysis (EDA)
Conducted an initial analysis of the cleaned data to understand trends, distributions, and missing values.
Generated key visualizations for better insights:
Educational Data Trends: Line graph showing educational attainment trends over time.
Crime Data Trends: Line graph highlighting fluctuations in crime rates over time.
City Comparisons: Bar charts comparing total crime values and educational attainment across cities.
4. Visualization
The following visualizations were created to identify patterns and address the research questions:

Crime Trends Over Time: Line graph showing total crime values from 2019 to 2023.
Educational Trends Over Time: Line graph showing educational attainment values (e.g., high school and bachelor's degree percentages) across years.
Total Crime by City: Bar chart comparing crime values for all cities.
Educational Data by City Over Time: Stacked bar chart displaying educational attainment across cities and years.
These visualizations highlight:

Trends in education and crime separately.
Comparisons between cities in terms of education and crime rates.
5. Analysis Limitations
Data Gaps: We couldn’t fully merge educational and crime datasets due to format inconsistencies and missing fields for direct correlations.
Manual Adjustments: Educational data required manual downloads after scraping challenges.
Assumptions: Crime data was aggregated as totals, limiting analysis of specific crime categories.
6. Key Insights and Next Steps
Cities like New York reported both higher educational attainment and total crime values, showing complex relationships between these variables.
Cities with lower education levels, such as Phoenix, also reported lower total crime values.
Trends over time revealed fluctuations in crime rates, particularly in 2020 and 2023, likely due to socio-economic disruptions.
Future Steps: A deeper regression analysis, once data alignment is improved, could provide stronger evidence for the correlation between education and crime.
