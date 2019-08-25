words = ['buy', 'price', 'discount', 'promotion', 'promo', 'shop', 
         'buying', 'prices', 'pricing', 'shopping', 'discounts', 
         'promos', 'ecommerce', 'e commerce', 'buy online',
         'shop online', 'cheap', 'best price', 'lowest price',
         'cheapest', 'best value', 'offer', 'offers', 'promotions',
         'purchase', 'sale', 'bargain', 'affordable',
         'cheap', 'low cost', 'low price', 'budget', 'inexpensive', 'economical']
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

print(words)
# Create an empty list
keywords_list = list()

# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)

# Create a DataFrame from list
import  pandas as pd
keywords_df = pd.DataFrame.from_records(keywords_list)
print(keywords_df)

# Rename the columns of the DataFrame
keywords_df.columns = ["Ad Group", "Keyword"]

# Add a campaign column
keywords_df["Campaign"] = "SEM_Sofas"

# Add a criterion type column
keywords_df["Criterion Type"] = "Exact"

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase["Criterion Type"] = "Phrase"

# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)

print(keywords_df_final)

# Save to CSV
keywords_df_final.to_csv('TesteGoogleKW.csv', index=False)
