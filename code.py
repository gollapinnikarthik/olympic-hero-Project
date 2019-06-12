# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data = data.rename(columns = {'Total': 'Total_Medals'})
print(data.head(10))

#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 
'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 
'Both', data['Better_Event'])

better_event = data['Better_Event'].value_counts().index.values[0]
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#nlargest gives the largest number of values in the frame. If we want top 3 or top 5 we specify the integer and the column in which you want to know the top n performing values
#top3 = df.nlargest(3, 'Score')

top_countries = top_countries[:-1]

def top_ten(data, column):
    country_list = []
    country_list = list((data.nlargest(10, column)['Country_Name']))
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print('Common countries: -', common)


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
plt.figure(figsize = (20, 6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])
plt.title('Total 10 Summer')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')

winter_df = data[data['Country_Name'].isin(top_10_winter)]
plt.figure(figsize = (20, 6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])
plt.title('Total 10 Winter')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')


top_df = data[data['Country_Name'].isin(top_10)]
plt.figure(figsize = (20, 6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])
plt.title('Total 10 Medals')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')




# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(), 'Country_Name']

print(summer_max_ratio, summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(), 'Country_Name']

print(winter_max_ratio, winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(), 'Country_Name']

print(top_max_ratio, top_country_gold)


# --------------
#Code starts here
data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total'] * 3 + data_1['Silver_Total'] * 2 + data_1['Bronze_Total'] * 1

most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(), 'Country_Name']

print(best_country, 'Best Country is the which has maximun total points', most_points)


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best.reset_index(drop = True)
best = best[['Gold_Total', 'Silver_Total', 'Bronze_Total']]


best.plot.bar(figsize = (10, 6), stacked = True)
plt.xlabel('United States')
plt.ylabel('Medals')
plt.xticks(rotation = 45)

#x = plt.legend(bbox_to_anchor = (0., 0.5, 0.5, .05))
x = plt.legend()
x.get_texts()[0].set_text('Gold Total: ' + str(best['Gold_Total'].values))
x.get_texts()[1].set_text('Silver Total: ' + str(best['Silver_Total'].values))
x.get_texts()[2].set_text('Bronze Total: ' + str(best['Bronze_Total'].values))


