# Sales Analysis Pipeline
### Project Overview
To design an end-to-end Databricks ETL pipeline for sales analysis. Apply medallion architecture and use all the Databricks advanced features. Using data visualization provided by Databricks itself. End result we target achievement.
### Solution Architecture
####1. Architecture Overview

I have used Databricks features and created an **end-to-end ETL** pipeline. I have used the medallion architecture **(Bronze, Silver, Gold)** pattern. I have written all code in class and object style, because we can easily achieve scalable, reliable transformations and business-ready analytics for sales data.
The architecture uses Databricks **Auto Loader, Structured Streaming, Delta Lake, and Unity Catalog**. Using **SCD Type 1** and **SCD Type 2**.
In this project, <br/>I ensure data quality, reliability, and governance.

**Project folder structure**</br>

Hackathon2026-Sales-Analytics/</br>
├── config</br>
│ └── metadata_setup.py</br>
├── dashboard</br>
├── docs</br>
│ └── README.md</br>
├── etl</br>
│ ├── bronze</br>
│ │ ├── bronze_order_details_ingest</br>
│ │ ├── bronze_orders_ingest</br>
│ │ └── bronze_sales_target_ingest</br>
│ ├── silver</br>
│ │ ├── silver_actual_orders_transform</br>
│ │ ├── silver_order_items_transform</br>
│ │ ├── silver_orders_transform</br>
│ │ ├── silver_return_orders_transform</br>
│ │ └── silver_sales_targets_transform</br>
│ └── gold</br>
│ └──── gold_sales_facts</br>
├── setup</br>
│ └── create_tables</br>
└── temp</br>

**ETL Workflow Diagram**
</br>
!['etl'](ETL-workflow-diagram)

!['timeline'](timeline)

####2. Source Systems
The pipeline ingests data from **CSV** file, including:
- Orders
- Order Details
- Sales Targets

####3. Bronze Layer - Raw Ingestion
**Purpose**: Capture raw data with minimal transformation.

Key Characteristics:
- Ingestion using Auto Loader (cloudFiles)
- Structured Streaming for incremental loads
- Schema evolution mode use the **rescue**
- **rescue** columns are captured to easily handle unexpected schema changes.
- Uses the **availableNow trigger**.
- Raw data stored in Delta format

**Output:**
- bronze_orders
- bronze_order_details
- bronze_sales_target

####4. Silver Layer

**Purpose**: Apply business rules and data quality transformations.

**Key Transformations:**
- Data cleansing and type casting
- Deduplication
- Separation of actual orders and return orders
- Standardization of columns
- Enrichment through joins

**Output:**
- silver_orders
- silver_order_items
- silver_actual_orders
- silver_return_orders
- silver_sales_targets

####5. Gold Layer
**Purpose:** Provide analytics-ready tables for reporting and decision-making.

**Key Features:**

- Aggregations and KPIs
- Revenue and profit calculations
- Target vs actual comparisons
- Time-based analytics (daily / monthly)

**Output**:
- gold_daily_sales_summary
- gold_sales_facts
- gold_monthly_profit_vs_target
- gold_profit_target_metrics

####6. Data Processing & Orchestration
End-to-end processing uses Structured Streaming

- Checkpointing ensures fault tolerance
- Delta Lake provides **ACID** compliance
- Jobs can be orchestrated using Databricks Workflows

####7. Visualization & Consumption
Gold tables are consumed directly using Databricks SQL dashboards

Built-in visualizations provide insights into:

**Sales KPI**
- Total Revenue by Month (Line Chart)
- Top 10 Products by Revenue (Bar chart)

**Customer Insights**
- Customer Segmentatikon by Purchase Frequency (Pie Chart)
- Top Customers by Spend (Bar Chart)

**Product Performance**
- Quantity Sold by Product Category (Bar Chart)

**Operational Efficency**
- Order Processed per day (Line Chart)
- Cancelled Orders Trend (Bar Chart)

####8. Conclusion

This architecture demonstrates a **production-grade ETL solution** using Databricks best practices, delivering reliable, scalable, and business-focused analytics through the Medallion Architecture.