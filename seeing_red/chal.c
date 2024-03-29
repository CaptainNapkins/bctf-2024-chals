#include <stdio.h>
#include <string.h>

char ticket[40];

void use_ticket(char *ticket) {
	FILE *fp = fopen("flag.txt", "r");
	if (fp == NULL) {
		printf("flag.txt not found");
		return;
	}
	int yo = fgets(ticket, 39, fp); 
}	

int main() {
	char buff[56];
	char song[20];
	//puts("Help! I idk where my eras ticket went!!");
	//puts("Last I saw it I think I put it in a buffer somewhere...");
	//printf("Do you know where it could be??! ");
	puts("I was going to go to the eras tour, but something came up :(");
	puts("You can have my ticket! Only thing is... I forgot where I put it...");
	printf("Do you know where it could be?! ");
	fgets(buff, 64, stdin);

	fflush(stdin);

	printf("\nsooo... anyways whats your favorite Taylor Swift song? ");
	// insert my favorite
	fgets(song, 19, stdin);	
	strtok(song, "\n");
	printf("Oooh!! ");
	printf(song);
	printf("! Thats a good one!\n");
	use_ticket(ticket);
	printf(ticket);
	
}
	

	
