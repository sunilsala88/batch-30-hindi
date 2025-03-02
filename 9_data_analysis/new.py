import pandas as pd
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()


# Corrected raw URLs for reading CSVs directly
sp500_url = "https://raw.githubusercontent.com/sunilsala88/batch-29/main/10_data_analysis/sp500.csv"
stock_value_url = "https://raw.githubusercontent.com/sunilsala88/batch-29/main/10_data_analysis/stock_value.csv"
sbin_url = "https://raw.githubusercontent.com/sunilsala88/batch-29/main/10_data_analysis/SBIN.csv"
unicorn_companies_url = "https://raw.githubusercontent.com/sunilsala88/batch-29/main/10_data_analysis/Unicorn_companies.csv"

# Reading CSVs into DataFrames
sp500_df = pd.read_csv(sp500_url)
stock_value_df = pd.read_csv(stock_value_url)
sbin_df = pd.read_csv(sbin_url)
unicorn_companies_df = pd.read_csv(unicorn_companies_url)

# Display first few rows of one dataset as a sample
print(sp500_df.head())
