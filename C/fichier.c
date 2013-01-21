#include <stdio.h>

main(){
	char nom_fichier[100], nom[100], prenom[100];
	int age;

	FILE *fichier;

	printf("Nom du fichier : ");
	scanf("%s", nom_fichier);

	fichier = fopen(nom_fichier, "a"); /* Ouverture en ajout ("a" comme "add") */
	
	/* On vérifie que l'ouverture n'a pas posé de problème.
	   NULL est une valeur spéciale de C 
	*/
	if(fichier == NULL){
		printf("Erreur concernant le fichier\n");
	}
	else{
		printf("\nNom, prénom, âge ? \n");
		scanf("%s %s %d", nom, prenom, &age);

		/* On écrit dans le fichier */
		fprintf(fichier, "%s %s %d\n", nom, prenom, age);
	}

	fclose(fichier); /* on ferme le fichier */
}

/*
Nom du fichier : /tmp/test.txt

Nom, prénom, âge ? 
LeJeannot
Jean
44

-----
Dans la console :

$ cat /tmp/test.txt
LeJeannot Jean 44

*/