# arcgis_learn

Meta package to simpify install of dependencies required for using arcgis.learn module

## Post Build Installation Steps using conda  
```bash
conda install -c esri -c fastai -c pytorch -c plotly -c sandeepgadhwal arcgis_learn
```
```bash
conda install -c esri -c sandeepgadhwal arcgis_learn
```
```bash
conda install -c esri -c esri/label/prerelease -c sandeepgadhwal arcgis_learn
```

## Post Build Installation Steps using the local build
````bash
conda install -c esri -c fastai -c pytorch -c plotly -c "C:\Users\san10428\conda-bld" arcgis_learn
````
````bash
conda install -c esri -c sandeepgadhwal -c "C:\Users\san10428\conda-bld" arcgis_learn
````
````bash
conda install -c esri -c fastai -c pytorch -c plotly -c ~/anaconda3/conda-bld -c sandeepgadhwal arcgis_learn
````
````bash
conda install -c esri -c sandeepgadhwal -c ~/anaconda3/conda-bld  arcgis_learn
````

## Upgrading any package installed with the metapackage
Most of the packages are pinned with the metapackage to work with a particular version of arcgis.learn.
If you need to manually upgrade any package you need to first remove the arcgis_learn metapackage and then 
continue.
You can remove just the arcgis_learn metapackage using the following command, it won't affect other packages installed with it. 
````bash
conda remove arcgis_learn --force
````

~~~~