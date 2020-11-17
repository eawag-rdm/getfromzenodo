'''getfromzenodo.py

Usage:
  getfromzenodo.py <zenodo_url>
  getfromzenodo.py (--help|-h)

Options:
  --help -h   Show ths help.

'''

import requests
from docopt import docopt
import json

class GetPackage:
    def __init__(self, args):
        self.args = args
        self.z_apibase = 'https://zenodo.org/api/'

    def get_z_id(self):
        return self.args['<zenodo_url>'].split('/')[-1]

    def get_z_record(self, zid):
        url = self.z_apibase + 'records/{}'.format(zid)
        record = requests.get(url).json()
        return record

    def main(self):
        print(self.args)

if __name__ == '__main__':
    args = docopt(__doc__)
    gp = GetPackage(args)

    
    
