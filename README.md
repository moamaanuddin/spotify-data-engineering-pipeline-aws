# 🎵 Spotify Data Engineering Pipeline on AWS

<p align="center">
  <img src="architecture/architecture.png" width="850">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AWS-S3-orange?style=for-the-badge&logo=amazonaws">
  <img src="https://img.shields.io/badge/AWS-Glue-yellow?style=for-the-badge&logo=amazonaws">
  <img src="https://img.shields.io/badge/AWS-Athena-blue?style=for-the-badge&logo=amazonaws">
  <img src="https://img.shields.io/badge/Data-Engineering-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/SQL-Analytics-red?style=for-the-badge">
</p>

---

## 🌟 Project Highlights

✅ Built an End-to-End Serverless Data Pipeline

✅ Processed Spotify Music Data using AWS Glue

✅ Converted Raw CSV Data into Optimized Parquet Files

✅ Automated Metadata Discovery using AWS Glue Crawlers

✅ Queried Data using Amazon Athena

✅ Implemented Modern Data Lake & Data Warehouse Architecture

---

## 🎯 Project Objective

This project demonstrates how modern Data Engineering pipelines are built using AWS cloud services.

The pipeline ingests Spotify datasets from Amazon S3, transforms them using AWS Glue Studio, stores analytics-ready data in Parquet format, catalogs metadata using AWS Glue Crawlers, and enables analytical querying using Amazon Athena.

---

## 🏗️ Architecture

```text
Spotify Dataset
       │
       ▼
📦 Amazon S3 (Raw Layer)
       │
       ▼
⚙️ AWS Glue Studio ETL
       │
       ▼
🗄️ S3 Data Warehouse (Parquet)
       │
       ▼
🕷️ AWS Glue Crawler
       │
       ▼
📚 AWS Data Catalog
       │
       ▼
🔍 Amazon Athena
       │
       ▼
📊 Amazon QuickSight (Planned)
```

---
spotify-data-engineering-pipeline-aws/
│
├── README.md
│
├── architecture/
│   └── architecture.png
│
├── screenshots/
│   ├── s3-staging.png
│   ├── s3-datawarehouse.png
│   ├── glue-etl-workflow.png
│   ├── glue-crawler.png
│   ├── athena-top-tracks.png
│   └── athena-genre-analysis.png
│
├── sql/
│   ├── top_tracks.sql
│   ├── top_artists.sql
│   ├── genre_analysis.sql
│   └── label_analysis.sql
│
└── glue-scripts/
    └── etl_job.py
## ☁️ AWS Services Used

| Service              | Purpose             |
| -------------------- | ------------------- |
| 📦 Amazon S3         | Data Lake Storage   |
| ⚙️ AWS Glue Studio   | ETL Processing      |
| 🕷️ AWS Glue Crawler | Schema Discovery    |
| 📚 Glue Data Catalog | Metadata Management |
| 🔍 Amazon Athena     | SQL Analytics       |
| 🔐 IAM               | Access Management   |
| 📊 QuickSight        | Visualization Layer |

---

## 📂 Dataset Information

🎵 Dataset: Spotify Dataset 2023

👤 Author: Tony Gordon Jr.

🔗 Source:

https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023

### Files Used

```text
artists.csv
albums.csv
track.csv
```

---

## 🔄 ETL Workflow

### Step 1 — Data Ingestion 📥

Raw Spotify CSV files are uploaded to Amazon S3.

### Step 2 — Data Transformation ⚙️

AWS Glue Studio performs:

* Dataset joins
* Schema mapping
* Data cleansing
* Column selection
* CSV → Parquet conversion

### Step 3 — Data Warehouse 🗄️

Curated data is stored in Amazon S3 using Parquet format.

### Step 4 — Metadata Discovery 🕷️

AWS Glue Crawler scans the warehouse and creates tables automatically.

### Step 5 — Analytics 🔍

Athena queries generate business insights directly from S3.

---

## 📸 Project Screenshots

### 📦 S3 Data Lake

![S3](screenshots/s3-staging-layer.png)

---

### ⚙️ AWS Glue Studio Workflow

![Glue ETL](screenshots/glue-etl-workflow.png)

---

### 🕷️ AWS Glue Crawler

![Crawler](screenshots/glue-crawler.png)

---

### 🔍 Athena Analytics

![Athena](screenshots/athena-top-tracks.png)

---

## 📈 Sample Business Insights

### 🎶 Most Popular Tracks

| Track                           | Artist       | Popularity |
| ------------------------------- | ------------ | ---------- |
| Cruel Summer                    | Taylor Swift | 99         |
| All I Want For Christmas Is You | Mariah Carey | 99         |
| My Love Mine All Mine           | Mitski       | 98         |

---

### 🔥 Top Analytics Performed

* Top Artists by Followers
* Genre Popularity Analysis
* Label Performance Analysis
* Album Popularity Trends
* Music Release Trends
* Track Duration Analysis

---

## 📊 Future Dashboard (QuickSight)

Planned visualizations:

📈 Genre Popularity Dashboard

📈 Top Artists Dashboard

📈 Track Popularity Dashboard

📈 KPI Dashboard

📈 Music Trend Analysis

---

## 🧠 Skills Demonstrated

### Data Engineering

* ETL Development
* Data Warehousing
* Data Lake Architecture
* Metadata Management

### AWS

* Amazon S3
* AWS Glue Studio
* AWS Glue Crawlers
* AWS Athena
* IAM

### Analytics

* SQL
* Athena
* Data Transformation
* Business Intelligence

---

## 🚀 Project Impact

✔️ Built a scalable serverless architecture

✔️ Automated schema discovery

✔️ Improved query efficiency using Parquet

✔️ Enabled SQL analytics without provisioning servers

✔️ Demonstrated real-world Data Engineering workflow

---

## 👨‍💻 Author

### Mohammed Amaanuddin

🚀 Data Engineer

☁️ AWS | Python | SQL | Spark | Data Engineering

⭐ If you found this project useful, consider giving it a star!
