# Ideation
- Situation is
	- "I lost my ticket to the ERAs tour! Only you can help me find it"

- But idk, need to make a fun spin
	- Cant leak straight off the stack and cant just do what 
	sigpwny's chal does where you put an address on the stack to read from

- Maybe a ROP one where you have to ROP and place the flag buff on stack somehow?
	- Would have to give em a small overflow to prevent libc
	- hmmmm, could be interesting
		- Maybe the designer "Lost the flag" in the buffers within the program lol and couldn't find it
			- And maybe its from the point of view of the ticket designer, ticketmaster, or tour manager and 
			taylor will be mad if she finds out lol
	- Maybe he lost is ticket code?
		- he lost is voucher trying to write a bot lmao 

## Notes
- jack pointed out that we can use the read function to avoid the mutex problem i was having with
fgets and scanf since itll just use the read syscall




