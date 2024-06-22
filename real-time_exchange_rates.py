import requests
import pandas as pd

# Configuration
API_KEY = '6316a80b0ee8409eb07092d0'
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

# Fetch real-time exchange rate
response = requests.get(API_URL)
data = response.json()

# Extract USD to INR rate
usd_to_inr = data['conversion_rates']['INR']

# Create a DataFrame for the exchange rate
exchange_rate_df = pd.DataFrame({
    'currency': ['USD'],
    'exchange_rate': [usd_to_inr]
})

# Save the exchange rate to a CSV file
exchange_rate_df.to_csv('exchange_rate.csv', index=False)
