# data_loader.py
from ucimlrepo import fetch_ucirepo
import pandas as pd

def load_online_retail_data():
    # Fetch dataset from UCI ML repository
    online_retail = fetch_ucirepo(id=352)
    # Convert features to pandas DataFrame
    df = pd.DataFrame(online_retail.data.features)
    # Display metadata for reference
    print(online_retail.metadata)
    # Return the DataFrame
    return df
