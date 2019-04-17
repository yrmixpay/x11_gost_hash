import x11_gost_hash
from binascii import unhexlify, hexlify

import unittest

# yrmixcoin block #1
# ivan@b1:~/.yrmixcoin$ yrmixcoin-cli getblockhash 1
# 0000024a1ede3e643c6beabfbffef7d0be6f96175d870f524671f46ca9bc8edd
# ubuntu@b1:~/.yrmixcoin$ yrmixcoin-cli getblock 0000024a1ede3e643c6beabfbffef7d0be6f96175d870f524671f46ca9bc8edd
#{
#    "hash" : "0000024a1ede3e643c6beabfbffef7d0be6f96175d870f524671f46ca9bc8edd",
#    "confirmations" : 1,
#    "size" : 179,
#    "height" : 1,
#    "version" : 20000000,
#    "merkleroot" : "044cbb591e616d75def4e8e62f6c8443624f8aba9e3a62e62e5ff1c5c8c59f71",
#    "tx" : [
#        "044cbb591e616d75def4e8e62f6c8443624f8aba9e3a62e62e5ff1c5c8c59f71"
#    ],
#    "time" : 1555423404,
#    "nonce" : 7189,
#    "bits" : "1e0ffff0",
#    "difficulty" : 000244140625,
#    "chainwork" : "0000000000000000000000000000000000000000000000000000000000200020",
#    "previousblockhash" : "00000c492bf73490420868bc577680bfc4c60116e7e85343bc624787c21efa4c",
#    "nextblockhash" : "00000d87443123cc4848baa166279698b0eb529698c4440ff85cf03ca94dff12"
#}

header_hex = ("02000000" +
    "8b1571d81c37123a73e0273bcaaf77eff9401a930e2cb499dcb72fdfaf47dd23" +
    "8fb363378365ef92c076efd83a074d960369813416b47a06963b2b59c3e5ec4b"
    "1555423404" +
    "1e0ffff0" +
    "7189")

best_hash = '0000024a1ede3e643c6beabfbffef7d0be6f96175d870f524671f46ca9bc8edd'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_x11_gost_hash(self):
        self.pow_hash = hexlify(x11_gost_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

