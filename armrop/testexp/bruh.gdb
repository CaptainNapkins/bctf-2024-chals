init-pwndbg
set arch aarch64
file chalarm
tar ext :1234
break *get_address
break *(feedback + 108)
continue
# display $x0
# display $x1
# display $x2
# display $x29
# display $x30
# display/20gx $sp
# display/5i $pc
