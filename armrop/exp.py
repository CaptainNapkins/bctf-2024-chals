from pwn import *

elf = context.binary = ELF('chalarm')
