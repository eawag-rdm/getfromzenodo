import getfromzenodo as gfz
import pytest

TEST_Z_URL = 'https://zenodo.org/record/3776769'

def init_gp(argtokens):
    args = gfz.docopt(gfz.__doc__, argv=argtokens)
    gp = gfz.GetPackage(args)
    return gp

def test_args(capsys):
    argtokens = ['-h']
    with pytest.raises(SystemExit):
        args = gfz.docopt(gfz.__doc__, argv=argtokens)
    out, err = capsys.readouterr()
    assert(out.split('\n')[0] == 'getfromzenodo.py')

    argtokens = ['lll']
    gp = init_gp(argtokens)
    assert(gp.args['<zenodo_url>'] == 'lll')

def test_get_z_id():
    argtokens = [TEST_Z_URL]
    gp = init_gp(argtokens)
    zid = gp.get_z_id()
    assert(zid == '3776769')
 
def test_get_z_record():
    argtokens = ['https://zenodo.org/record/3776769']
    gp = init_gp(argtokens)
    record = gp.get_z_record(gp.get_z_id())
    assert(record['metadata']['creators'][0]['name'] == "Harald von Waldow")
    

