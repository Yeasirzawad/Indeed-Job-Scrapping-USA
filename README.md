

# Job Market Analysis in Data-Driven Careers in USA
## Project Overview
This project presents a comprehensive analysis of the job market for data-driven careers in the USA, offering insights into in-demand roles, skills, salary benchmarks, company profiles, geographic hotspots, and workforce development needs. The analysis is presented in the form of an interactive Power BI dashboard.

## Objective
1.Provide a detailed overview of the job market landscape for data-driven roles in the USA.

2.Identify the top industries, companies, and geographic regions with high demand for data professionals. 

3.Analyze salary trends and benchmarks for different data roles across various job levels and company sizes. 

4.Highlight the essential skills required for data-driven roles, including programming languages, databases, and data visualization tools. 

5.Evaluate company profiles, employee benefits, and work culture factors that influence job satisfaction and retention in the data field.

## Data Collection
The data collection methodology employed a multi-phased web scraping approach using Selenium in Python, targeting Indeed.com, a leading job aggregation platform. In the initial phase, we extracted 11,290 job posting links for roles including data analyst, business analyst, data scientist, data engineer, and machine learning engineer. Subsequently, we scraped these links to gather comprehensive job information, including job titles, job levels, required academic degrees, job locations, salary ranges etc. Building on this foundation, we identified 4,989 unique company links within the job listings. In the final phase, we leveraged these company links to extract detailed organizational profiles, encompassing data on revenue ranges, employee counts, founding years, work well-being scores, and industries etc.

![Explain a step or phase](https://github.com/Yeasirzawad/Indeed-Job-Scrapping-USA/assets/163287308/a2f68015-c204-491b-aafb-9552a42f06c3)


## Datasets

### Clean Dataset

| Variables | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `role` | `string` | The job role or position (e.g., business analyst, data analyst, data engineer) |
| `level` | `string` | The level of the job position (e.g., entry_level, mid_level, senior_level) |
| `degree` | `string` | The required degree or educational qualification for the job (e.g., bachelors, masters, doctorate)|
| `link` | `string` | The URL of the job posting |
| `job_title` | `string` | The title of the job position |
| `company` | `string` | The name of the company offering the job |
| `company_url` | `string` | The URL or website address of the company |
| `location` | `string` | The location of the job|
| `job_type` | `string` | The type of job (e.g., full-time, part-time, contract)|
| `description` | `string` | The detailed description of the job responsibilities and requirements|
| `cname` | `string` | The name of the company offering the job|
| `ratings` | `float` | The rating or score given to the company by employees or reviewers|
| `review_count` | `integer` | The number of reviews or ratings submitted for the company|
| `review_link` | `string` | The URL or link to the company's review page|
| `company_size` | `ordinal` |The size or number of employees in the company|
| `company_revenue` | `ordinal` | The revenue range of the company|
| `company_industry` | `string` | The industry or sector in which the company operates|
| `ceo_name` | `string` | The name of the company's Chief Executive Officer.|
| `ceo_approve_percentage` | `integer` | The percentage of employees or reviewers who approve of the company's CEO|
| `company_founded` | `integer` | The year in which the company was founded.|
| `company_website_url` | `string` | The URL or website address of the company|
| `Average_rating_score` | `float` | The average work well-being score given to the company|
| `Average_rating` | `ordinal` | The descriptive rating for the company (e.g., Average, Above average, Below average).|
| `Happiness` | `integer` | Score for employee happiness at the company|
| `Stress-free` | `integer` | Score for the stress-free environment at the company|
| `Purpose` | `integer` | Score for the sense of purpose employees feel at the company|
| `Satisfaction` | `integer` | Score for employee satisfaction at the company|
| `Flexibility` | `integer` | Score for the flexibility offered by the company|
| `Achievement` | `integer` | Score for the  for achievement at the company|
| `Learning` | `integer` | Score for the learning and development opportunities at the company|
| `Inclusion` | `integer` | Score for the inclusive culture at the company|
| `Support` | `integer` | Score for the support provided to employees by the company|
| `Appreciation` | `integer` | Score for the appreciation shown to employees by the company|
| `Energy` | `integer` | Score for the energy of employees at the company|
| `Compensation` | `integer` | Score for the compensation or salaries provided by the company|
| `Management` | `integer` | Score for the management or leadership at the company|
| `Trust` | `integer` | Score for the trust employees have in the company's leadership|
| `Belonging` | `integer` | Score for the sense of belonging employees feel at the company|
| `min_salary` | `float` | The minimum salary or lower end of the salary range|
| `max_salary` | `float` | The maximum salary or upper end of the salary range|
| `min_max_revenue` | `ordinal` | The combined minimum and maximum revenue range of the company.|
| `python` | `integer` | A binary value indicating whether Python skills are required for the job role (1) or not (0)|
| `mysql` | `integer` | A binary value indicating whether MySQL skills are required for the job role (1) or not (0)|
| `postgresql` | `integer` | A binary value indicating whether Postgresql skills are required for the job role (1) or not (0)|
| `tensorflow` | `integer` | A binary value indicating whether Tensorflow skills are required for the job role (1) or not (0)|
| `pytorch` | `integer` | A binary value indicating whether Pytorch skills are required for the job role (1) or not (0)|
| `aws` | `integer` | A binary value indicating whether AWS skills are required for the job role (1) or not (0)|
| `tableau` | `integer` | A binary value indicating whether Tableau skills are required for the job role (1) or not (0)|
| `powerbi` | `integer` | A binary value indicating whether Powerbi skills are required for the job role (1) or not (0)|
| `hadoop` | `integer` | A binary value indicating whether Hadoop skills are required for the job role (1) or not (0)|
| `kafka` | `integer` | A binary value indicating whether Kafka skills are required for the job role (1) or not (0)|
| `java` | `integer` | A binary value indicating whether Java skills are required for the job role (1) or not (0)|
| `excel` | `integer` | A binary value indicating whether Excel skills are required for the job role (1) or not (0)|
| `scikit-learn` | `integer` | A binary value indicating whether Scikit-Learn skills are required for the job role (1) or not (0)|
| `sklearn` | `integer` | A binary value indicating whether Sklearn skills are required for the job role (1) or not (0)|
| `r` | `integer` | A binary value indicating whether r skills are required for the job role (1) or not (0)|
| `scala` | `integer` | A binary value indicating whether Scala skills are required for the job role (1) or not (0)|
| `stata` | `integer` | A binary value indicating whether STATA skills are required for the job role (1) or not (0)|
| `spss` | `integer` | A binary value indicating whether SPSS skills are required for the job role (1) or not (0)|
| `sas` | `integer` | A binary value indicating whether SAS skills are required for the job role (1) or not (0)|

### Benefits
| Variables | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `link` | `string` | The URL of the job posting|
| `benefits` | `list` | Benefits Provided by Company for the Job|

### States
| Variables | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `link` | `string` | The URL of the job posting|
| `State Abbreviation` | `list` |States where job is located|







## Data Cleaning and Segmentation:

1. Imported the scraped data into Python and loaded it into a pandas DataFrame for further processing.
2. Conducted data cleaning, including handling missing values, removing duplicates, and formatting columns.
3. Performed data transformations and created derived columns to enhance the analysis.
4. Extracted relevant skills mentioned in the job descriptions.

## Dashboard Overview
The Power BI dashboard consists of four main pages:

1. Summary: Provides an overview of the project objectives, dataset, and key insights.
2. Job Information: Analyzes job postings by level, average salaries based on degree and job level, and salaries across different data roles.
3. Company & Skills: Examines company revenue distribution, job postings and salaries by company size and roles, and required skills for various data roles.
4. Company Overview: Showcases job postings and ratings of top companies, CEO approval and work wellbeing scores by revenue, top employee benefits, and a detailed overview of selected companies.



[![View Report](https://img.shields.io/badge/View%20Power%20BI%20Report-0078D4?style=for-the-badge&logo=power-bi&logoColor=white)](https://app.powerbi.com/view?r=eyJrIjoiYTQ5MDc4NjAtYzI0ZS00YTRjLWE4NGEtODgxMzY4Yjc2ZGI2IiwidCI6IjZmNDczODVjLTY3YjQtNGMwNi1hN2M0LWVmNmZhNTI4YTk1ZSIsImMiOjEwfQ%3D%3D&pageName=8261f97ece42040ada0a&fbclid=IwZXh0bgNhZW0CMTEAAR15CYGczhBypvaadaHKGVFyOjUbe_WgPAWGWk3Q81zstFIE7EAazZUQ4O8_aem_QDHVIHBEAiA7BCugdAbn6g)



## Key Insights
Some of the key insights derived from the analysis include:

1. Analyzed 11,290 job postings across 131 industries and 4,989 unique companies.

2. Top states with the most job openings: California, Texas, and New York.

3. Top hiring industries: Information Technology, Healthcare, and Aerospace & Defense.

4. Machine learning engineers have the highest average salary, earning $165K.

5. 22.18% of companies have $1B-5B revenue, followed by $100M-500M (17.89%).

6. Average CEO approval rating is 45.5%, with a company rating of 3.7/5.

7. Python, SQL, Power BI, and Tableau are essential across data roles, while Scala, TensorFlow, and Kafka are critical for data engineers and scientists.

## Contribution

Contributions to this project are welcome. If you have any suggestions, improvements, or additional insights to share, please open an issue or submit a pull request.


## Authors

- [@Yeasirzawad](https://github.com/Yeasirzawad)
