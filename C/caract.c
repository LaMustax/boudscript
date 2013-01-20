/* 3.5.10 */
#include <stdio.h>

main() {
	char majuscule;

	printf("Entrer une majuscule : ");
	scanf("%c", &majuscule);

	/* On passe du caractère au code ASCII rien qu'en l'affichant comme un entier

	   Pour passer de la majuscule à la minuscule, il suffit d'ajouter la différence
	   entre une majuscule et une minuscule (voir la table ASCII). On peut prendre 'A'
	   comme on peut prendre 'Z' ou 'Y', etc.
	*/
	printf("Code ascii : %i\nMinuscule : %c\n",
	majuscule,
	majuscule + ('a' - 'A')
	);
}