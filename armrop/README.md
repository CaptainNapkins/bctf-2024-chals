## Notes
- Simple arm rop chal
- Write flag to data section and go back to libc
	- Do we want no canary or leak canary + ROP
- Static or dynamic linking? Dynamic linking seems hella annoying, idk

## Scenario ideas
- Something about buying arms and legs idk
- Have a choice to either buy an arm or a leg
	- But what happens when you buy it?
	- need a way to print canary since i don't wanna disable it
- printf to leak canary and pie
	- In "feedback" take name (printf vuln) then have the bof and thats the ROP
	- OR, we have them guess a random number to become worthy of taking an arm and or leg


## Description Ideation
- "When something costs and arm and a leg, have you ever thought, what if you could buy more arms and legs?" 



