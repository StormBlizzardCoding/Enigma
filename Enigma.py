class Enigma:
    def __init__(self, rotors=(1, 2, 3), rotorloc=[0, 0, 0], rotor1=None,
                 rotor2=None, rotor3=None, rotor4=None, rotor5=None,
                 endscrambler=None, charset=None, forcecaps=True):
        """ Create a new Enigma object.

Note: None means default. Default is not the Enigma default.

Create a new Enigma object """
        
        self._setupcharswap(charset, forcecaps)

        if rotor1:
            self._r1 = rotor1
        else:
            self._r1 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                        11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18,
                        19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25}

        if rotor2:
            self._r2 = rotor2
        else:
            self._r2 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                        11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18,
                        19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25}
        if rotor3:
            self._r3 = rotor3
        else:
            self._r3 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                        11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18,
                        19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25}
        if rotor4:
            self._r4 = rotor4
        else:
            self._r4 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                        11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18,
                        19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25}
        if rotor5:
            self._r5 = rotor5
        else:
            self._r5 = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                        11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18,
                        19:19, 20:20, 21:21, 22:22, 23:23, 24:24, 25:25}
        if endscrambler:
            self._scre = endscrambler
        else:
            self._scre = {0:2, 1:3, 2:0, 3:1, 4:9, 5:24, 6:7, 7:6, 8:10, 9:4,
                          10:8, 11:16, 12:22, 13:17, 14:18, 15:19, 16:11, 17:13,
                          18:14, 19:15, 20:25, 21:23, 22:12, 23:21, 24:5, 25:20}

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
                self._chset[x] = chl[x]
                self._chset[chl[x]] = x

    def _caps(self, txt):
        return(txt.upper())

    def _endscramble(self, n):
        return(self._scre[n])
