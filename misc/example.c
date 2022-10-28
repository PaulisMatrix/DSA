#include<stdio.h>

int main()
{
    FILE *fp;
    char ch;
    int noc=0,nob=0,not=0,nol=0;

    fp=fopen("FileOperations.txt","r");

    if (fp==NULL)
    {
        printf("File cannot be opened\n");
        return -1;
    }

    while(1)
    {
        ch = fgetc(fp);
        if (ch==EOF)
            break;
        noc++;
        if (ch==' ')
            nob++;
        if (ch=='\n')
            nol++;
        if (ch=='\t')
            not++;
    }

    printf("\n");
    fclose(fp);
    printf ("Number of characters = %d\n", noc );
    printf("Number of blanks = %d\n", nob );   
    printf("Number of tabs = %d\n", not );
    printf("Number of lines = %d\n", nol );

    return 0;   
}