```s
[KGL] WSL -  cou: 01-operating-syste-overview on chore/study [ base 3.9.12] [ﳑ 1.13.8] ❯ readelf -h pause
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x401050
  Start of program headers:          64 (bytes into file)
  Start of section headers:          14648 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         13
  Size of section headers:           64 (bytes)
  Number of section headers:         31
  Section header string table index: 30
```

`Entry point address:               0x401050`

```s
[KGL] WSL -  cou: 01-operating-syste-overview on chore/study [ base 3.9.12] [ﳑ 1.13.8] ❯ readelf -S pause
There are 31 section headers, starting at offset 0x3938:

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         0000000000400318  00000318
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.gnu.propert NOTE             0000000000400338  00000338
       0000000000000020  0000000000000000   A       0     0     8
  [ 3] .note.gnu.build-i NOTE             0000000000400358  00000358
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .note.ABI-tag     NOTE             000000000040037c  0000037c
       0000000000000020  0000000000000000   A       0     0     4
  [ 5] .gnu.hash         GNU_HASH         00000000004003a0  000003a0
       000000000000001c  0000000000000000   A       6     0     8
  [ 6] .dynsym           DYNSYM           00000000004003c0  000003c0
       0000000000000060  0000000000000018   A       7     1     8
  [ 7] .dynstr           STRTAB           0000000000400420  00000420
       000000000000003e  0000000000000000   A       0     0     1
  [ 8] .gnu.version      VERSYM           000000000040045e  0000045e
       0000000000000008  0000000000000002   A       6     0     2
  [ 9] .gnu.version_r    VERNEED          0000000000400468  00000468
       0000000000000020  0000000000000000   A       7     1     8
  [10] .rela.dyn         RELA             0000000000400488  00000488
       0000000000000030  0000000000000018   A       6     0     8
  [11] .rela.plt         RELA             00000000004004b8  000004b8
       0000000000000018  0000000000000018  AI       6    24     8
  [12] .init             PROGBITS         0000000000401000  00001000
       000000000000001b  0000000000000000  AX       0     0     4
  [13] .plt              PROGBITS         0000000000401020  00001020
       0000000000000020  0000000000000010  AX       0     0     16
  [14] .plt.sec          PROGBITS         0000000000401040  00001040
       0000000000000010  0000000000000010  AX       0     0     16
  [15] .text             PROGBITS         0000000000401050  00001050
       0000000000000175  0000000000000000  AX       0     0     16
  [16] .fini             PROGBITS         00000000004011c8  000011c8
       000000000000000d  0000000000000000  AX       0     0     4
  [17] .rodata           PROGBITS         0000000000402000  00002000
       0000000000000004  0000000000000004  AM       0     0     4
  [18] .eh_frame_hdr     PROGBITS         0000000000402004  00002004
       0000000000000044  0000000000000000   A       0     0     4
  [19] .eh_frame         PROGBITS         0000000000402048  00002048
       0000000000000100  0000000000000000   A       0     0     8
  [20] .init_array       INIT_ARRAY       0000000000403e10  00002e10
       0000000000000008  0000000000000008  WA       0     0     8
  [21] .fini_array       FINI_ARRAY       0000000000403e18  00002e18
       0000000000000008  0000000000000008  WA       0     0     8
  [22] .dynamic          DYNAMIC          0000000000403e20  00002e20
       00000000000001d0  0000000000000010  WA       7     0     8
  [23] .got              PROGBITS         0000000000403ff0  00002ff0
       0000000000000010  0000000000000008  WA       0     0     8
  [24] .got.plt          PROGBITS         0000000000404000  00003000
       0000000000000020  0000000000000008  WA       0     0     8
  [25] .data             PROGBITS         0000000000404020  00003020
       0000000000000010  0000000000000000  WA       0     0     8
  [26] .bss              NOBITS           0000000000404030  00003030
       0000000000000008  0000000000000000  WA       0     0     1
  [27] .comment          PROGBITS         0000000000000000  00003030
       000000000000002a  0000000000000001  MS       0     0     1
  [28] .symtab           SYMTAB           0000000000000000  00003060
       00000000000005e8  0000000000000018          29    45     8
  [29] .strtab           STRTAB           0000000000000000  00003648
       00000000000001ca  0000000000000000           0     0     1
  [30] .shstrtab         STRTAB           0000000000000000  00003812
       000000000000011f  0000000000000000           0     0     1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  l (large), p (processor specific)
```

```s
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
...
  [15] .text             PROGBITS         0000000000401050  00001050
       0000000000000175  0000000000000000  AX       0     0     16
...
  [25] .data             PROGBITS         0000000000404020  00003020
       0000000000000010  0000000000000000  WA       0     0     8
```

```s
[KGL] WSL -  cou: 01-operating-syste-overview on chore/study [ base 3.9.12] [ﳑ 1.13.8] ❯ ./pause &
[1] 22448
```

```s
[KGL] WSL -  cou: 01-operating-syste-overview on chore/study [ base 3.9.12] [ﳑ 1.13.8] ❯ cat /proc/22448/maps
00400000-00401000 r--p 00000000 08:20 222423                             /home/cou/dev/12_study/linux-in-practice-2nd/study/01-operating-syste-overview/pause
00401000-00402000 r-xp 00001000 08:20 222423                             /home/cou/dev/12_study/linux-in-practice-2nd/study/01-operating-syste-overview/pause
00402000-00403000 r--p 00002000 08:20 222423                             /home/cou/dev/12_study/linux-in-practice-2nd/study/01-operating-syste-overview/pause
00403000-00404000 r--p 00002000 08:20 222423                             /home/cou/dev/12_study/linux-in-practice-2nd/study/01-operating-syste-overview/pause
00404000-00405000 rw-p 00003000 08:20 222423                             /home/cou/dev/12_study/linux-in-practice-2nd/study/01-operating-syste-overview/pause
7fd32b9f9000-7fd32ba1b000 r--p 00000000 08:20 64854                      /usr/lib/x86_64-linux-gnu/libc-2.31.so
7fd32ba1b000-7fd32bb93000 r-xp 00022000 08:20 64854                      /usr/lib/x86_64-linux-gnu/libc-2.31.so
7fd32bb93000-7fd32bbe1000 r--p 0019a000 08:20 64854                      /usr/lib/x86_64-linux-gnu/libc-2.31.so
7fd32bbe1000-7fd32bbe5000 r--p 001e7000 08:20 64854                      /usr/lib/x86_64-linux-gnu/libc-2.31.so
7fd32bbe5000-7fd32bbe7000 rw-p 001eb000 08:20 64854                      /usr/lib/x86_64-linux-gnu/libc-2.31.so
7fd32bbe7000-7fd32bbed000 rw-p 00000000 00:00 0 
7fd32bbf7000-7fd32bbf8000 r--p 00000000 08:20 64849                      /usr/lib/x86_64-linux-gnu/ld-2.31.so
7fd32bbf8000-7fd32bc1b000 r-xp 00001000 08:20 64849                      /usr/lib/x86_64-linux-gnu/ld-2.31.so
7fd32bc1b000-7fd32bc23000 r--p 00024000 08:20 64849                      /usr/lib/x86_64-linux-gnu/ld-2.31.so
7fd32bc24000-7fd32bc25000 r--p 0002c000 08:20 64849                      /usr/lib/x86_64-linux-gnu/ld-2.31.so
7fd32bc25000-7fd32bc26000 rw-p 0002d000 08:20 64849                      /usr/lib/x86_64-linux-gnu/ld-2.31.so
7fd32bc26000-7fd32bc27000 rw-p 00000000 00:00 0 
7ffc78214000-7ffc78236000 rw-p 00000000 00:00 0                          [stack]
7ffc782d0000-7ffc782d4000 r--p 00000000 00:00 0                          [vvar]
7ffc782d4000-7ffc782d5000 r-xp 00000000 00:00 0                          [vdso]
```