# Nuisance / Public Safety Data

## Presentation Deck
https://drive.google.com/open?id=1eXPpQAxta1V1BN_8qx8uF1D56YO4BVEFm84cqasXqjw

## Data Retrieval
The datasets can be retrieved with the following bash command:
```bash
wget --accept "*.csv","*.xlsx" --no-directories --recursive --level 1 \
--no-parent https://data.bloomington.in.gov/dataset/nuisance-complaints-data
```

Observe that half the data formats are in CSV while the other half are in Excel format (determined by .xlsx). This is an unfortunate inconsistency 
and so we will convert the Excel to CSV, which is more uniform and adaptable. 

There are multiple ways to do this. I decided to use a simple Python script: https://github.com/dilshod/xlsx2csv
Obtain this program following the instructions in the repo and then run the conversion script
```bash
python data_to_csv
```
