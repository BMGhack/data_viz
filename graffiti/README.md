# Data Visualization

## JupyterLab

This approach leverages the free and open source Jupyter Lab Notebook system for documenting the steps taken. 

I used [pipenv](https://github.com/pypa/pipenv) to help manage the virtualenv.

https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html

If you've cloned this repo, there is already a Pipfile that will track dependencies.

```
pipenv install
pipenv shell
jupyter labextension install @jupyter-widgets/jupyterlab-manager jupyter-leaflet
jupyter lab
```

The `jupyter lab` command should launch the server and open a browser to navigate to something like: `http://localhost:8888/lab`

## Data

Data is being sourced from the City of Bloomington's Data Portal:

https://data.bloomington.in.gov/

In this visualization, we'll be looking at the Graffiti report

https://data.bloomington.in.gov/dataset/graffiti-reports

Download the dataset to your local machine for reading in. 
(TODO: way to pull directly from the data portal?)

## Read Data

https://docs.python.org/3/library/csv.html



```python
import csv
with open('c0bf9039-7736-4ea5-8191-cdf821f304f5.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    count = 0 
    for row in reader:
        # first two rows is enough to show it's working
        if count < 2:
            print(', '.join(row))
        count += 1
```

    ﻿_id, ticket_id, enteredDate, lastModified, closedDate, status, contactMethod, category, description, department, location, city, state, zip, latitude, longitude
    1, 124433, 2011-11-29T23:18:14, 2016-09-11T22:02:05, 2012-06-08T14:09:47, closed, Phone Call, Graffiti, wall of Framemakers building had white spray paint on wall and door, , 314 W Kirkwood AVE, Bloomington, IN, 47404, 39.16685104370117, -86.53697204589844


Now that we know we can read the data, let's parse it. In this case there are only ~800 rows... we can store that in memory:


```python
reports = []

with open('c0bf9039-7736-4ea5-8191-cdf821f304f5.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # eliminate blank rows if they exist
    rows = [row for row in reader if row]
    header = rows[0]

    for row in rows[1:]:
        # print(row)
        current_report = {}
        for col_header, data_column in zip(header, row):
            # print(col_header, data_column)
            current_report[col_header] = data_column
        
        reports.append(current_report)

print(reports[0])
```

    {'\ufeff_id': '1', 'ticket_id': '124433', 'enteredDate': '2011-11-29T23:18:14', 'lastModified': '2016-09-11T22:02:05', 'closedDate': '2012-06-08T14:09:47', 'status': 'closed', 'contactMethod': 'Phone Call', 'category': 'Graffiti', 'description': 'wall of Framemakers building had white spray paint on wall and door', 'department': '', 'location': '314 W Kirkwood AVE', 'city': 'Bloomington', 'state': 'IN', 'zip': '47404', 'latitude': '39.16685104370117', 'longitude': '-86.53697204589844'}


# Show On Map

Now that we have data read in, we can show it on a map (geospatially). If using pipenv, ipyleaflet should have been installed with `pipenv install`  

https://github.com/jupyter-widgets/ipyleaflet
https://ipyleaflet.readthedocs.io/en/latest/

In this case, all rows have a lat/long associated with them. If they did not, we would need to geocode those addresses. `geopy` would help with this:

https://towardsdatascience.com/geocode-with-python-161ec1e62b89


```python
from ipyleaflet import Map, Marker

center = (39.16685104370117, -86.53697204589844)

m = Map(center=center, zoom=15)

for r in reports:
    marker = Marker(location=(r['latitude'], r['longitude']), draggable=False)
    m.add_layer(marker)
    
display(m)
```


    Map(center=[39.16685104370117, -86.53697204589844], controls=(ZoomControl(options=['position', 'zoom_in_text',…



```python

```

## TODO

Pandas would help simplify the process of reading CSV files and working with the data. 

## Conversion

    jupyter nbconvert my_notebook.ipynb --to markdown --output output.md
