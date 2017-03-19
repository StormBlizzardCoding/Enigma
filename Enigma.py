class Enigma:
    def __init__(self, rotors=(1, 2, 3), rotorloc=[1, 1, 1], rotor1=None,
                 rotor2=None, rotor3=None, rotor4=None, rotor5=None,
                 endscrambler=None, charset=None, forcecaps=True):
        self._setupcharswap(charset, forcecaps)
        
        if endscrambler:
            self._scre = endscrambler
        else:
            self._scre = {1:3, 2:26, 3:1, 4:9, 5:24, 6:7, 7:6, 8:10, 9:4, 10:8,
                          11:16, 12:22, 13:17, 14:18, 15:19, 16:11, 17:13,
                          18:14, 19:15, 20:25, 21:23, 22:12, 23:21, 24:5, 25:20,
                          26:2}

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
            chl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            strl = True
            l = 26
            
        if strl:
            self._chset = {}
            for x in range(0, l):
                self._chset[x+1] = chl[x]
                self._chset[chl[x]] = x+1

    def _caps(self, txt):
        return(txt.upper())

    def _endscramble(self, n):
        return(self._scre[n])
