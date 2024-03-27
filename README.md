
# Spotify Song Analysis
Code Louisville Data Analysis Capstone Projext


## Overivew
This Notebook Analizes the correaltion between most popular Artists on Spotify in 2023 and Grammy Winners in the past few years. There are three main data sets that come from Kaggle.


## Data Sources
I used Data from Kaggle. They came in the form of a CVS.
https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data
https://www.kaggle.com/code/alancano/spotify-top-songs
https://www.kaggle.com/datasets/meeratif/spotify-most-streamed-songs-of-all-time/data


### Requirements to meet Project List
1. Read in three CSV DATA Files
2. Clean Data and perfom a SQL join with data using SQLite3, Python, and Pandas
3. Make 3 matplotlib, and plotly visualtions to display data.
4. Utilize a virtual environemtn and include README
5. Annotate code with markdown cells in Jupyter Notebook.
6. Set up local database with SQLite3.



## Instructions/Virutal Environment Instructions
. Clone the repository to your machine:
    ```bash
    git clone https://github.com/floodadosious34/Music-Trends-Data-Analysis.git
    ```
2. After you have cloned the repo to your machine, navigate to the project 
folder in GitBash/Terminal.

3. Create a virtual environment in the project folder. `python3 -m venv venv` [^1]
4. Activate the virtual environment. `source venv/bin/activate`
5. Install the required packages. `pip install -r requirements.txt`
6. When you are done working on your repo, deactivate the virtual environment. 
`deactivate`
7. Run the [create_sql_db](create_sql_db.ipynb) notebook to unzip data files and create 'NHL_data.db' for future SQL queries.
 


