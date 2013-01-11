# IPython log file
path = 'enwiki-20130102-pages-logging.xml'
get_ipython().system(u'cat sample')
from lxml import etree
f = open(path, 'r')
tree = etree.parse(f)
#get id's for contributors'
IDS = tree.xpath('/*/*/*[1]')
IDS.pop(0)
UIDS = tree.xpath('/*/*/*[3]/*[2]')
#get document titles
TITLES = tree.xpath('/*/*/*[7]')
IDTXTS = [i.text for i in IDS]
UDTXTS = [i.text for i in UIDS]
TITLETXTS = [lt.text for lt in TITLES]
z = zip(IDTXTS, UDTXTS, TITLETXTS)
