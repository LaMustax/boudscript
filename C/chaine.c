/* 4.1.9 */
#include <stdio.h>
#include <ctype.h>  /* pour toupper() */
#include <string.h> /* pour strlen()  */

main() {
	char nom[100];
	int longueur;
	
	printf("Entrer un nom : ");
	scanf("%s", nom); /* pas la peine de mettre & puisqu'on a déjà une référence */

	nom[0] = toupper(nom[0]); /* On modifie le premier caractère */
	longueur = strlen(nom);

	printf("\nNom : %s\nLongueur : %i\n", nom, longueur);
}

/* 
Entrer un nom : leJeannot

Nom : LeJeannot
Longueur : 9
*/