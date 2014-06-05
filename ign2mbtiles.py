import logging
from landez import MBTilesBuilder

logging.basicConfig(level=logging.DEBUG)

url = "http://gpp3-wxs.ign.fr/qunk4wvmc8pjw82h379if6sl/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&STYLE=normal&FORMAT=image/jpeg&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}.jpg"

mb = MBTilesBuilder(cache=True, tiles_url=url, tiles_headers={'Referer': 'localhost'}, filepath="/Users/pierregiraud/Documents/MapBox/tiles/ign.mbtiles")

# corsica
bboxes = [
    (8.7, 41.5, 9.4, 42.1),
    (9.3, 42.68, 9.497, 43.01),
    (9.049, 42.64, 9.327, 42.73),
    (9.294, 41.96, 9.57, 42.69),
    (8.52, 41.86, 9.3, 42.63),
    (8.657, 41.4, 9.43, 41.97),
    (9.034, 41.32, 9.29, 41.48),
]
zooms = [11, 13, 15]

for bbox in bboxes:
    mb.add_coverage(bbox=bbox, zoomlevels=zooms)

mb.run(force=True)
