#include <stdio.h>
#include <time.h>

int main() {
 	char feedback[100];
        fgets(feedback, 0x100, stdin);
        printf(feedback);
        puts("Thanks!");	

}
