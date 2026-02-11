
import struct
class Encoder:

    def encodeNode(self, id, node_name):
        """
        Encodes a node ID and name into bytes.
        Format: [ID (4 bytes)] + [Name Length (4 bytes)] + [Name Bytes]
        """
        # Encode strings to bytes
        name_bytes = node_name.encode('utf-8')
        name_len = len(name_bytes)
        
        # Pack ID and name length as 4-byte unsigned integers (Big Endian)
        header = struct.pack('>II', id, name_len)
        
        return header + name_bytes

    def decodeNode(self, data):
        """
        Decodes bytes back into a node ID and name.
        """
        # Unpack ID and name length from the first 8 bytes
        id, name_len = struct.unpack('>II', data[:8])
        
        # Extract name bytes and decode
        name_bytes = data[8:8+name_len]
        node_name = name_bytes.decode('utf-8')
        
        return id, node_name