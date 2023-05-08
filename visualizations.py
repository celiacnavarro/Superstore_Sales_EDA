#Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import matplotlib.ticker as ticker
from matplotlib.colors import LinearSegmentedColormap

# Load dataset

df = pd.read_csv('data/data_cleaned.csv')

# Top 10 Spending Customers

customers = df.groupby(["Customer Name"]).sum().sort_values("Sales", ascending=False).head(10)
customers = customers[["Sales"]].round(2)
customers.reset_index(inplace=True)

color_map = LinearSegmentedColormap.from_list('my_colors', ['#1A5F7A', '#57C5B6'])

plt.title("Top Spending Customers", fontsize=14, pad=20) 
plt.bar(customers["Customer Name"], customers["Sales"], width=0.5, color=color_map(np.linspace(0, 1, len(customers))))
plt.xlabel("Customer Name",fontsize=10) 
plt.ylabel("Total Amount Spent",fontsize=10) 
plt.xticks(fontsize=8, rotation=90)
plt.yticks(fontsize=8)
for x,y in customers["Sales"].items(): 
    plt.text(x,y-8000,'$'+ str(y), fontsize=8,rotation=90, color='white',horizontalalignment='center')

plt.tight_layout()
plt.savefig('images/top_spending_customers.png')

# Top 10 Spending States

states = df.groupby(["State"]).sum().sort_values("Sales", ascending=False).head(10)
states = states[["Sales"]].round(2)
states.reset_index(inplace=True)

color_map = LinearSegmentedColormap.from_list('my_colors', ['#FF6000', '#FFA559'])

plt.title("Top Spending States", fontsize=14, pad=20) 
plt.bar(states["State"], states["Sales"], width=0.5, color=color_map(np.linspace(0, 1, len(states))))
plt.xlabel("State",fontsize=12) 
plt.ylabel("Total Amount Spent",fontsize=12) 
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=8)

for x,y in states["Sales"].items(): 
    if x == 0:
        plt.text(x,y-120000,'$'+ str(y), fontsize=8,rotation=90, color='white',horizontalalignment='center')
    else:
        plt.text(x,y+30000,'$'+ str(y), fontsize=8,rotation=90, color='black',horizontalalignment='center')

    
plt.tight_layout()
plt.savefig('images/top_spending_states.png')

# Top 10 Spending Cities

cities = df.groupby(["City"]).sum().sort_values("Sales", ascending=False).head(10)
cities = cities[["Sales"]].round(2)
cities.reset_index(inplace=True)

color_map = LinearSegmentedColormap.from_list('my_colors', ['#4D904D', '#8BE08E'])

plt.title("Top Spending Cities", fontsize=14, pad=20) 
plt.bar(cities["City"], cities["Sales"], width=0.5, color=color_map(np.linspace(0, 1, len(states))))
plt.xlabel("City",fontsize=12) 
plt.ylabel("Total Amount Spent",fontsize=12) 
plt.xticks(fontsize=8, rotation=45)
plt.yticks(fontsize=8)


for x,y in cities["Sales"].items(): 
    if x == 0:
        plt.text(x,y-70000,'$'+ str(y), fontsize=8,rotation=90, color='white',horizontalalignment='center')
    else:
        plt.text(x,y+15000,'$'+ str(y), fontsize=8,rotation=90, color='black',horizontalalignment='center')


plt.tight_layout()
plt.savefig('images/top_spending_cities.png')

# Top Selling Categories

category = df.groupby(["Category"]).sum().sort_values("Sales", ascending=False)
category = category[["Sales"]]
category.reset_index(inplace=True)

colors = ['#FD6787', '#6CA0DC', '#77DD77']

explode = (0.05,0.05,0.05)
fig1, ax1 = plt.subplots()
plt.title("Top Selling Categories", fontsize=16, pad=10) 
pie = ax1.pie(category['Sales'], colors = colors, labels=category['Category'], startangle=90, autopct='%1.1f%%', explode=explode)
for text in pie[2]:
    text.set_color('white')
    text.set_size(12)

plt.tight_layout()
plt.savefig('images/top_selling_categories.png')

# Top Selling Products

products = df.groupby(["Product Name"]).sum().sort_values("Sales",ascending=False).head(8)
products = products[["Sales"]].round(2)
products.reset_index(inplace=True)

colors = ['#FFB6C1', '#FFDAB9', '#B0C4DE', '#7de3e3', '#98FB98', '#FFA07A', '#F0E68C', '#DDA0DD']

plt.figure(figsize=(30,30))
explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05)
fig1, ax1 = plt.subplots()
plt.title("Top Selling Products", fontsize=16, pad=10) 
pie = ax1.pie(products['Sales'], colors = colors, labels=products['Product Name'], startangle=90, autopct='%1.1f%%', explode=explode)

centre_circle = plt.Circle((0,0),0.8,fc='white') 
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.tight_layout()
plt.savefig('images/top_selling_products.png', bbox_inches='tight')

# Top 10 Selling Subcategories

subcat = df.groupby(['Category','Sub-Category']).sum().sort_values("Sales", ascending=False).head(10)
subcat = subcat[["Sales"]].round(2)
subcat = subcat.sort_values("Category")
subcat.reset_index(inplace=True)

subcat_group = subcat.groupby(['Category']).sum()
subcat_group.reset_index(inplace=True)

fig, ax = plt.subplots()
ax.axis('equal')
ax.pie(subcat_group['Sales'], labels=subcat_group['Category'], autopct='%1.1f%%', startangle=90, colors=['#FD6787', '#6CA0DC', '#77DD77'], radius=1, wedgeprops=dict(edgecolor='w'))
ax2 = ax.twinx()
pie2 = ax2.pie(subcat['Sales'], labels=subcat['Sub-Category'], autopct='%1.1f%%', colors=['#E75A7C', '#E87DA6', '#EAB6C1', '#5289C7', '#6CA0DC', '#A7BFE8', '#4D904D', '#6AC06A', '#8BE08E', '#B4EEB4']
, radius=0.9, startangle=90, labeldistance=0.60,wedgeprops=dict(edgecolor='w'), pctdistance=0.45,rotatelabels =True)

for text in pie2[1]:
    text.set_size(7)
for text in pie2[2]:
    text.set_size(7)
ax.set_title('Top Selling Sub-Categories', pad=30)

plt.savefig('images/top_selling_subcategories.png')

# Revenue by Customer Segment

segment = df.groupby(["Segment"]).sum().sort_values("Sales", ascending=False)
segment = segment[["Sales"]]
segment.reset_index(inplace=True)

colors = ['#569DAA', '#917FB3', '#FF6969']

plt.title('Revenue by Customer Segment', pad=20)
plt.bar(segment["Segment"], segment["Sales"], width=0.5, color=colors)
plt.xlabel("Segment",fontsize=10) 
plt.ylabel("Total Revenue (in millions)",fontsize=10) 
plt.xticks(fontsize=9, rotation=0)
plt.yticks(fontsize=8)

for x,y in segment["Sales"].items(): 
    plt.text(x,y-300000,'$'+ str(round(y,2)), fontsize=8,rotation=90, color='white',horizontalalignment='center')


plt.tight_layout()
plt.savefig('images/sales_by_segment.png')

# Revenue by Shipping Mode

ship = df.groupby(["Ship Mode"]).sum().sort_values("Sales", ascending=False)
ship = ship[["Sales"]]
ship.reset_index(inplace=True)

colors = ['#F45050', '#146C94', '#19A7CE', '#A6D0DD']

plt.title('Revenue by Shipping Mode', pad=20)
plt.bar(ship["Ship Mode"], ship["Sales"], width=0.5, color=colors)
plt.xlabel("Shipping Mode",fontsize=10) 
plt.ylabel("Total Revenue (in millions)",fontsize=10) 
plt.xticks(fontsize=9, rotation=0)
plt.yticks(fontsize=8)

for x,y in ship["Sales"].items(): 
    if x < 1:
        plt.text(x,y-350000,'$'+ str(round(y,2)), fontsize=8,rotation=90, color='white',horizontalalignment='center')
    else:
        plt.text(x,y+80000,'$'+ str(round(y,2)), fontsize=8,rotation=90, color='black',horizontalalignment='center')


plt.tight_layout()
plt.savefig('images/sales_by_shipping_mode.png')

# Sales over time period

df_line = df[['Order Date','Sales']].sort_values('Order Date') 
df_line['Order Date'] = pd.to_datetime(df_line['Order Date'])
df_line = df_line.groupby('Order Date').mean() 

plt.figure(figsize=[8,5])
plt.plot(df_line.index, 'Sales', data=df_line, color='#F05454') # Avg Sales over Time
plt.title("Average Sales over Time Period(2015-2018)", pad=20)
plt.xlabel("Time Period(2015-2018)",fontsize=10) 
plt.ylabel("Revenue ($)",fontsize=10) 

plt.tight_layout()
plt.savefig('images/sales_over_time.png')
plt.show()