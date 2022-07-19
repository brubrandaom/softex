#include <stdio.h>

int main(){
    float num, dobro, ter;
    printf("Informe um numero: ");
    scanf("%f", &num);
    dobro = num*2;
    ter = num/3.0;
    printf("Dobro: %0.2f\nTerca parte: %0.2f\n", dobro, ter);
    return 0;
}