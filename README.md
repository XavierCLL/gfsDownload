
# gfsDownload

Tools for downloading gfs meteo parameters modelling estimation on
an area and on a specific time. GFS is a product of NCEP,NOAA and
provide a full range of product which are describe in http://www.nco.ncep.noaa.gov/pmb/products/gfs/


## Installation

```
mkdir PATH/TO/INSTALL
cd PATH/TO/INSTALL/gfsDownload
git clone git+git://github.com/XavierCLL/gfsDownload.git
sudo apt-get install grib-api libopenjpeg pyproj python
```
```
python3 GFSDownload.py -help
```

( or you cas Use pip to install gfsDownload )

## Overview: What can gfsDownload do?

gfsDownload has a main function, allow download of parameters on a
area in an automatic way

### Four paramaters are mandatory:

#### `--code <GFSCode>`

A list of code which define parameters desired. Code reference can be found on :
 
- [For analyse](http://www.nco.ncep.noaa.gov/pmb/products/gfs/gfs_upgrade/gfs.t06z.pgrb2.0p25.anl.shtml)

- [For forecast](http://www.nco.ncep.noaa.gov/pmb/products/gfs/gfs_upgrade/gfs.t06z.pgrb2.0p25.f006.shtml)

###### CODE PARAMETERS Exemple:

- precipitation : APCP _[m of water]_
- temperature : TMP
- pressure : PRES _[Pa]_
- dewpoint : DPT _[K]_
- eastward wind component UGRD _[m s-1]_
- northward wind component VGRD _[m s-1]_

### `--init <dateStart YYYY-MM-DD>` and `--end <dateEnd YYYY-MM-DD>`
 
Interval period is needed, these parameters should be in a 14 days range from maximum date today 

### `--shapefile <shapefile>` or `-Extend < xmin,ymax,xmax,ymin>` 

Area needed, shapefile (srs is not important because it will be reprojected in WGS84) or extend in WGS84

### EXAMPLES:
- Temperature on a shapefile during the first to the second of january: `python3 GFSDownload.py -c TMP -i 2014-01-01 -e 2014-01-02 -s PATH_TO_SHAPE`
- Pressure and dewPoint on a area during the first month of 2015 on a specific extend: `python3 eraInterimDownload.py -c PRES,DPT -i 2015-01-01 -e 2015-02-01 -E xmin,ymax,xmax,ymin`
 

### Five paramaters are optional:
 
####  `--Step <gfsDownload Step> (default 0)` 

The step of modeling. The step of itarate data over the days choosen! default is 0,6,12,18. A list is possible for that parameter:
`python3 GFSDownload.py -c TMP -i 2013-11-08 -e 2013-12-09 -E
xmin,ymax,xmax,ymin -p 0,6`

#### `--Grid <grid spacing on °.arc> (default 0)`

The spacing of final raster. grid possible: 0.25/0.5/1/2.5 default is 0.25 
`python3 GFSDownload.py -c TMP -i 2015-04-19 -e 2015-04-19 -E xmin,ymax,xmax,ymin -g 0.5`

#### `--Outfile <Path to downloaded Raster> (default /home/user/eraInterim)`

`python3 GFSDownload.py -c PRES -i 2011-10-01 -e 2011-10-02 -E xmin,ymax,xmax,ymin -o PATH/TO/FILE' All` 

downloaded raster are tif with a VAR_LEVEL_DateInit_DateEnd.tif name

#### `--proxy <proxy: True/False> (default False)`

Sometimes a proxy definition is needed for downloading from external
network. When this option is activated, a proxy user/key/site could be
defined to overpass it 

### Important Notes

All downloaded and processed images are stored by default in your
home directory in GFS forlder: ~/GFS 

### To Do List

- Improve console output
- Maintain with bug error

