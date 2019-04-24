import x11_gost_hash
from binascii import unhexlify, hexlify

import unittest

# yrmixcoin block #1
# ivan@b1:~/.yrmixcoin$ yrmixcoin-cli getblockhash 1
# 000001c9dbe16f2336f4fefca8226e214a61e21c2b7b7bd31b74e63909ee09b9
# ivan@b1:~/.yrmixcoin$ yrmixcoin-cli getblock 000001c9dbe16f2336f4fefca8226e214a61e21c2b7b7bd31b74e63909ee09b9
#{
#    "hash" : "000001c9dbe16f2336f4fefca8226e214a61e21c2b7b7bd31b74e63909ee09b9",
#    "confirmations" : 1,
#    "size" : 179,
#    "height" : 1,
#    "version" : 20000000,
#    "merkleroot" : "eb268b61804ad6c8438f353f9280b587888b213943d138d2bd534312465debd1",
#    "tx" : [
#        "eb268b61804ad6c8438f353f9280b587888b213943d138d2bd534312465debd1"
#    ],
#    "time" : 1556120338,
#    "nonce" : 2853,
#    "bits" : "1e0ffff0",
#    "difficulty" : 000244140625,
#    "chainwork" : "0000000000000000000000000000000000000000000000000000000000200020",
#    "previousblockhash" : "000003ca5c682e062b5ccc430f553bab45446d7d331cc6b188086ece99a8eba2",
#    "nextblockhash" : "00000c7c9563b9875a7dc8bfba10b8f42efc150a004dfb90e2cf8c16452c0830"
#}

header_hex = ("00000020" +
    "a2eba899ce6e0888b1c61c337d6d4445ab3b550f43cc5c2b062e685cca030000" +
    "d1eb5d46124353bdd238d14339218b8887b580923f358f43c8d64a80618b26eb"
    "1283c05c" +
    "f0ff0f1e" +
    "250b0000")

best_hash = 'b909ee0939e6741bd37b7b2b1ce2614a216e22a8fcfef436236fe1dbc9010000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_x11_gost_hash(self):
        self.pow_hash = hexlify(x11_gost_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

