from librb.rbRadios import RadioBrowser

rb = RadioBrowser()


def getstations_byname(query):
    results = rb.stations_byname(query)
    stations = []
    for st in results:
        try:
            station = {'stationname': st['name'], 'id': st['id'], 'codec': st['codec'], 'bitrate': st['bitrate'], 'country': st['country'], 'homepage': st['homepage'], 'genre': st['tags']}
            stations.append(station)
        except:
            pass
    return stations


def geturl_byid(id):
    url = rb.playable_station(id)['url']
    if url is not None:
        return url
    else:
        return "-1"


def getstationname_byid(id):
    return rb.stations_byid(id)


if __name__ == "__main__":
    r = getstations_byname('r.sh')
    stationinfo = getstationname_byid(96748)
    pass
