/* 3.6.3.4 */
#include <stdio.h>

main() {
	int a, b, c;
	
	printf("Entrer trois entiers : ");
	scanf("%d %d %d", &a, &b, &c);

	if((a<b) && (a<c)){
		printf("VRAI\n");
	}
	else{
		printf("FAUX\n");
	}
}

/*
Entrer trois entiers : 1 2 3
VRAI

Entrer trois entiers : 3 2 1
FAUX
*/