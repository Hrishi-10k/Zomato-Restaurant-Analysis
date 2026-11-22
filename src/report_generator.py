from pathlib import Path
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak,
)

# ---------------------------------------------------------
# PROJECT PATHS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "zomato_cleaned.csv"
INSIGHTS_PATH = BASE_DIR / "outputs" / "analysis" / "business_insights.txt"
GRAPH_DIR = BASE_DIR / "outputs" / "graphs"
REPORT_DIR = BASE_DIR / "outputs" / "reports"

REPORT_DIR.mkdir(parents=True, exist_ok=True)

PDF_PATH = REPORT_DIR / "Zomato_Restaurant_Analysis_Report.pdf"


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

df = pd.read_csv(DATA_PATH)

rated_df = df[df["aggregate_rating"] > 0]

total_restaurants = len(df)
total_cities = df["city"].nunique()
total_cuisines = df["cuisines"].nunique()

average_rating = rated_df["aggregate_rating"].mean()
highest_rating = rated_df["aggregate_rating"].max()

online_delivery_count = (
    df["has_online_delivery"].str.strip().str.lower() == "yes"
).sum()

online_delivery_percentage = (online_delivery_count / total_restaurants) * 100

average_cost = df["average_cost_for_two"].mean()

top_city = df["city"].value_counts().idxmax()

cuisine_df = df.assign(
    cuisines=df["cuisines"].fillna("Unknown").str.split(",")
).explode("cuisines")

cuisine_df["cuisines"] = cuisine_df["cuisines"].str.strip()

cuisine_counts = cuisine_df[cuisine_df["cuisines"] != "Unknown"][
    "cuisines"
].value_counts()

top_cuisine = cuisine_counts.index[0] if not cuisine_counts.empty else "N/A"


# ---------------------------------------------------------
# READ BUSINESS INSIGHTS
# ---------------------------------------------------------

if INSIGHTS_PATH.exists():
    business_insights = INSIGHTS_PATH.read_text(encoding="utf-8")
else:
    business_insights = (
        "Business insights file was not found. "
        "Please generate it from the EDA notebook."
    )


# ---------------------------------------------------------
# PDF DOCUMENT SETTINGS
# ---------------------------------------------------------

document = SimpleDocTemplate(
    str(PDF_PATH),
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=45,
    bottomMargin=45,
)

styles = getSampleStyleSheet()

styles.add(
    ParagraphStyle(
        name="ReportTitle",
        parent=styles["Title"],
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#C62828"),
        spaceAfter=20,
    )
)

styles.add(
    ParagraphStyle(
        name="SectionHeading",
        parent=styles["Heading1"],
        fontSize=17,
        leading=22,
        textColor=colors.HexColor("#B71C1C"),
        spaceBefore=12,
        spaceAfter=10,
    )
)

styles.add(
    ParagraphStyle(
        name="SubHeading",
        parent=styles["Heading2"],
        fontSize=12,
        textColor=colors.HexColor("#333333"),
        spaceBefore=8,
        spaceAfter=6,
    )
)

styles.add(
    ParagraphStyle(
        name="BodyTextCustom",
        parent=styles["BodyText"],
        fontSize=9,
        leading=14,
        spaceAfter=8,
    )
)

story = []


# ---------------------------------------------------------
# COVER PAGE
# ---------------------------------------------------------

story.append(Spacer(1, 1.3 * inch))

story.append(Paragraph("ZOMATO RESTAURANT ANALYSIS", styles["ReportTitle"]))

story.append(
    Paragraph("Data Analysis & Business Intelligence Report", styles["Heading2"])
)

story.append(Spacer(1, 25))

story.append(Paragraph("Project Objective", styles["SectionHeading"]))

story.append(
    Paragraph(
        "This project analyzes restaurant data to identify customer "
        "preferences, popular cuisines, restaurant ratings, pricing "
        "patterns, city-wise distribution, and online delivery trends.",
        styles["BodyTextCustom"],
    )
)

story.append(Spacer(1, 20))

story.append(Paragraph("Technologies Used", styles["SectionHeading"]))

story.append(
    Paragraph(
        "Python | Pandas | NumPy | Matplotlib | Seaborn | MySQL | ReportLab",
        styles["BodyTextCustom"],
    )
)

story.append(Spacer(1, 30))

story.append(Paragraph("Generated Automatically Using Python", styles["Italic"]))

story.append(PageBreak())


# ---------------------------------------------------------
# EXECUTIVE SUMMARY
# ---------------------------------------------------------

story.append(Paragraph("1. Executive Summary", styles["SectionHeading"]))

summary = (
    f"This analysis covers <b>{total_restaurants:,}</b> restaurant "
    f"records across <b>{total_cities:,}</b> cities. "
    f"The dataset contains <b>{total_cuisines:,}</b> distinct cuisine "
    f"entries. The average rating among rated restaurants is "
    f"<b>{average_rating:.2f}</b>, and the highest observed rating is "
    f"<b>{highest_rating:.2f}</b>. "
    f"Online delivery is available at approximately "
    f"<b>{online_delivery_percentage:.2f}%</b> of restaurants. "
    f"<b>{top_city}</b> has the largest number of restaurant records, "
    f"while <b>{top_cuisine}</b> is the most frequently listed cuisine."
)

story.append(Paragraph(summary, styles["BodyTextCustom"]))


# ---------------------------------------------------------
# DATASET OVERVIEW
# ---------------------------------------------------------

story.append(Paragraph("2. Dataset Overview", styles["SectionHeading"]))

overview_data = [
    ["Metric", "Value"],
    ["Total Restaurants", f"{total_restaurants:,}"],
    ["Total Cities", f"{total_cities:,}"],
    ["Distinct Cuisine Entries", f"{total_cuisines:,}"],
    ["Rated Restaurants", f"{len(rated_df):,}"],
    ["Restaurants Not Rated", f"{total_restaurants-len(rated_df):,}"],
    ["Average Restaurant Rating", f"{average_rating:.2f}"],
    ["Highest Restaurant Rating", f"{highest_rating:.2f}"],
    ["Online Delivery Restaurants", f"{online_delivery_count:,}"],
    ["Online Delivery Percentage", f"{online_delivery_percentage:.2f}%"],
    ["Average Cost for Two", f"{average_cost:,.2f} dataset units"],
    ["Most Represented City", top_city],
    ["Most Popular Cuisine", top_cuisine],
]

overview_table = Table(overview_data, colWidths=[240, 230])

overview_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#B71C1C")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            (
                "ROWBACKGROUNDS",
                (0, 1),
                (-1, -1),
                [colors.white, colors.HexColor("#F5F5F5")],
            ),
            ("PADDING", (0, 0), (-1, -1), 7),
        ]
    )
)

story.append(overview_table)


# ---------------------------------------------------------
# DATA CLEANING SUMMARY
# ---------------------------------------------------------

story.append(Paragraph("3. Data Cleaning & Preparation", styles["SectionHeading"]))

cleaning_points = [
    "Loaded the original restaurant dataset using Pandas.",
    "Handled missing cuisine values using an Unknown category.",
    "Removed duplicate records.",
    "Standardized column names and text formatting.",
    "Identified zero ratings as Not Rated instead of genuine zero-star ratings.",
    "Prepared the cleaned dataset for analysis and visualization.",
]

for point in cleaning_points:
    story.append(Paragraph(f"• {point}", styles["BodyTextCustom"]))


# ---------------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------------

story.append(Paragraph("4. Business Insights", styles["SectionHeading"]))

for line in business_insights.splitlines():
    line = line.strip()

    if line:
        story.append(Paragraph(line, styles["BodyTextCustom"]))


# ---------------------------------------------------------
# VISUALIZATION SECTION
# ---------------------------------------------------------

story.append(PageBreak())

story.append(Paragraph("5. Data Visualizations", styles["SectionHeading"]))

charts = [
    ("01_rating_histogram.png", "Restaurant Rating Distribution"),
    ("02_cuisine_count.png", "Top 10 Most Popular Cuisines"),
    ("03_city_restaurant_count.png", "Top 10 Cities by Restaurant Count"),
    ("04_price_range_pie.png", "Restaurant Distribution by Cost Range"),
    ("05_online_delivery_count.png", "Online Delivery Availability"),
    ("06_cost_distribution.png", "Average Cost Distribution"),
    ("07_votes_scatter.png", "Customer Votes vs Ratings"),
    ("08_rating_boxplot.png", "Restaurant Rating Box Plot"),
    ("09_correlation_heatmap.png", "Correlation Heatmap"),
    ("10_pairplot.png", "Restaurant Features Pair Plot"),
]

for filename, title in charts:

    image_path = GRAPH_DIR / filename

    if image_path.exists():

        story.append(Paragraph(title, styles["SubHeading"]))

        chart = Image(str(image_path))

        chart_width = 6.2 * inch
        chart_height = 4.0 * inch

        chart.drawWidth = chart_width
        chart.drawHeight = chart.imageHeight * chart_width / chart.imageWidth

        max_height = 4.2 * inch

        if chart.drawHeight > max_height:
            chart.drawHeight = max_height

        story.append(chart)
        story.append(Spacer(1, 15))

    else:
        story.append(
            Paragraph(f"Visualization not found: {filename}", styles["BodyTextCustom"])
        )


# ---------------------------------------------------------
# CONCLUSION
# ---------------------------------------------------------

story.append(PageBreak())

story.append(Paragraph("6. Conclusion", styles["SectionHeading"]))

conclusion = (
    "The Zomato Restaurant Analysis project demonstrates how data "
    "analysis can uncover useful patterns in restaurant distribution, "
    "ratings, cuisines, pricing, customer votes, and online delivery. "
    "The findings can support business decisions related to restaurant "
    "performance, customer preferences, and market opportunities. "
    "The cleaned dataset and visualizations can also be used to build "
    "interactive dashboards in Power BI."
)

story.append(Paragraph(conclusion, styles["BodyTextCustom"]))


# ---------------------------------------------------------
# GENERATE PDF
# ---------------------------------------------------------

document.build(story)

print("PDF report generated successfully!")
print(f"Report location: {PDF_PATH}")
