#include <stdio.h>

int main(){
    char nome[60];
    printf("Como voce se chama? ");
    gets(nome);
    printf("É um prazer te conhecer, %s!\n", nome);
    return 0;
}