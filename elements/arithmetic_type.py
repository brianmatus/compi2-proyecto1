from enum import Enum

ArithmeticType = Enum('ArithmeticType',
                   ' '.join([
                       "SUM",
                       "SUB",
                       "MULT",
                       "DIV",
                       "POW",
                       "MOD",
                       "NEG"
                   ]))
