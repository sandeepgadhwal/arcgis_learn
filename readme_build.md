# arcgis_learn

Meta package to simpify install of dependencies required for using arcgis.learn module

## Reference
[https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html](https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html)

## Building Doc
clone the repo if you do not have it
````bash
git clone https://github.com/sandeepgadhwal/arcgis_learn
````
Trigger Build
````bash
conda build arcgis_learn -c esri -c pytorch -c fastai -c plotly
````

## Testing
Make sure you are in a clean env before testing the build
````bash
conda create -n arcgis_learn
conda activate arcgis_learn
````
Install the local build
````bash
conda install -c esri -c fastai -c pytorch -c plotly -c "C:\Users\san10428\conda-bld" arcgis_learn
````
Now run the sanity tests which you wat to run

## Copy Package to repo for archiving
````bash
md "arcgis_learn\dst\noarch"
copy "C:\Users\san10428\conda-bld\noarch\arcgis_learn-0.1.8-py37_0.tar.bz2" "arcgis_learn\dst\noarch\arcgis_learn-0.1.8-py37_0.tar.bz2"
````

## Publishing
install anaconda client
```bash
conda install anaconda-client
```
Login to anaconda
```bash
anaconda login
```
Upload build artifact
```bash
anaconda upload arcgis_learn/dst/noarch/arcgis_learn-0.1.8-py37_0.tar.bz2
```

## Cleanup
Clean intermediate and final build artifact from local
```bash
conda build purge
```