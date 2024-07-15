import pandas as pd

# Load the CSV Files
landing_pages_file = 'landing_pages_search.csv'
affiliates_file = 'MyAffiliates - Affiliate Report.csv'

landing_pages = pd.read_csv(landing_pages_file)
affiliates = pd.read_csv(affiliates_file)

# Request to the user to input the Blocked Domain URL
domain = input("Insert an Ad-Server Domain Address (i.e. cdnt3.cldfrbcdn302.com): ")

# Filter the file landing_pages by Tracking Domain
filtered_landing_pages = landing_pages[landing_pages['Tracking Domain'] == domain][['Landing Page ID', 'Channels']]

# Verify if there are results after the filter
if filtered_landing_pages.empty:
    print(f"There are not Landing Pages for that domain {domain}.")
else:
    # Merge the filtered file with affiliates using 'Landing Page ID'
    merged_data = pd.merge(filtered_landing_pages, affiliates, on='Landing Page ID', how='inner')

    # Select the desired Columns for the excel file 
    result = merged_data[['Affiliate ID', 'Affiliate', 'Landing Page', 'Landing Page ID', 'Channels', 'Clicks', 'Signups', 'NDC', 'Deposits']]

    # Save the Excel File
    output_file = f'{domain}_affiliate_report.xlsx'
    result.to_excel(output_file, index=False, engine='openpyxl')

    print(f'File Saved Successfully as  {output_file}.')
