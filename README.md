Creatign a Custom GraphDB in Go lang

TARGETS

Write targets
storage of uniqe stings (Name of nodes in the Graph)
storage of connections between the strings(edges in the Graph)

Read targets
Quickly lookup for the string (node lookup)
Quickly find paths between a given source  and destination node.

Architecture(v0.0)
Storage will have pages of size 5MB each,
Maximum pages allowed in Memory is 100 pages.

page Design
+---------------------------------------------------+
| Page Header (64 bytes)                             |
+---------------------------------------------------+
| Payload (NodeMeta records / BTree / adjacency)    |
+---------------------------------------------------+

page Header 

Offset  Size  Field
---------------------------------------------------------
0       4     MagicNumber        uint32
4       1     PageType           uint8
5       1     PageVersion        uint8
6       2     Flags              uint16
8       8     PageID             uint64
16      8     LSN                uint64
24      8     Checksum           uint64
32      4     PayloadStart       uint32
36      4     PayloadEnd         uint32
40      4     RecordCount        uint32
44      4     Reserved           uint32
48      16    Reserved / Padding
---------------------------------------------------------
Total: 64 bytes
