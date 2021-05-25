{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Intro to Cartopy\n",
    "\n",
    "Cartopy is a Python package that provides easy creation of maps with matplotlib."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Cartopy *vs* Basemap"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Cartopy is replacing Basemap, which is nearing its [end-of-life in 2020](https://matplotlib.org/basemap/users/intro.html#cartopy-new-management-and-eol-announcement). All new software development should try to use Cartopy whenever possible.\n",
    "* Cartopy is better integrated with matplotlib and in a more active development state, supported by the UK Met Office \n",
    "* Proper handling of datelines in cartopy - one of the bugs in basemap (example: [Challenger circumnavigation](http://ocefpaf.github.io/python4oceanographers/blog/2013/09/23/cartopy/))\n",
    "* Cartopy offers powerful vector data handling by integrating shapefile reading with Shapely capabilities\n",
    "* Cartopy now has support for gridlines on all plots as of May 2020\n",
    "* Basemap has a map scale bar feature (can be [buggy](https://github.com/matplotlib/basemap/issues/165)); still [not implemented](https://github.com/SciTools/cartopy/issues/490) in cartopy, but there are some messy [workarounds](http://stackoverflow.com/questions/32333870/how-can-i-show-a-km-ruler-on-a-cartopy-matplotlib-plot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As for the standard matplotlib plots, we first need to import `pyplot` submodule and make the graphical output appear in the notebook:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to create a map with cartopy and matplotlib, we typically need to import pyplot from matplotlib and cartopy's crs (coordinate reference system) submodule. These are typically imported as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then let's import the cartopy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cartopy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In addition, we import cartopy's **coordinate reference system** submodule:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cartopy.crs as ccrs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Creating GeoAxes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Cartopy-matplotlib interface is set up via the `projection` keyword when constructing `Axes` / `SubAxes`\n",
    "* The resulting instance (`cartopy.mpl.geoaxes.GeoAxesSubplot`) has new methods specific to drawing cartographic data, e.g. **coastlines**:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = plt.axes(projection=ccrs.PlateCarree())\n",
    "ax.coastlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('axes type:', type(ax))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here we are using a Plate Carrée projection, which is one of the *equidistant cylindrical projections*.\n",
    "\n",
    "A full list of Cartopy projections is available at http://scitools.org.uk/cartopy/docs/latest/crs/projections.html.\n",
    "\n",
    "Map projections induce some strong opinions in people ([obligatory xkcd](https://xkcd.com/977/)). Always consider the map projections that you choose for your project. All projections distort, but some are more suited to certain tasks. See links at the bottom of this notebook for more information about projections."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Putting georeferenced data on a map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Use the standard matplotlib plotting routines with an additional `transform` keyword.\n",
    "* The value of the `transform` argument should be the cartopy coordinate reference system *of the data being plotted*. This will typically be Plate Carrée as, under this projection, any point's location in lon and lat is simply its coordinates in the xy plane"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = plt.axes(projection=ccrs.PlateCarree())\n",
    "ax.coastlines()\n",
    "ax.set_global()\n",
    "plt.plot([-100, 50], [25, 25], linewidth=4, color='r', transform=ccrs.PlateCarree())\n",
    "plt.plot([-100, 50], [25, 25], linewidth=4, color='b', transform=ccrs.Geodetic())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Notice that unless we specify a map extent (we did so via the **``set_global``** method in this case) the map will zoom into the range of the plotted data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Decorating the map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can add grid lines and tick labels to the map using the `gridlines()` method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = plt.axes(projection=ccrs.PlateCarree())\n",
    "ax.coastlines()\n",
    "ax.gridlines(draw_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Grid lines are not restricted to rectangular plots, all Cartopy projections now accept gridlines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ax = plt.axes(projection=ccrs.AlbersEqualArea())\n",
    "ax.coastlines()\n",
    "ax.gridlines(draw_labels=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can control the specific tick values by using matplotlib's locator object, and the formatting can be controlled with matplotlib formatters:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "import matplotlib.ticker as mticker\n",
    "\n",
    "ax = plt.axes(projection=ccrs.PlateCarree())\n",
    "ax.coastlines()\n",
    "gl = ax.gridlines(draw_labels=True)\n",
    "\n",
    "gl.xlocator = mticker.FixedLocator([-180, -90, 0, 90, 180])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exercise\n",
    "Experiment with the following code cell to produce a map:\n",
    "- Uncomment lines to use their functionality\n",
    "- Try changing the coordinate reference system (check the list of them [here](https://scitools.org.uk/cartopy/docs/latest/crs/projections.html))\n",
    "- Change the plot limits and tick locations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = plt.figure(figsize=(10, 5))\n",
    "ax = plt.axes(projection=ccrs.PlateCarree())\n",
    "ax.set(xlim=[80,140], ylim=[-20,20], transform =ccrs.PlateCarree() )\n",
    "ax.coastlines()\n",
    "\n",
    "#gl = ax.gridlines(draw_labels=True)\n",
    "#gl.xlocator = mticker.FixedLocator([90, 110, 130])\n",
    "#ax.stock_img()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Inbuilt Feautures\n",
    "Cartopy has inbuilt functionality to plot coastlines, national boundaries, lakes, rivers and more. [Documentation here](https://scitools.org.uk/cartopy/docs/latest/matplotlib/feature_interface.html)\n",
    "\n",
    "All of these features come in three scales ‘10m’, ‘50m’, or ‘110m’. Corresponding to 1:10,000,000, 1:50,000,000, and 1:110,000,000 \n",
    "\n",
    "10m offers the highest resolution, but is slower to plot\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate the coastline feature at three different scales\n",
    "land_110m = cartopy.feature.NaturalEarthFeature('physical', 'coastline', '110m',\n",
    "                                        edgecolor='k', facecolor='palegreen')\n",
    "land_50m = cartopy.feature.NaturalEarthFeature('physical', 'coastline', '50m',\n",
    "                                        edgecolor='k', facecolor='palegreen')\n",
    "land_10m = cartopy.feature.NaturalEarthFeature('physical', 'coastline', '10m',\n",
    "                                        edgecolor='k', facecolor='palegreen')\n",
    "\n",
    "# Make 3 geoaxes by using subplots with subplot_kw to specify the projection\n",
    "fig, axs = plt.subplots(ncols=3, figsize=(15,6),subplot_kw={'projection': ccrs.AlbersEqualArea()})\n",
    "axs = axs.ravel()\n",
    "\n",
    "# Add coastlines of varying scale to the three axes\n",
    "axs[0].add_feature(land_110m)\n",
    "axs[1].add_feature(land_50m)\n",
    "axs[2].add_feature(land_10m)\n",
    "\n",
    "axs[0].set_title(\"1:110 million coastline\")\n",
    "axs[1].set_title(\"1:50 milion coastline\")\n",
    "axs[2].set_title(\"1:10 million coastline\")\n",
    "\n",
    "# Add national borders to the final axes and gridlines to all axes\n",
    "axs[2].add_feature(cartopy.feature.BORDERS)\n",
    "for ax in axs:\n",
    "    gl = ax.gridlines(draw_labels=False)\n",
    "    ax.set_extent([-5, 5, 50, 56], crs=ccrs.PlateCarree());\n",
    "# Note that the limits of the plot are set using PlateCarree"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Plotting layers directly from Web Map Service (WMS) and Web Map Tile Service (WMTS)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'http://map1c.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi'\n",
    "fig = plt.figure(figsize=(12, 8))\n",
    "\n",
    "ax = plt.axes(projection=ccrs.PlateCarree())\n",
    "ax.add_wmts(url, 'VIIRS_CityLights_2012');"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reminder: Cartopy is based on matplotlib\n",
    "\n",
    "Consequentially, most plotting functions available in matplotlib can be reproduced with Cartopy. Usually, this is achieved by calling the plotting method with the **transform** keyword argument to inform matplotlib of the coordinate system of the data you are plotting. This will typically be Plate Carrée"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Plot a basic global map\n",
    "fig = plt.figure(figsize=(12, 8))\n",
    "ax = plt.axes(projection=ccrs.Robinson())\n",
    "ax.coastlines()\n",
    "ax.set_global()\n",
    "ax.gridlines(draw_labels=True)\n",
    "ax.stock_img()\n",
    "# Add some scatter points\n",
    "lon_0 = np.random.randint(low=-180, high=180, size=10)\n",
    "lat_0 = np.random.randint(low=-20, high=20, size=10)\n",
    "ax.scatter(lon_0, lat_0, color='k', transform = ccrs.PlateCarree())\n",
    "\n",
    "# Add a circumnavigating line following the geodetic (great circle) line between points\n",
    "ax.plot([-120, -90, -50, 0, 40, 120, 175, 200, 250, -120],\n",
    "        [60, 70, 0, -30, 0, 50, 25, 10, 0, 60],\n",
    "        linewidth=2, color='C2', transform=ccrs.Geodetic())\n",
    "\n",
    "\n",
    "# Add a countour plot\n",
    "x1, y1 = np.meshgrid(np.linspace(-170,170,100), np.linspace(-70,-30,100))\n",
    "z1 = np.sin(x1/30) * np.cos(y1/10)\n",
    "ax.contourf(x1,y1,z1, 20, cmap='RdBu', transform=ccrs.PlateCarree())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Challenge\n",
    "Make a map of Europe with the capital cities marked, a flight path from Norwich to Beijing and some bathymetry from the Mediterranean\n",
    "#### Hints:\n",
    "- Make use the land feature we created previously\n",
    "- Use a scatter for the capitals\n",
    "- The flight path between Norwich and Beijing should be a great circle path\n",
    "- The bathymetry in the Mediterranean can be added with contourf and needs an appropriate colour map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![](../figures/europe_map.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "capital_lat, capital_lon = np.loadtxt('../data/capital_locs.csv', skiprows=1, delimiter=',', usecols=(2,3), unpack=True)\n",
    "\n",
    "norwich_beijing_lat = [52.630535, 39.904211]\n",
    "norwich_beijing_lon = [1.297250, 116.407395]\n",
    "\n",
    "import xarray as xr # More on this bit with Jenny tomorrow\n",
    "bathy_ds = xr.open_dataset('../data/bathy_subset.nc')\n",
    "bathy_lon, bathy_lat, bathy_h = bathy_ds.bathymetry.longitude, bathy_ds.bathymetry.latitude, bathy_ds.bathymetry.values\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your code here"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Scroll down for a sample solution\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    ".\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig = plt.figure(figsize=(12, 8))\n",
    "ax = plt.axes(projection=ccrs.Robinson(central_longitude=7.5))\n",
    "ax.coastlines()\n",
    "ax.add_feature(land_50m)\n",
    "ax.add_feature(cartopy.feature.BORDERS)\n",
    "\n",
    "ax.set_extent([-10, 25, 35, 60], crs=ccrs.PlateCarree());\n",
    "\n",
    "ax.scatter(capital_lon[capital_lat<55], capital_lat[capital_lat<55], color='k', transform=ccrs.PlateCarree(), zorder=2)\n",
    "\n",
    "ax.plot(norwich_beijing_lon, norwich_beijing_lat, linestyle='--', transform=ccrs.Geodetic())\n",
    "\n",
    "ax.contourf(bathy_lon, bathy_lat, bathy_h, 20, vmin=-3200, vmax=200, cmap='Blues_r', transform=ccrs.PlateCarree())\n",
    "gl = ax.gridlines(draw_labels=True)\n",
    "gl.xlocator = mticker.FixedLocator([-10, 0,10, 20])\n",
    "gl.ylocator = mticker.FixedLocator([40, 50,60])\n",
    "#plt.savefig('../figures/europe_map.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Bonus section: high definition shapefiles\n",
    "\n",
    "If you plan to work at very small scales (sub km), the inbuilt coastlines will not be sufficiently detailed. Instead you can get some from [Open Street Map](https://osmdata.openstreetmap.de/download/land-polygons-split-4326.zip) and plot them with cartopy. For details on how to subset the shapefiles to your region of interest so they don't take all day to plot, see [here](\n",
    "https://gis.stackexchange.com/questions/6019/cutting-up-a-shapefile-into-smaller-parts?rq=1\n",
    "). Here's how they look."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "land_110m = cartopy.feature.NaturalEarthFeature('physical', 'coastline', '110m',\n",
    "                                        edgecolor='k', facecolor='palegreen')\n",
    "land_50m = cartopy.feature.NaturalEarthFeature('physical', 'coastline', '50m',\n",
    "                                        edgecolor='k', facecolor='palegreen')\n",
    "land_10m = cartopy.feature.NaturalEarthFeature('physical', 'coastline', '10m',\n",
    "                                        edgecolor='k', facecolor='palegreen')\n",
    "\n",
    "# Make 3 geoaxes by using subplots with subplot_kw to specify the projection\n",
    "fig, axs = plt.subplots(ncols=3, figsize=(15,6),subplot_kw={'projection': ccrs.Robinson()})\n",
    "axs = axs.ravel()\n",
    "\n",
    "# Add coastlines of varying scale to the three axes\n",
    "axs[0].add_feature(land_50m)\n",
    "axs[1].add_feature(land_10m)\n",
    "\n",
    "from cartopy.io import shapereader\n",
    "shp = shapereader.Reader('../data/coasts/hidf_land.shp')\n",
    "for record, geometry in zip(shp.records(), shp.geometries()):\n",
    "    axs[2].add_geometries([geometry], ccrs.PlateCarree(), facecolor='lightgreen', edgecolor='black', linewidth=0.1)\n",
    "\n",
    "axs[0].set_title(\"1:50 milion coastline\")\n",
    "axs[1].set_title(\"1:10 million coastline\")\n",
    "axs[2].set_title(\"OSM coastline\")\n",
    "\n",
    "for ax in axs:\n",
    "    gl = ax.gridlines(draw_labels=False)\n",
    "    ax.set_extent([-6.3, -5.4, 56, 57], crs=ccrs.PlateCarree());\n",
    "    \n",
    "plt.savefig('../figures/scot_coast.png')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## References\n",
    "- Some discussion on projections https://source.opennews.org/articles/choosing-right-map-projection/\n",
    "- How to choose a projection http://www.geo.hunter.cuny.edu/~jochen/gtech201/lectures/lec6concepts/map%20coordinate%20systems/how%20to%20choose%20a%20projection.htm\n",
    "- Lon and lat of capital cities taken from https://www.jasom.net/list-of-capital-cities-with-latitude-and-longitude/"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
