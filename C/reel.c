/* 3.4.9.1
   complier avec : gcc reel.c -lm -o reel
*/
#include <stdio.h>
#include <math.h>

main() {
	float reel, partie_decimale;
	int entier, arrondi;

	printf("Entrer un réel : ");
	scanf("%f", &reel);

	/* on converti notre réel en entier (on vire tout ce qui est après la virgule) */
	entier = reel;
	/* 	comme on a viré ce qu'il y a après la virgule dans entier,
		reel - entier ça laisse tout après la virgule
	*/
	partie_decimale = reel - entier;

	printf("\nRésultat de :\n \
	* partie entière : %d\n \
	* partie décimale : %f\n \
	* arrondi : %f\n",
	entier,
	partie_decimale,
	/* floor arrondi un réel donc floor(5.4) == 5 et floor(5.5) == 5
	   sauf qu'on veut qu'au dessus de X,5 on passe au nombre supérieur
	   donc on ajoute 0,5 : floor(5.4+0.5) == floor(5.9) == 5
	   et floor(5.5+0.5) == floor(6.0) == 6
	*/
	floor(reel + 0.5)
	);
}

/*
Entrer un réel : 5.4

Résultat de :
 	* partie entière : 5
 	* partie décimale : 0.400000
 	* arrondi : 5.000000
*/

/*
Entrer un réel : 5.5

Résultat de :
 	* partie entière : 5
 	* partie décimale : 0.500000
 	* arrondi : 6.000000
*/