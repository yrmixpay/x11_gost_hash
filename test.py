import x11_gost_hash
from binascii import unhexlify, hexlify

import unittest

# yrmixcoin block #1
# yrmixcoin@b1:~/.yrmixcoin$ yrmixcoin-cli getblockhash 1
# 000005b3f9ab5ffcef68cfa3d76bbaf259e6e546a7bf6d7acd349edfed361080
# yrmixcoin@b1:~/.yrmixcoin$ yrmixcoin-cli getblock 000005b3f9ab5ffcef68cfa3d76bbaf259e6e546a7bf6d7acd349edfed361080
#{
#    "hash" : "000005b3f9ab5ffcef68cfa3d76bbaf259e6e546a7bf6d7acd349edfed361080",
#    "confirmations" : 1,
#    "size" : 169,
#    "height" : 1,
#    "version" : 20000000,
#    "merkleroot" : "0bed774890c67025be6ed8ee5243f4114fff40602d974776ea72411193ef28b7",
#    "tx" : [
#        "0bed774890c67025be6ed8ee5243f4114fff40602d974776ea72411193ef28b7"
#    ],
#    "time" : 1555543013, 
#    "nonce" : 21170,
#    "bits" : "1e0ffff0",
#    "difficulty" : 0.000244140625,
#    "chainwork" : "0000000000000000000000000000000000000000000000000000000000200020",
#    "previousblockhash" : "00000d87443123cc4848baa166279698b0eb529698c4440ff85cf03ca94dff12",
#    "nextblockhash" : "00000f4c2843ee8c08de6739bd4fe42ddea33b9b775132502865892bbcee1b42"
#}

header_hex = ("00000020" +
    "12ff4da93cf05cf80f44c4989652ebb098962766a1ba4848cc233144870d0000" +
    "b728ef93114172ea7647972d6040ff4f11f44352eed86ebe2570c6904877ed0b"
    "e5b3b75c" +
    "f0ff0f1e" +
    "b2520000")

best_hash = '801036eddf9e34cd7a6dbfa746e5e659f2ba6bd7a3cf68effc5fabf9b3050000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_x11_gost_hash(self):
        self.pow_hash = hexlify(x11_gost_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

