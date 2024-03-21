arm:
	aarch64-linux-gnu-gcc chal.c -no-pie -o  exparm
final:
	aarch64-linux-gnu-gcc chal.c -no-pie -o  chal

static:
	aarch64-linux-gnu-gcc chal.c -o expstatic -static

clean:
	rm exparm

patch:
	patchelf --set-interpreter ld-linux-aarch64.so.1 --set-rpath . exparm
