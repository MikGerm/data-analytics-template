Educational Attainment and Crime Rates in Major U.S. Cities
1. Introduction
Education plays a critical role in shaping socio-economic conditions within urban areas. Higher educational attainment is often linked to better employment opportunities, higher incomes, and overall stability. In contrast, cities with lower levels of education frequently experience higher crime rates, making education a potential area for intervention in crime reduction.
This project explores the relationship between educational attainment and crime rates across five major U.S. cities: New York City, Los Angeles, Chicago, Houston, and Phoenix. Our main goal is to determine if cities with higher education levels experience lower crime rates and identify patterns that could help inform policy decisions.
I used educational data (percentage of adults with a high school diploma or bachelor's degree) and crime data (total crimes, violent crimes, and property crimes) over multiple years. However, as we proceeded, we faced challenges with data scraping, merging, and cleaning, which influenced how we structured the analysis. Despite this, we adapted by conducting separate visual analyses for both datasets and examining trends independently.

​​2. Data
2.1 Educational Attainment Data (Web-Scraped)
Source: Census.gov
Description:
The dataset provides detailed insights into the educational composition of adults aged 25 and older across five major U.S. cities: New York City, Los Angeles, Chicago, Houston, and Phoenix. Specifically, it includes:
High School Diploma Percentage: The percentage of adults with at least a high school diploma. This metric serves as a baseline for general educational attainment within a city.
Bachelor’s Degree Percentage: The percentage of adults with a bachelor’s degree or higher. This metric reflects the presence of higher education and advanced skills within the population, which may correlate with socio-economic outcomes such as employment rates, income levels, and crime rates.
Initial Scraping Process:
To acquire this data, I initially relied on web scraping techniques, aiming to automate the extraction of educational statistics directly from Census.gov. Python tools like Selenium and Playwright were used to interact with the website and retrieve dynamically generated content. However, I encountered several significant challenges:
Dynamic Content:
The tables on Census.gov are JavaScript-rendered, meaning they load only after specific user interactions, such as selecting dropdown menus or clicking buttons. This made it impossible to scrape the data using standard tools like BeautifulSoup, which work only with static HTML. While Selenium and Playwright are designed to handle such scenarios, they presented their own set of issues.
Browser Crashes:
Despite configuring Selenium with ChromeDriver to align with the correct versions of Chrome, the browser frequently crashed during execution. Errors like "Stacktrace" and "Session Not Found" indicated potential compatibility issues or performance limitations, especially when handling large, interactive web pages.
Anti-Scraping Measures:
After repeated attempts to scrape the site, the Census.gov server likely detected automated access and began blocking requests. Errors like "Page Failed to Load" and "Something Went Wrong" became more frequent, suggesting the site employed anti-bot mechanisms to protect its content.
Switching to Manual Downloads:
Given these challenges and the time constraints of the project, I decided to switch to manually downloading the necessary CSV files from Census.gov for each city. Although this required more effort upfront, it ensured that the data was accurate, complete, and consistent for analysis. This approach also eliminated the risk of missing data due to scraping errors or incomplete table loads.
Benefits of Manual Downloads:
Clean Data: The downloaded files required minimal cleaning, allowing me to focus on analysis rather than troubleshooting technical issues.
Time Efficiency: While scraping would have been automated in an ideal scenario, manual downloads saved time by avoiding repeated trial-and-error attempts.
Data Accuracy: By accessing official CSV files directly from Census.gov, I ensured the data was authentic and free from corruption during the collection process.
Limitations:
Reduced Automation: The manual download process limited the scalability of data collection. If additional cities or time periods were needed, the process would have to be repeated manually.
In summary, the educational attainment data provided the foundation for analyzing the socio-economic dynamics of major U.S. cities. While the initial scraping attempts were unsuccessful, pivoting to manual downloads ensured the integrity and reliability of the dataset, enabling a robust analysis of the relationship between education and crime rates.

Educational Attainment Data
Column			Type		Description
City				Text                   Name of the city
State				Text		State abbreviation
Bachelor_Percentage		Numeric	% adults with bachelor's degree or more
High_School_Percentage	Numeric	% of adults with a high school diploma

2.2 Crime Data (Downloaded)
Source: FBI Crime Data Explorer & city open data portals
Description: Crime data includes:
Total Crimes: All reported crimes per year.
Violent Crimes: Crimes involving physical harm or force.
Property Crimes: Crimes like theft or burglary.
This dataset was downloaded in CSV format and provided clear yearly crime counts for each city. However, some challenges arose during data cleaning:
City Name Variations: For example, "New York" vs. "New York City" needed standardization.
Missing Years: Data for Houston was incomplete and had to be accounted for separately.
Crime Data
Column			Type		Description
City				Text                   Name of the city
State				Text		State abbreviation
Total_Crime			Numeric            Total reported crimes
Violent_Crime			Numeric            Total violent crimes
Property_Crime			Numeric            Total property crimes

2.3 Data Cleaning and Combining
While my original goal was to merge educational and crime datasets for a direct comparison, the process wasn’t straightforward. Issues included:
Missing Data: Some cities lacked complete data across all years.
City Mismatches: City names varied between datasets, requiring manual cleaning and formatting.
Different Structures: Educational data was structured differently (e.g., percentages), while crime data had raw counts.
To address these issues:
I standardized city names and numeric formats.
Missing rows were dropped, and both datasets were cleaned separately.
Instead of a single merged analysis, I decided individual analyses for educational trends and crime trends.

3. Analysis and Visualizations
3.1 Educational Trends Over Time
I first analyzed trends in educational attainment from 2018 to 2022. This analysis aggregated the total percentage of adults with either a high school diploma or a bachelor's degree across all cities. The graph below illustrates the steady increase in educational attainment during this period.

Key Insights:
Overall Improvement: Educational attainment levels, while not drastically different year over year, show a gradual upward trend. This indicates that cities are maintaining steady progress in education, with slight improvements in the percentage of adults achieving high school diplomas or bachelor’s degrees.
Significant Growth in 2019: A noticeable jump occurred between 2018 and 2019, which could reflect new educational initiatives, policy changes, or improved data reporting for certain cities.
Slight Decline in 2020: Educational progress flattened slightly in 2020. This could be a result of pandemic-related disruptions, such as the closing of educational institutions, reduced workforce training programs, and economic stress affecting access to education.
Plateau in Recent Years: Between 2021 and 2022, the values stabilized, suggesting a recovery period post-pandemic but not a significant leap in education levels.
City Contributions: Larger cities like New York and Los Angeles contributed the most to the overall upward trend, whereas cities like Phoenix and Houston displayed slower growth in educational attainment.

3.2 Crime Trends Over Time
Next, I plotted total crime trends over time for the five cities.
Key Insights:
Key Insights:
Increase in 2020: Crime rates spiked significantly in 2020, likely due to pandemic-related challenges such as economic downturns, unemployment, and social disruptions. The lockdowns and resource strains placed on law enforcement may have further contributed to this trend.
Drop in 2021: A decline occurred in 2021, suggesting temporary stabilization. This could be attributed to improved community programs, the gradual reopening of society, and better law enforcement response post-pandemic.
Steady Rise from 2022 to 2023: Crime rates increased again in 2022 and peaked in 2023. This upward trajectory highlights ongoing challenges in addressing crime despite improving socio-economic conditions. Factors like inflation, housing crises, or specific regional issues might have driven this increase.
City Variability: Cities like New York City contributed the most to the rise in crime values, whereas smaller cities like Phoenix reported relatively lower crime totals throughout the period.


3.3 Educational Trends by City

Finally, I examined educational attainment by city using a stacked bar chart.
Key Insights:
New York City Dominates Crime Totals: New York City stands out with the highest crime totals, significantly surpassing all other cities. This aligns with its larger population size and urban density, which are often correlated with higher crime rates.
Moderate Levels in Chicago and Los Angeles: Cities like Chicago and Los Angeles show moderate crime values compared to New York but 
