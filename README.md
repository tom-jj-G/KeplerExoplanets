# KeplerExoplanets

## Presentation

### Selected topic
### Reason why the topic has been selected
### Description of the source of data
### Questions we hope to answer with the data

## GitHub
### Communication protocols
After each pull request (PR), the person in charge of the github repository will review the code and ask for team assistance if necessary.
![review_process.png)](images/github/review_process.png)

After the PR has been accepted, the person who made the PR will merge her/his code to the main branch and alert the team that their own personal branch or sub-branch needs to be updated with the latest version of the main branch.
![github_merge.png)](images/github/github_merge.png)


## Machine Learning Model
At the moment our target result is binary: Is it a planet or not. 
The dataset is labeled (koi_pdisposition) and so we will apply a supervised ML logistics model.<br>

Additionally our plan is to create a neural net with the sigmoid activation function and compare it to the supervised ML model.

During the initial EDA its been relaved that (koi_disposition) may be another target worth investigating. The is not binary but has (4) possible outcomes.<br>
Also during EDA we discovered that there are a large number of NaN values that we will need to process.

For the initial model we have removed all NaNs.

## Database
We are using the Postgres DB, currently an instance residing on Damien's local machine.

Created a DB called "kepler", with one initial table called "raw_kepler".
- The table is a one-to-one map wth the source CSV data file.

Project DB files of note:
- The DB & table definition SQL files are in the project Database folder.
- The source CSV file is in the project Resources folder.

Use the PG Admin Import/Export tool to import the CSV file.
An initial load resulted in the following outcome:
- "Successfully run. Total query runtime: 215 msec. 9564 rows affected."

*NOTE:*
During initial loading I assumed, based on an initial quick read of the page describing the data columns of our source data file, that the column "kepid" might be suitable as a unique primary key. That turned out to NOT be the case, further review of the data model is required.
- Data dictionary "Data Columns in Kepler Objects of Interest Table" is located here "https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html#tce_info"


## Dashboard
