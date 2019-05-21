import x11_gost_hash
from binascii import unhexlify, hexlify

import unittest

# Yrmixcoin block #1
# yrmixcoin@b1:~/.yrmixcoin$ yrmixcoin-cli getblockhash 1
# 000009dc863579fc5c6ec9d7c65997b0a27cf5cdfece9a2f73c80eaa2bb76506
# yrmixcoin@b1:~/.yrmixcoin$ yrmixcoin-cli getblock 000009dc863579fc5c6ec9d7c65997b0a27cf5cdfece9a2f73c80eaa2bb76506
#{
#    "hash" : "000009dc863579fc5c6ec9d7c65997b0a27cf5cdfece9a2f73c80eaa2bb76506",
#    "confirmations" : 9040,
#    "size" : 179,
#    "height" : 1,
#    "version" : 2,
#    "merkleroot" : "ccc1ece42fa6fb1974de4e645f2acaf791941909167939ec28033555a6244d0f",
#    "tx" : [
#        "ccc1ece42fa6fb1974de4e645f2acaf791941909167939ec28033555a6244d0f"
#    ],
#    "time" : 1556748307,
#    "nonce" : 8892,
#    "bits" : "1e0ffff0",
#    "difficulty" : 0.00024414,
#    "chainwork" : "0000000000000000000000000000000000000000000000000000000000200020",
#    "previousblockhash" : "00000e3b098df459b7c4adced7630106bdf2dbc85f2fc63b8c7c7fc434cfdc0e",
#    "nextblockhash" : "00000e51c1c4215748a716bfdbe7585cf7a9b1e4360593c62b09ad723de08d57"
#}

header_hex = ("00000020" +
    "0edccf34c47f7c8c3bc62f5fc8dbf2bd060163d7ceadc4b759f48d093b0e0000" +
    "0f4d24a655350328ec39791609199491f7ca2a5f644ede7419fba62fe4ecc1cc"
    "1318ca5c" +
    "f0ff0f1e" +
    "bc220000")

best_hash = '0665b72baa0ec8732f9acefecdf57ca2b09759c6d7c96e5cfcfc3586dc090000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_x11_gost_hash(self):
        self.pow_hash = hexlify(x11_gost_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

