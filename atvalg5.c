#include <stdio.h>

int main(){
    float sal, sal2;
    printf("Informe seu salario atual: ");
    scanf("%f", &sal);
    sal2 = sal+(sal*0.15);
    printf("Seu salario novo é de: R$%0.2f\n", sal2);

    return 0;
}