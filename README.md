![image](https://github.com/user-attachments/assets/f1eaa7ea-1454-4fce-bbed-b645e9af1513)
# Solar Energy Analytics Report – Week 0 Challenge
**Project**: Exploratory Solar Analysis for MoonLight Energy Solutions  
**Date:** May 2025



## 1. Introduction

This project focuses on analyzing environmental and solar irradiance data collected from solar farms in Benin, Sierra Leone, and Togo. The objective is to identify regions with high potential for solar energy investments, helping MoonLight Energy Solutions optimize operational efficiency and sustainability.

The data includes hourly solar radiation measurements (GHI, DNI, DHI), temperature, humidity, wind, and other relevant environmental variables.



## 2. Methodology

### Tools Used
- **Python**, **pandas**, **seaborn**, **matplotlib**, **scipy**
- **Jupyter Notebooks** for EDA
- **Streamlit** for dashboard deployment
- **Git/GitHub** for version control and CI/CD

## Steps Taken
1. **Data Cleaning & Profiling**
   - Checked for missing values and outliers.
   - Imputed missing data using median.
   - Dropped irrelevant fields (e.g., Comments column).

2. **Exploratory Data Analysis**
   - Distribution plots for GHI, DNI, DHI.
   - Time series analysis to explore trends.
   - Correlation heatmaps and scatter plots for insight discovery.
   - Impact of cleaning events on module readings.

3. **Cross-Country Comparison**
   - Compared GHI, DNI, DHI across countries using boxplots.
   - Summary statistics table (mean, median, std).
   - ANOVA test to evaluate statistical significance.

4. Dashboard
   - Built an interactive Streamlit app to explore country-wise metrics.





## 4. Recommendations

- Benin showed consistently higher GHI and DNI values, making it the most viable candidate for large-scale solar installation.
- Implement routine sensor cleaning**, as data showed a clear boost in sensor readings post-cleaning.
- Use real-time monitoring dashboards** for operational oversight.
- Invest in automated cleaning systems** to improve energy output without manual intervention.



## 5. Conclusion

This challenge provided hands-on exposure to end-to-end data engineering and analysis. The findings highlight Benin’s solar advantage, reveal valuable patterns from environmental features, and support strategic investment decisions.

MoonLight Energy Solutions can leverage these insights to deploy solar assets where they yield maximum return and reliability.



# Dashboard link

https://solar-challenge-week1-p5njyqbwxwka6xau6sh5hd.streamlit.app/





