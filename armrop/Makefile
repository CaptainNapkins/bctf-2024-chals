arm:
	aarch64-linux-gnu-gcc chal.c -pie -o chalarm
armnopie:
	aarch64-linux-gnu-gcc chal.c -no-pie -o chalnopie

reg:
	gcc chal.c -o chal64
armstatic:
	aarch64-linux-gnu-gcc chal.c -o chalar -static-pie

clean:
	rm chal64
	rm chalarm
