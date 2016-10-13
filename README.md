### Parse PIT

- It's based on the source code from Google, used to locate the image on your device (eMMC or UFS).


```
$ ./pitparser.py sample.pit

Magic: 0x12349876
Count: 22
---------------------
Partition ID: 80
Name: BOOTLOADER
File Name: sboot.bin
Delta Name:
Binary: 0
Device: 8
Blkstart: 0
Blknum: 1024
Offset: 1
filesize: 0
---------------------
Partition ID: 90
Name: CM
File Name: cm.bin
Delta Name:
Binary: 0
Device: 8
Blkstart: 0
Blknum: 1024
Offset: 2
filesize: 0

...

```
