import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)
df['year'] = pd.to_datetime(df['date']).dt.year

def get_big_mac_price_by_year(year,country_code):
    df_filtered = df[(df["year"] == year) & (df["iso_a3"] == country_code.upper())] #Ai helped me write the boolean expression and series
    mean_price = df_filtered["dollar_price"].mean() 
    return round(mean_price, 2) #Ai helped me write the round function to get it to 2 decimal places 

def get_big_mac_price_by_country(country_code):
    df_filtered = df[df["iso_a3"] == country_code.upper()] #Ai helped me write the boolean expression and series
    mean_price = df_filtered["dollar_price"].mean() 
    mean_price = df_filtered["dollar_price"].mean()
    return round(mean_price, 2) #Ai helped me write the round function to get it to 2 decimal places 
   
def get_the_cheapest_big_mac_price_by_year(year):
    df_filtered = df[df["year"] == year]
    min_row = df_filtered.loc[df_filtered["dollar_price"].idxmin()] #Ai helped me write this
    country_name = min_row["name"]
    country_code = min_row["iso_a3"]
    dollar_price = min_row["dollar_price"]
    return f"{country_name}({country_code}): ${dollar_price:.2f}" #Ai helped me write this 

def get_the_most_expensive_big_mac_price_by_year(year):
    df_filtered = df[df["year"] == year]
    max_row = df_filtered.loc[df_filtered["dollar_price"].idxmax()] #Ai helped me write this 
    country_name = max_row["name"]
    country_code = max_row["iso_a3"]
    dollar_price = max_row["dollar_price"] 
    return f"{country_name}({country_code}): ${dollar_price:.2f}" #Ai helped me write this 

if __name__ == "__main__":
    print("Price in Malaysia (MYS) in 2008:", get_big_mac_price_by_year(2008, "mys"))
    print("Average price in Malaysia (MYS) overall:", get_big_mac_price_by_country("mys"))
    print("Cheapest Big Mac in 2008:", get_the_cheapest_big_mac_price_by_year(2008))
    print("Most expensive Big Mac in 2003:", get_the_most_expensive_big_mac_price_by_year(2003))

# CITATION / AI USAGE
# ----------------------------------------------------------------------------
# AI Assistance: Line 7
# Reference: Chat-GPT 4. (2025, March 22). "Show me an example code line to filter a DataFrame where 'year' equals a variable" Generated using OpenAI Chat-GPT. https://chat.openai.com/

# AI Assistance: Line 9
# Reference: Chat-GPT 4. (2025, March 22). "Show me a code line that rounds mean_price to 2 decimals and returns it." Generated using OpenAI Chat-GPT. https://chat.openai.com/

# AI Assistance: Line 12
# Reference: Chat-GPT 4. (2025, March 22). "Show me an example code line to filter a DataFrame where 'iso_a3' equals an uppercase country code." Generated using OpenAI Chat-GPT. https://chat.openai.com/

# AI Assistance: Line 15
# Reference: Chat-GPT 4. (2025, March 22). "Show me a code line that rounds mean_price to 2 decimals and returns it." Generated using OpenAI Chat-GPT. https://chat.openai.com/

# AI Assistance: Line 19
# Reference: Chat-GPT 4. (2025, March 22). "Can you show me a quick example of filtering a pandas DataFrame by a given year and an uppercase country code?" Generated using OpenAI Chat-GPT. https://chat.openai.com/

# AI Assistance: Line 23
# Reference: Chat-GPT 4. (2025, March 22). "Show me a code example to format a string with country name, country code, and dollar price (rounded to 2 decimals)." Generated using OpenAI Chat-GPT. https://chat.openai.com/

# AI Assistance: Line 27
# Reference: Chat-GPT 4. (2025, March 22). "Show me a code example that retrieves the row with the maximum 'dollar_price' using idxmax() and loc." Generated using OpenAI Chat-GPT. https://chat.openai.com/

# AI Assistance: Line 31
# Reference: Chat-GPT 4. (2025, March 22). "This is how im suppose to use f-strings for formatting output (included text from khan code academy). Can you walk me through this?" Generated using OpenAI Chat-GPT. https://chat.openai.com/