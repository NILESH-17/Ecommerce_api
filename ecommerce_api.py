# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an URL object
url = '---Enter your Ecommerce WebSite Here,'
# Create object page
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')

# Obtain information from tag <table>
table1 = soup.find('table', id='id')

# Obtain every title of columns with tag <th>
headers = []
for i in table1.find_all('th'):
 title = i.text
 headers.append(title)

 # Convert wrapped text in column names into one line text
headers[13] = 'Column names'

# Create a dataframe
mydata = pd.DataFrame(columns = headers)

#Cleaning and Processing of a Data
# Create a for loop to fill mydata
for j in table1.find_all('tr')[1:]:
 row_data = j.find_all('td')
 row = [i.text for i in row_data]
 length = len(mydata)
 mydata.loc[length] = row

# Export to csv
mydata.to_csv('filename.csv', index=False)
# read csv
mydata2 = pd.read_csv('filename.csv')

# Filter Data
# --add '0' to NaN Values
df.fillna(0)

# To operate Analaytics Operations on csv file
# --Pandas library
# 1.get Average of each column
mydata2.mean()
mydata2.average()

# Check records in Ascending or Descending Order on the basis of GST Rate
df1 = df.sort_values(by=['GST rate'])
df1 = df.sort_values(by=['GST rate'], ascending=False)

# Perform More Analytics to Data as per Requirement
# Some Analytics oprations can be Performned as
#  1.Get the Product name having Highest/Smallest gst rate.
#  2.Get the Info. About Product which has Increasing/Decreasing gst rate as per yearly data for each month/yearly in case.
#  3.which product having more demand?
#  4.in current month which product having highest sell?
#  5.Which product can be Dropped on the basis of Performance.etc

#after analysing all this records--
#records can be transfer into Charts using 'Matplotlib' [in case if needed]

#final records to be exported into csv/excel format for futher Investigation to Experts
df.to_csv('filename.csv')
df.to_excel('filename.xlsx')






