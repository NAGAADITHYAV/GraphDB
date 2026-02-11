import unittest
from DB.encoder import Encoder

class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.encoder = Encoder()

    def test_encode_decode_basic(self):
        id = 123
        name = "Test Node"
        encoded = self.encoder.encodeNode(id, name)
        decoded_id, decoded_name = self.encoder.decodeNode(encoded)
        self.assertEqual(id, decoded_id)
        self.assertEqual(name, decoded_name)

    def test_encode_decode_empty_string(self):
        id = 456
        name = ""
        encoded = self.encoder.encodeNode(id, name)
        decoded_id, decoded_name = self.encoder.decodeNode(encoded)
        self.assertEqual(id, decoded_id)
        self.assertEqual(name, decoded_name)

    def test_encode_decode_special_chars(self):
        id = 789
        name = "Node with @#$%^&*()"
        encoded = self.encoder.encodeNode(id, name)
        decoded_id, decoded_name = self.encoder.decodeNode(encoded)
        self.assertEqual(id, decoded_id)
        self.assertEqual(name, decoded_name)
    
    def test_encode_decode_unicode(self):
        id = 999
        name = "Node with emoji 🚀"
        encoded = self.encoder.encodeNode(id, name)
        decoded_id, decoded_name = self.encoder.decodeNode(encoded)
        self.assertEqual(id, decoded_id)
        self.assertEqual(name, decoded_name)

if __name__ == '__main__':
    unittest.main()
