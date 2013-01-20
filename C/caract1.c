/* 3.5.10 */
#include <stdio.h>

main() {
	int code;
	char caractere;

	printf("Entrer un code ASCII : ");
	scanf("%d", &code);

	printf("Caractère : %c\n\n", code);

	getchar(); /* on enlève le saut de ligne resté dans le buffer*/

	printf("Entrer un caractère : ");
	scanf("%c", &caractere);

	printf("Code ascii : %i\n", caractere);
}

/* Si on ne vide pas le buffer avec getchar() (à la ligne 13, direction Saint-Denis-Université) :

Entrer un code ASCII : 65
Caractère : A

Entrer un caractère : Code ascii : 10

> Le 2e scanf va récupérer le caractère '\n' (saut de ligne) qui est resté dans le buffer
puis affiche son code à ski ...

Programme final :

Entrer un code ASCII : 65
Caractère : A

Entrer un caractère : A
Code ascii : 65
*/