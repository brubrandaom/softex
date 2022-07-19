#include <stdio.h>

int main(){
    float n1, n2, media;
    printf("Informe as duas notas: ");
    scanf("%f %f", &n1, &n2);
    media = (n1+n2)/2;
    printf("Sua media na disciplina foi: %0.2f\n", media);
    return 0;
}