import os
import shutil
import logging
import geojson
from shapely.geometry import shape
from landez import MBTilesBuilder
from mbutil import mbtiles_to_disk

logging.basicConfig(level=logging.DEBUG)

KEY = 'jhyvi0fgmnuxvfv0zjzorvdn'

# use png extension instead of jpeg
# jpeg will actually be downloaded but extension is png which won't break
# mbutil
url = "http://gpp3-wxs.ign.fr/%s/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&STYLE=normal&FORMAT=image/jpeg&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}.png" % KEY

filepath = "ign.mbtiles"
mb = MBTilesBuilder(cache=True, tiles_url=url, tiles_headers={'Referer': 'localhost'}, filepath=filepath)

if os.path.exists(mb.filepath):
    if os.path.exists(mb.cache.folder):
        shutil.rmtree(mb.cache.folder)
    mbtiles_to_disk(mb.filepath, mb.cache.folder)

f = file('ign2mbtiles.geojson', 'r')
boxes_as_geojson = f.read()
features = geojson.loads(boxes_as_geojson).features

zooms = [11, 13, 15]

for feature in features:
    bbox = shape(feature.geometry).bounds
    mb.add_coverage(bbox=bbox, zoomlevels=zooms)

mb.run(force=True)
