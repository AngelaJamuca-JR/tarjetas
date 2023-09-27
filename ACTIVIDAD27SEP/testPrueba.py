
from nose2.tools import params
from removeMod import removeVowels

@params(("SAos","Ss"),("Miss","Mss"),("please12","pls12"),("Hi","H"))


def test_removeVowels(int,exp):
    assert removeVowels(int) == exp



if __name__=='__main__':
    import nose2
    nose2.main()