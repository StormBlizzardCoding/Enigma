# Enigma Defaults

rotor1, rotor2, rotor3, rotor4, rotor5, reflect1, reflect2, reflect3 =
{}, {}, {}, {}, {}, {}, {}, {}
rmaps = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
         "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO",
         "ESOVPZJAYQUIRHXLNFTGKDCMWB", "VZBRGITYUPSDNHLXAWMJQOFECK",
         "EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT",
         "FVPJIAOYEDRZXWGCTKUQSBNMHL"]

turnpoints = ["z", "q", "e", "v", "j", "z"]

for x in range(0,26):
    rotor1[rmaps[0][x]] = rmaps[1][x]
    rotor2[rmaps[0][x]] = rmaps[2][x]
    rotor3[rmaps[0][x]] = rmaps[3][x]
    rotor4[rmaps[0][x]] = rmaps[4][x]
    rotor5[rmaps[0][x]] = rmaps[5][x]
    reflect1[rmaps[0][x]] = rmaps[6][x]
    reflect2[rmaps[0][x]] = rmaps[7][x]
    reflect3[rmaps[0][x]] = rmaps[8][x]
