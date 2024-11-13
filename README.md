# Online Retail Data Analysis Project

This project analyzes transactional data from an online retail store, leveraging data cleaning, integration, transformation, exploratory data analysis (EDA), and feature engineering to extract insights. The dataset used is from the UCI ML Repository, containing transactions for a UK-based online retailer between 01/12/2010 and 09/12/2011.

## Project Structure

- **data_loader.py**: This script loads the dataset from the UCI ML Repository. It first fetches the dataset metadata and features using `ucimlrepo`, and then loads `InvoiceNo` and `StockCode` directly from the repository’s CSV file. This ensures all columns are included in the final dataset.
  
- **data_acquisition_and_EDA.ipynb**: This notebook performs data acquisition, cleaning, integration, transformation, and exploratory data analysis. Key steps include:
  - Handling missing values and duplicate transactions.
  - Filtering canceled transactions, transforming date and price information, and creating customer-level metrics.
  - Exploratory Data Analysis (EDA) to explore transaction frequency, top-selling products, customer demographics, seasonal patterns, and more.

## Installation Guide

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Aditya-gam/Online-Retail-Data-Analysis.git
cd Online-Retail-Data-Analysis
```

### 2. Set Up a Virtual Environment

To avoid dependency conflicts, create and activate a virtual environment:

```bash
python -m venv online_retail_env
Mac: source online_retail_env/bin/activate  
Windows: online_retail_env\Scripts\activate
```

### 3. Install Required Packages

Install all required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run Data Loading Script

To load the dataset, you can use the `data_loader.py` file. This will fetch the necessary columns and create a clean dataset for further analysis:

```python
# In Python or Jupyter Notebook
from data_loader import load_online_retail_data
df = load_online_retail_data()
```

### 5. Run the Data Acquisition and EDA Notebook

Open the `data_acquisition_and_EDA.ipynb` notebook to perform data cleaning, integration, transformation, and exploratory analysis. Run the cells sequentially for a complete data analysis workflow.

You can find the cleaned and modified dataset after running `data_acquisition_and_EDA.ipynb` notebook in the `dataset/` directory.
