#profiles = sc.parallelize(range(1,200))
def fetchProfile(id):
    import urllib2
    response = urllib2.urlopen("http://seattle.pydata.org/speaker/profile/%s" % id)
    html = response.read()
    pronouns
#profiles.map(fetchProfile)
