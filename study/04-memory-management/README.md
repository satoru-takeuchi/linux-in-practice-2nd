
[図解でわかるSpectreとMeltdown](https://speakerdeck.com/sat/tu-jie-dewakaruspectretomeltdown)
[Reading privileged memory with a side-channel](https://googleprojectzero.blogspot.com/2018/01/reading-privileged-memory-with-side.html)
[Meltdown: Reading Kernel Memory from User Space](https://www.usenix.org/conference/usenixsecurity18/presentation/lipp)

## mmap

```s
$ ./mmap 
*** 新規メモリ領域獲得前のメモリマップ ***
...
7f860365f000-7f8605910000 rw-p 00000000 00:00 0 
...

*** 新規メモリ領域: アドレス = 0x7f85c365f000, サイズ = 0x40000000 ***

*** 新規メモリ領域獲得後のメモリマップ ***
...
7f85c365f000-7f8605910000 rw-p 00000000 00:00 0 
...
```

0x7f860365f000 - 0x7f85c365f000 = 0x40000000