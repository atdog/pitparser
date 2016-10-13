#!/usr/bin/env python

from pwn import *
import sys

class Part:
    def __init__(self, data):
        self.__parse_part(data)

    def __parse_part(self, data):
        self.binary = u32(data[0:4])
        self.device = u32(data[4:8])

        self.id = u32(data[8:12])

        self.attribute = u32(data[12:16])
        self.update = u32(data[16:20])

        self.blkstart = u32(data[20:24])
        self.blknum = u32(data[24:28])
        self.offset = u32(data[28:32])
        self.filesize = u32(data[32:36])

        self.name = data[36:68].replace('\x00', '')
        self.filename = data[68:100].replace('\x00', '')
        self.deltaname = data[100:].replace('\x00', '')

class PIT:
    def __init__(self, data):
        self.__parse_pit(data)
        
    def __parse_pit(self, data):
        self.magic = u32(data[0:4])
        self.count = u32(data[4:8])
        self.dummy = data[8:28]
        self.partitions = self.__parse_part_info(data[28:])
        self.signature = data[-256:].encode('hex')

    def __parse_part_info(self, data):
        result = []

        for _ in xrange(self.count):
            part = data[0:132]
            data = data[132:]
            result.append(Part(part))

        return result

argv = sys.argv

if len(argv) != 2:
    print argv[0] + " [pit_file]" 
    sys.exit(0)

with open(argv[1], 'rb') as fh:
    data = fh.read()

    pit = PIT(data)

    print "Magic: " + hex(pit.magic)
    print "Count: " + str(pit.count)

    for i in xrange(pit.count):
        part = pit.partitions[i]
        print "---------------------"
        print "Partition ID: " + str(part.id)
        print "Name: " + part.name
        print "File Name: " + part.filename
        print "Delta Name: " + part.deltaname
        print "Binary: " + str(part.binary)
        print "Device: " + str(part.device)
        print "Blkstart: " + str(part.blkstart)
        print "Blknum: " + str(part.blknum)
        print "Offset: " + str(part.offset)
        print "filesize: " + str(part.filesize)

    print "---------------------"
    print "Signature: " + pit.signature
