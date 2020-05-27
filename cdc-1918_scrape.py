#Web scraping cdc 1918 pandemic flue
import os
from lxml import html
import csv
import requests

#create parser object
response = requests.get(url="https://www.cdc.gov/flu/pandemic-resources/1918-commemoration/pandemic-timeline-1918.htm"
)

tree = html.fromstring(html=response.text)

# Datastores for the different html tags
title = []
para = []
cardttl = []
cardtext = []

# Use Xpath for traversing thru a nested div structure
title = tree.xpath("//h1[contains (@id,'content')]/text()")
para = tree.xpath("//div[contains (@class,'card-body p-0')]/p/text()")
card_ttl = tree.xpath("//div[@class='card-body']/h5/text()")
card_body = tree.xpath("//div[@class='card-body']/ul/li/text()")

# Typecast lists and combined together
cdc_intro = zip(title, para)
cardlist = list(card_ttl)
cardbody = list(card_body)
cdc_list = [cardlist, cardbody]

# Setup the output CSV file
output_file = os.path.join("cardbody.csv")

# Generate the CSV file
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
# Write the headers
    writer.writerow(["Card Header", "Card Text"])
# Write the intro headline and paragraph
    writer.writerows(cdc_intro)
# Write the each of the entries and rows
    writer.writerows(cdc_list)













