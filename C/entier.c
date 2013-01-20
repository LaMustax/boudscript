/* 3.3.9 */
#include <stdio.h>

main() {
	int nombre1, nombre2;

	printf("Entrer deux entiers : ");
	scanf("%d %d", &nombre1, &nombre2);

	/* Pour sauter une ligne lorsque l'on écrit une chaîne dans le programme,
	   il suffit de mettre un antislash en fin de ligne (sans espace)

	   Du coup on fait un printf de la mort qui reste lisible :
	*/
	printf("\nRésultat de :\n \
	* %d + %d : %d\n \
	* %d - %d : %d\n \
	* %d * %d : %d\n \
	* %d / %d : %d\n \
	* %d %% %d : %d\n",
	nombre1, nombre2, nombre1+nombre2,
	nombre1, nombre2, nombre1-nombre2,
	nombre1, nombre2, nombre1*nombre2,
	nombre1, nombre2, nombre1/nombre2,
	nombre1, nombre2, nombre1%nombre2
	);
}

/*
Entrer deux entiers : 5 2

Résultat de :
 	* 5 + 2 : 7
 	* 5 - 2 : 3
 	* 5 * 2 : 10
 	* 5 / 2 : 2
 	* 5 % 2 : 1
*/