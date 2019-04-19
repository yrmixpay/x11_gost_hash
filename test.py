import x11_gost_hash
from binascii import unhexlify, hexlify

import unittest

# yrmixcoin block #1
# yrmixcoin@b1:~/.yrmixcoin$ yrmixcoin-cli getblockhash 1
# 00000365ec975434eda669cc8ca78b94e1de088e12425fa56d38374a58bdee7a
# yrmixcoin@b1:~/.yrmixcoin$ yrmixcoin-cli getblock 00000365ec975434eda669cc8ca78b94e1de088e12425fa56d38374a58bdee7a
#{
#    "hash" : "00000365ec975434eda669cc8ca78b94e1de088e12425fa56d38374a58bdee7a",
#    "confirmations" : 3,
#    "size" : 179,
#    "height" : 1,
#    "version" : 20000000,
#    "merkleroot" : "cc5c480285146417c83251bc5cdf6dae6aa7d335955b28a0cf2845a068270c09",
#    "tx" : [
#        "cc5c480285146417c83251bc5cdf6dae6aa7d335955b28a0cf2845a068270c09"
#    ],
#    "time" : 1555715011, 
#    "nonce" : 55488,
#    "bits" : "1e0ffff0",
#    "difficulty" : 0.000244140625,
#    "chainwork" : "0000000000000000000000000000000000000000000000000000000000200020",
#    "previousblockhash" : "00000d87443123cc4848baa166279698b0eb529698c4440ff85cf03ca94dff12",
#    "nextblockhash" : "00000c7c9563b9875a7dc8bfba10b8f42efc150a004dfb90e2cf8c16452c0830"
#}


header_hex = ("00000020" +
    "12ff4da93cf05cf80f44c4989652ebb098962766a1ba4848cc233144870d0000" +
    "090c2768a04528cfa0285d9535d3a76aae6ddf5cbc5132c81764148502485ccc "
    "c353ba5c" +
    "f0ff0f1e" +
    "c0d80000")

best_hash = '7aeebd584a37386da5a55f42128e08dee1948ba78ccc69a6ed345497ec65030000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_x11_gost_hash(self):
        self.pow_hash = hexlify(x11_gost_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

