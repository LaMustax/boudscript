/* 3.4.9.2 */
#include <stdio.h>
/* En C, on déclare tout ce qu'on peut en tant que constante afin de pouvoir
   modifier la valeur plus tard si nécessaire.
*/
#define PI 3.1415926535

main() {
	float rayon, surface, volume;

	printf("Entrer le rayon de la sphère : ");
	scanf("%f", &rayon);

	/* on effectue les calculs */
	surface = 4 * PI * rayon * rayon;
	volume = (rayon * surface) / 3;

	printf("\nSurface : %f\nVolume : %f\n", surface, volume);
}

/*
Entrer le rayon de la sphère : 2.2

Surface : 60.821236
Volume : 44.602238
*/