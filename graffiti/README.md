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

In this visualization, we'll be looking at the graffiti report

https://data.bloomington.in.gov/dataset/graffiti-reports

Download the dataset to your local machine for reading in. 
```bash
wget https://data.bloomington.in.gov/dataset/08557e0d-74a6-48e9-9578-e9210973886c/resource/c0bf9039-7736-4ea5-8191-cdf821f304f5/download/graffiti.csv
```

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

## Conversion

    jupyter nbconvert my_notebook.ipynb --to markdown --output output.md
