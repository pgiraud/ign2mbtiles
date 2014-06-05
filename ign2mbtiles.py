import logging
from landez import MBTilesBuilder

logging.basicConfig(level=logging.DEBUG)

url = "http://gpp3-wxs.ign.fr/qunk4wvmc8pjw82h379if6sl/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&STYLE=normal&FORMAT=image/jpeg&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}.jpg"

mb = MBTilesBuilder(cache=True, tiles_url=url, tiles_headers={'Referer': 'localhost'}, filepath="/home/pierre/Documents/MapBox/tiles/ign.mbtiles")
mb.add_coverage(bbox=(8.7, 41.6, 9.2, 41.9), zoomlevels=[13, 15])

mb.run(force=True)
