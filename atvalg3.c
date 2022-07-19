#include <stdio.h>

int main(){
    char nome[60];
    float sal;
    printf("Informe seu nome: ");
    gets(nome);
    printf("Informe seu salario: ");
    scanf("%f", &sal);
    printf("Nome do funcionário: %s\nSalario: %0.2f\n", nome, sal);

    return 0;
}