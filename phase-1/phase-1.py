# i'm a comment

import urllib2
import json
import googlemaps

gmaps = googlemaps.Client(key='')


def get_html(url):
    """
    Does a thing
    :param url: a URL
    :return: the URL (opened)
    """
    return urllib2.urlopen(url).read()


def api_call(origins, destinations):
    gmaps.distance_matrix(origins, destinations, mode="transit", language="en-US")


def main():
    pass


if __name__ == "__main__":
    main()