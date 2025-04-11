#include <stdio.h> 
int main (){
    int entrada;
    do{
        scanf("%d",&entrada);
        if(entrada!=42){
            printf("%d\n",entrada);
        } else {break;}
    }while(1);
}