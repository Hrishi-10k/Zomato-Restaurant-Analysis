# 🍽️ Zomato Restaurant Analysis | Data Analytics Project

## 📌 Project Overview

This project focuses on analyzing restaurant data from Zomato to uncover insights about restaurant distribution, customer ratings, cuisines, pricing, city-wise performance, and online delivery services.

The project combines **SQL, Python, Exploratory Data Analysis (EDA), and Power BI** to transform raw restaurant data into meaningful business insights and interactive visualizations.

The objective is to understand restaurant market trends, identify popular cuisines, analyze customer ratings, and explore how restaurant characteristics vary across cities.

---

## 🎯 Objectives

- Analyze restaurant distribution across different cities.
- Identify the most popular cuisines.
- Evaluate restaurant ratings and customer voting patterns.
- Analyze average cost for two people across restaurants.
- Understand online delivery availability.
- Identify trends and patterns using exploratory data analysis.
- Build interactive Power BI dashboards for business insights.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| SQL | Data querying and business analysis |
| MySQL | Database management |
| Power BI | Interactive dashboards |
| Jupyter Notebook | Exploratory data analysis |
| Git & GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
Zomato-Restaurant-Analysis/
│
├── data/
│   ├── raw/
│   │   └── zomato.csv
│   │
│   └── processed/
│       └── zomato_cleaned.csv
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_restaurant_analysis.sql
│   └── 03_business_insights.sql
│
├── notebooks/
│   └── zomato_eda.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── visualization.py
│   └── report_generator.py
│
├── outputs/
│   ├── graphs/
│   ├── reports/
│   │   └── Zomato_Restaurant_Analysis_Report.pdf
│   └── analysis/
│       └── business_insights.txt
│
├── powerbi/
│   └── zomato_dashboard.pbix
│
└── README.md
```

---

## 📊 Dataset Overview

The dataset contains restaurant information from different cities, including ratings, cuisines, cost, votes, and online delivery availability.

### Dataset Statistics

| Metric | Value |
|---|---:|
| Total Restaurants | 9,551 |
| Unique Cities | 141 |
| Duplicate Records | 0 |
| Missing Cuisine Values | 9 |
| Restaurants with Rating 0 | 2,148 |

### Key Columns

| Column | Description |
|---|---|
| `restaurant_id` | Unique restaurant identifier |
| `restaurant_name` | Name of the restaurant |
| `city` | City where the restaurant operates |
| `cuisines` | Types of cuisines offered |
| `has_online_delivery` | Online delivery availability |
| `aggregate_rating` | Overall restaurant rating |
| `votes` | Number of customer votes |
| `average_cost_for_two` | Approximate cost for two people |

---

## 🔍 Project Workflow

### 1️⃣ Data Cleaning & Preprocessing

- Checked for duplicate records.
- Identified missing values.
- Handled missing cuisine information.
- Analyzed restaurants with zero ratings.
- Prepared the dataset for analysis and visualization.
- Exported the cleaned dataset for further use.

### 2️⃣ SQL Analysis

Used SQL to perform restaurant-related analysis and extract business insights.

Key analysis areas:

- Restaurant count by city.
- Top restaurants based on ratings and votes.
- City-wise restaurant distribution.
- Cuisine-related analysis.
- Average cost analysis.
- Online delivery availability.
- Rating-based restaurant analysis.

### 3️⃣ Exploratory Data Analysis (Python)

Performed EDA using Pandas, Matplotlib, and Seaborn to understand the dataset and discover trends.

### 📈 Visualizations Created

- Restaurant Rating Distribution
- Cuisine Count Analysis
- City-wise Restaurant Count
- Price Range Distribution
- Online Delivery Distribution
- Average Cost Distribution
- Votes vs Ratings Analysis
- Rating Box Plot
- Correlation Heatmap
- Pairplot Analysis

### 4️⃣ Power BI Dashboard

Created interactive dashboards to present restaurant data in a visually understandable and business-friendly format.

#### Dashboard 1 — Restaurant Overview

Provides an overall summary of restaurant data.

Key metrics and visualizations:

- Total Restaurants
- Average Restaurant Rating
- Total Cities
- Online Delivery Percentage
- Top Cities by Restaurant Count
- Top Cuisines
- Online Delivery Distribution
- Rating Distribution

#### Dashboard 2 — City Analysis

Focuses on restaurant distribution and performance across different cities.

Key analysis:

- City-wise restaurant distribution
- Top cities with the highest number of restaurants
- Average ratings across cities
- Average cost for two across cities
- City-level comparison and filtering

Interactive slicers allow users to explore the data dynamically.

---

## 💡 Key Business Insights

- The dataset contains **9,551 restaurants across 141 cities**.
- New Delhi represents the largest restaurant concentration in the dataset, with **5,473 restaurants**.
- **2,148 restaurants** have a rating of zero, highlighting the importance of separating unrated restaurants from rated restaurants during rating analysis.
- Online delivery is available at **2,451 restaurants**, while **7,100 restaurants** do not offer online delivery.
- Cuisine information was missing for a small number of restaurants and was handled during data cleaning.

These insights help understand restaurant market concentration, rating coverage, and online delivery adoption.

---

## 📉 Business Use Cases

This analysis can help:

- Restaurant owners understand market competition.
- Business analysts identify high-density restaurant markets.
- Customers explore restaurant trends and rating patterns.
- Businesses evaluate online delivery adoption.
- Decision-makers compare restaurant pricing and performance across cities.
- Marketing teams identify potential markets for expansion.

---

## 📸 Dashboard Preview

### Restaurant Overview Dashboard

> Add your Restaurant Overview dashboard screenshot here.

```text
![Restaurant Overview Dashboard](images/restaurant_overview.png)
```

### City Analysis Dashboard

> Add your City Analysis dashboard screenshot here.

```text
![City Analysis Dashboard](images/city_analysis.png)
```

---

## 📑 Project Report

A PDF report containing the analysis and visualizations is also available in the project:

`outputs/reports/Zomato_Restaurant_Analysis_Report.pdf`

---

## 🚀 How to Run the Project

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Zomato-Restaurant-Analysis.git
```

### Step 2 — Navigate to the Project Folder

```bash
cd Zomato-Restaurant-Analysis
```

### Step 3 — Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter reportlab
```

### Step 4 — Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/zomato_eda.ipynb
```

Run the notebook cells sequentially to explore the data and perform the analysis.

### Step 5 — Run SQL Analysis

- Open MySQL Workbench.
- Execute `01_database_setup.sql` to create the database and table.
- Import the dataset into the database.
- Run `02_restaurant_analysis.sql` for analytical queries.
- Run `03_business_insights.sql` for business-focused analysis.

### Step 6 — Explore the Power BI Dashboard

Open the Power BI file:

```text
powerbi/zomato_dashboard.pbix
```

Explore the interactive dashboard using the available slicers and visualizations.

---

## 📌 Skills Demonstrated

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- SQL Querying & Data Analysis
- MySQL Database Management
- Data Visualization
- Dashboard Development
- Business Insight Generation
- Python Data Analytics
- Analytical Thinking

---

## 👨‍💻 Author

**Hrishi Dahake**

Aspiring Data Analyst | Python | SQL | Power BI | Data Visualization

- GitHub: [GitHub Profile](https://github.com/Hrishi-10k)
- LinkedIn: [LinkedIn Profile](https://linkedin.com/in/hrishi-10k)

---

⭐ If you found this project interesting, feel free to explore the repository and connect with me!

