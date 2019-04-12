import x11_gost_hash
from binascii import unhexlify, hexlify

import unittest

# Yrmixcoin block #0
# yrmix@b1:~/.syrmixcoin$ yrmixcoin-cli getblockhash 0
# 00000d87443123cc4848baa166279698b0eb529698c4440ff85cf03ca94dff12
# yrmix@b1:~/.yrmixcoin$ yrmixcoin-cli getblock 00000d87443123cc4848baa166279698b0eb529698c4440ff85cf03ca94dff12
#{
#    "hash": "00000d87443123cc4848baa166279698b0eb529698c4440ff85cf03ca94dff12",
#    "confirmations": 1,
#    "size": 288,
#    "height": 0,
#    "version": 1,
#    "merkleroot" : "8db686f7eabfe0ba61e2e0601f3bd557a5926da4f68fa96fe1dafa5b98980c91",
#    "tx" : [
#        "8db686f7eabfe0ba61e2e0601f3bd557a5926da4f68fa96fe1dafa5b98980c91"
#    ],
#    "time" : 1431130209,
#    "nonce" : 569046,
#    "bits" : "1e0ffff0",
#    "difficulty" : 0.00024414,
#    "merkleroot": "2e3875684e7dbaa1b97a91aad29f0a7c2633b2c9f81401a9ebd326a08b42489d",
#    "previousblockhash" : "00000c492bf73490420868bc577680bfc4c60116e7e85343bc624787c21efa4c",
#    "nextblockhash" : "00000722c462136d5a41d80f3a7f36f24777e4276b7e141933649fc47dddd071"
#}

header_hex = ("03000000" +
    "4cfa1ec2874762bc4353e8e71601c6c4bf807657bc6808429034f72b490c0000" +
    "910c98985bfadae16fa98ff6a46d92a557d53b1f60e0e261bae0bfeaf786b68d"
    "61504d55" +
    "f0ff0f1e" +
    "d6ae0800")

best_hash = 'b0d98c92637728f6770e87d505ca390e1ed653c71fa4654491abae235b080000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_x11_gost_hash(self):
        self.pow_hash = hexlify(x11_gost_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

