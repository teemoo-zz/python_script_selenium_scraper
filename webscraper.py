from bs4 import BeautifulSoup
import requests
import pandas as pd

# Select the URL to scrape from
URL = 'https://coinmarketcap.com/'

# http request
webpage = requests.get(URL)

# Check the website content
webpage.content
type(webpage.content)

# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "html.parser")

# Find all elements containing cryptocurrency data
crypto_rows = soup.find_all('tr')

# Initialize lists to store data
rankings = []
names = []
tickers = []
prices = []
volumes = []

# Extract data from each row
for row in crypto_rows:
    # Rank
    rank_element = row.find('p', class_='sc-71024e3e-0 jBOvmG')
    rank = rank_element.text.strip() if rank_element else 'N/A'
    rankings.append(rank)
    
    # Name
    name_element = row.find('p', class_='sc-71024e3e-0 ehyBa-d')
    name = name_element.text.strip() if name_element else 'N/A'
    names.append(name)
    
    # Ticker
    ticker_element = row.find('p', class_='sc-71024e3e-0 OqPKt coin-item-symbol')
    ticker = ticker_element.text.strip() if ticker_element else 'N/A'
    tickers.append(ticker)
    
    # Price
    price_element = row.find('span')
    price = price_element.text.strip() if price_element else 'N/A'
    prices.append(price)
    
    # Volume
    volume_element = row.find('p', class_='sc-71024e3e-0 bbHOdE font_weight_500')
    volume = volume_element.text.strip() if volume_element else 'N/A'
    volumes.append(volume)

# Create a pandas DataFrame
crypto_data = pd.DataFrame({
    'Rank': rankings,
    'Name': names,
    'Ticker': tickers,
    'Price': prices,
    'Volume': volumes
})

# Drop the first row explicitly
crypto_data = crypto_data.drop(crypto_data.index[0])

# Display all rows in the DataFrame without the index column
pd.set_option('display.max_rows', None)  # Display all rows
print(crypto_data.to_string(index=False))

# Use pandas styling to make the DataFrame look better
styled_df = crypto_data.style.set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#404040'), ('color', 'white'), ('font-weight', 'bold')]},
    {'selector': 'tr:nth-of-type(odd)', 'props': [('background-color', '#f2f2f2')]},
    {'selector': 'tr:nth-of-type(even)', 'props': [('background-color', 'white')]},
    {'selector': 'td', 'props': [('text-align', 'center')]}
]).set_properties(**{'font-size': '12pt', 'font-family': 'Arial'})

# Display the styled DataFrame
styled_df
