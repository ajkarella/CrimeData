# Data Collection
Data Collection has presented some interesting challenges. Some of these include:
- Library issue
  - To speed up collection, we wanted to use multiprocessing
  - This did not play well with jupyter notebooks
  - So we had to run it in the pycharm IDE
- Limited access to data.
  - NYC's Data is only available to be pulled in 1000 entry increments
  - With over 5 million entries this could take time
- Formatting of data
  - The original data has large fields that made it impossible to store directly into a database
  - This created an extra pre-preprocessing step that we have to approach to store our data

# Work Order
- ~~**crimeCollector.py** - Collects data from NYC OpenData~~
- ~~**CleaningForSQL.ipynb** - Fixes errors in order to upload data to MySQL server~~
- **crimeCollector_V2.py** - Collects data from NYC OpenData and uploads to SQL server
- **Preprocessing.ipynb** - Cleans database and preps for EDA (uses "missingLaws.csv")
