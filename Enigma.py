from defaults import *

class Enigma:
    def __init__(self, rotorloc=[0, 0, 0], rotorturn=turnpoints[1:4],
                 rotor1=rotor1, rotor2=rotor2, rotor3=rotor3,
                 endscrambler=reflect1, charset=rmaps[0], forcecaps=True):
        """ Create a new Enigma object.

Defaults are Enigma rotors 1, 2 and 3 and reflector 1.

Create a new Enigma object using different rotors. """
        
        self._setupcharswap(charset, forcecaps)

        self._r1 = rotor1
        self._r2 = rotor2
        self._r3 = rotor3
        self._scre = endscrambler

    def _setupcharswap(self, charset, forcecaps):
        if forcecaps or not charset:
            self._prescr = self._caps
        else:
            self._prescr = None

        strl = False
        if type(charset) == type("") or type(charset) == type([]):
            chl = charset
            strl = True
            l = len(charset)
        elif type(charset) == type({}):
            self._chset = charset
        else:
            chl = rmaps[0]
            strl = True
            l = 26
            
        if strl:
            self._chset = {}
            for x in range(0, l):
                self._chset[x] = chl[x]
                self._chset[chl[x]] = x

    def _caps(self, txt):
        return(txt.upper())

    def _endscramble(self, n):
        return(self._scre[n])
