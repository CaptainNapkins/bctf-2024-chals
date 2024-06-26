#include <stdio.h>
#include <time.h>

int main() {
  setup();
  int choice;
  puts("Hello! \nWelcome to ARMs and Legs, here for all of your literal and metaphorical needs!");
  print_menu();
  scanf("%d", &choice);
  
  switch (choice) {
	  case 1:
		puts("So, you'd like to purchase an ARM...are you worthy enough to purchase such an appendage?");
		if (!worthyness_tester()) {
			get_address();
			feedback();
		} else {
			puts("Close, but no cigar. Maybe try a Leg?");
		}
		break;
	 case 2:
		puts("So, you'd like to purchase a Leg...are you worthy enough to purchase such an appendage?!");
                if (!worthyness_tester()) {
                        get_address();
                        feedback();
		} else {
                        puts("Close, but no cigar. Maybe try an ARM?");
		}
		break;

	puts("Thanks for shopping with us! Bye!");
  }
 }

void setup() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int trng() {
	int num;
	int random_num;
	num = (time(0) * 69) % 44;
	return num;
}

int worthyness_tester() {
	int num; 
	int random_num;
	puts("What number am I thinking of?");
	//random_num = trng();
	random_num = 1337;
	scanf("%d", &num);
	if (num == random_num) {
		printf("Wow, you may now purchase an appendage!");
		return 0;
	} else {
		return 1;
	}
}

void get_address() {
	char address[36];
        printf("\tCould we have an address to ship said appendage? ");
	scanf("%34s", address);
        printf("\nThanks, we will ship to: ");
        printf(address);
	printf("\n");
	clear_buffer();
}

void feedback() {
	char feedback[104];
	puts("Care to leave some feedback?!");
	fgets(feedback, 0x104, stdin);
	for (int i = 0; feedback[i] != '\0'; i++) {
		if (feedback[i] == '\n') {
			feedback[i] = '\0';
			break;
		}
	}
	puts("Thanks!");
}

void clear_buffer() {
	int c;
    	while ((c = getchar()) != '\n' && c != EOF);
}
	
void print_menu() {
  puts("What are you in the market for today?");
  puts("1. ARMs");
  puts("2. Legs");
}
