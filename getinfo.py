from scoreline import normalInfo, artInfo, musiceInfo
import json

def getInfo():
    info = []
    normal = []
    art = []
    musice = []
    for year in [2017, 2016, 2015]:
        artValue = artInfo(year)
        normalValue = normalInfo(year)
        musiceValue = musiceInfo(year)
        normal.extend(normalValue)
        art.extend(artValue)
        musice.extend(musiceValue)
    info.extend(normal)
    info.extend(art)
    info.extend(musice)
    return json.dumps(info, ensure_ascii=False)