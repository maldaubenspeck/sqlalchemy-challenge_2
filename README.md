# sqlalchemy-challenge_2

# The Challenge
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. Perform a precipitation analysis and then a station analysis.


# The Process
Before I begin explaining the process I will explain about my repo. My first repo had errors within the folders and environment that when I ran the app.py file I was not getting the results I wanted rather than lots of error codes. I then created a second repo but soon discovered that my file locations as well as a few adjustments within the code gave me the url link and ran correctly. I then realized that this was potentially my issue within the original repo, however I did not want to deal with messing things up so I continued with this one.

In Part 1, I initiated the analysis by connecting to the SQLite database using SQLAlchemy and reflected tables into classes with automap_base(). A session was established for Python-DB linkage, emphasizing the importance of closing the session at the notebook's end for resource management. The precipitation analysis involved finding the dataset's most recent date, querying the prior 12 months of precipitation data, and plotting the results using Matplotlib after loading them into a Pandas DataFrame. Additionally, I computed summary statistics for the precipitation data using Pandas.

For the station analysis, I crafted queries to calculate total station count, identify the most active stations, and determine temperature statistics for the most active station. A separate query was employed to retrieve the last 12 months of temperature observation (TOBS) data for the most active station, which was then visualized as a histogram. The coding conventions adhered to best practices, with imports at the script's beginning, variables and functions following standard conventions, and well-placed comments for enhanced readability.

In Part 2, I transitioned to designing a Flask API based on the queries from Part 1. The API offered routes for obtaining precipitation data, a list of stations, temperature observations for the most active station, and temperature statistics based on specified start and end dates. The Flask application was structured logically, and the homepage route provided clear documentation for the available routes. Overall, the process combined data analysis and visualization in Part 1 with the development of a user-friendly Flask API in Part 2, showcasing a comprehensive approach to exploring and sharing climate insights.

# What’s included?
Within this repo you will find my part 1 climate_starter.ipynb file within the first folder titled Starter_Code. To get to part 2 you will then open the folder Resources. There you will find the files named app.py, hawaii.sqlite, hawaii_measurements.csv, and hawaii_stations.csv. The file titled app.py will have the code used for part two and will run the url that is needed to get the results prompted. I have included photos of the different routes/web pages in a file in my repo titled results.

# Sources
For this challenge I utilized ChatGPT, fellow students, Youtube, VSCode, Jupyter Notebook, Google/Google Chrome, Stack Overflow, and Class recordings.
