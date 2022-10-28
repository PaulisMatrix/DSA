#include <stdio.h>
#include <cstdlib>

int main(){

    int i;
    int n = 10;
    
    int *ptr = (int*) malloc(n*sizeof(int));

    for(i = 0;i<n;i++){
        ptr[i] = i+1;
    }

    for(i=0;i<n;i++){
        printf("%d ",*(ptr+i));

    }

    //extend the array
    int m = n*2;
    int *ptr_new = (int*) realloc(ptr,m*sizeof(int));

    for(i=10;i<m;i++){
        ptr_new[i] = i+1;
    }

    
    for(i=10;i<m;i++){
        printf("%d ",*(ptr_new+i));

    }

    /*
    printf("\n");

    for(i=0;i<m;i++){
        printf("%d ",*(ptr_new+i));
    }
    */
   //free the memory
    int *ptr_new_new = (int*) realloc(ptr_new,0*sizeof(int));

    //segmentation fault
    for(i=0;i<m;i++){
        printf("%d ",*(ptr_new_new+i));

    }

    return 0;
}


