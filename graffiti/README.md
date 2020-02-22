# Graffiti Data Visualization

In this visualization, we'll be looking at the graffiti report

https://data.bloomington.in.gov/dataset/graffiti-reports

## Presentation Deck
https://drive.google.com/open?id=1Ni0k_WGriS9Ss3T2JRlW_uDhD18AFEfzxVEQPkvsDb4

## Installation

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


## Show On Map

Now that we have data read in, we can show it on a map (geospatially). If using pipenv, ipyleaflet should have been installed with `pipenv install`  

https://github.com/jupyter-widgets/ipyleaflet
https://ipyleaflet.readthedocs.io/en/latest/

In this case, all rows have a lat/long associated with them. If they did not, we would need to geocode those addresses. `geopy` would help with this:

https://towardsdatascience.com/geocode-with-python-161ec1e62b89


## Conversion

Jupyter notebooks can be converted to Markdown, if that helps with sharing:

    jupyter nbconvert my_notebook.ipynb --to markdown --output output.md
