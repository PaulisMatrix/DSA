#include<iostream>
using namespace std;
/*
    find x such that

    x % num[0] = rem[0]
    x % num[1] = rem[1]
    ...................
    x % num[n-1] = rem[n-1]

*/

int findMinx(int num[],int rem[],int size)
{
    int x=1,j;

    while(1)
    {
        for(j=0;j<size;j++)
        {
            if(x % num[j] != rem[j])
                break;
        }

        if(j==size)    
            return x;

        x++;    //keep searching for x if the condition is not met.
    }

}

int main()
{
    int num[] = {5,7,8}; //relatively primes,i.e not having any common factors
    int rem[] = {3,1,6};

    int size = sizeof(num)/sizeof(num[0]);

    cout<<"x is: "<<findMinx(num,rem,size);

    return 0;

}
