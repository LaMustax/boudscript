/* 3.6.3.4 */
#include <stdio.h>

main() {
	int nb, filtre, resultat;
	
	printf("Entrer un nombre : ");
	scanf("%d", &nb);

	filtre = 0xF; /* En héxadécimal (indiqué par 0x...), F correspond à 1111 en binaire */
	resultat = nb & filtre; /* On applique le filtre sur le nombre à filtrer */

	printf("\nRésultat : %d\n", resultat);
}

/* On ne garde que les 4 premiers bits donc : 15 (=1111) reste tel quel
mais 16 (=10000) revient à 0 :

-----

Entrer un nombre : 15

Résultat : 15

-----

Entrer un nombre : 16

Résultat : 0
*/