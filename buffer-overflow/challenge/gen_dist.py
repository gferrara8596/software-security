#!/usr/bin/env python3

import struct
from pwn import *

ptrs_base_addr = 0x56559094
pat_on_back_addr = 0xffffd14c
reg_size = 4

offset = int(-(ptrs_base_addr - pat_on_back_addr) / reg_size)

print(offset)
