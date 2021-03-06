# Ambient Weather to CSV
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c3bc4be17494f71bef89c4f0944d504)](https://app.codacy.com/app/dave_9/ambientweather-CH?utm_source=github.com&utm_medium=referral&utm_content=Pcolar/ambientweather-CH&utm_campaign=Badge_Grade_Dashboard)

## Create a CSV file from a API call to Ambient Weather

### Goal 
Create a script that can perform a GET request with the given API, transform that data into a human readable format, and then write it to a CSV

### Purpose 
The purpose of this exercise is to test your familiarity with the Extract & Transform operations.

### Methodology 
The test files are initially in Python format, but you may use any programming
language of your choosing to accomplish this task. You may convert the files to
your desired format, but please keep the names the same.

### Data Source
The API you will communicate with is connected to the weather sensor that is located at the Chapel Hill Public Library.

### Output The final CSV should include these data points
#### Temperature (F), Humidity (%), Wind Speed (mph), Wind Gust (mph), Daily Rainfall Totals (in), Monthly Rainfall Totals (in), Yearly Rainfall Totals (in), UV Radiation Index, and Date/Time

### Transform
Oftentimes, transforming data is the most time consuming process of ETL. To test
your comfort with this, we ask for an additional feature in your script.
#### For the Temperature (F) column
##### If the temperature is below 60 (F) write “Too cold”
##### If the temperature is above 85 (F) write “Too hot”
##### Else write “Goldilocks”

### Constraints
#### Please write your code in the test.py file you were given
#### Do not move the file to a different folder 
#### DO NOT INCLUDE THE secrets FILE IN THE UPLOAD
