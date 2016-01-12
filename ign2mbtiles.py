import logging
import geojson
from shapely.geometry import shape
from landez import MBTilesBuilder

logging.basicConfig(level=logging.DEBUG)

KEY = 'gnk8fnku3lwbxjz1fz34xx32'

# use png extension instead of jpeg
# jpeg will actually be downloaded but extension is png which won't break
# mbutil
url = "http://gpp3-wxs.ign.fr/%s/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&STYLE=normal&FORMAT=image/jpeg&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}.png" % KEY

mb = MBTilesBuilder(cache=True, tiles_url=url, tiles_headers={'Referer': 'localhost'}, filepath="/home/pierre/ign.mbtiles")

f = file('ign2mbtiles.geojson', 'r')
boxes_as_geojson = f.read()
features = geojson.loads(boxes_as_geojson).features

zooms = [11, 13, 15]

for feature in features:
    bbox = shape(feature.geometry).bounds
    mb.add_coverage(bbox=bbox, zoomlevels=zooms)

mb.run(force=True)
