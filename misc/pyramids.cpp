/*
pattern:
        * 
      * * 
    * * * 
  * * * * 
* * * * *

Code:
for(int i=0;i<n;i++) //handling number of rows
    {
        //print spaces
        for(int k=0;k<(n-i-1);k++)
        {
            cout<<" ";
        }

        for(int j=0;j<=i;j++) //handling number of *
        {
            cout<<"*";
        }

        cout<<endl;

    }

pattern:
        *
       * *
      * * *
     * * * *
    * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
code:

    //uparwala triangle
    int space = n-1;

    //outer loop
    for(int i=0;i<n;i++)
    {
        //print spaces
        for(int j=0;j<space;j++)
            cout<<" ";

        for(int j=0;j<=i;j++)
            cout<<"* ";

        space--;
        cout<<endl;

    }
    //nichewala triangle
    
    space = 0;
    
    //outer loop
    for(int i=n-1;i>=0;i--)
    {
        //print spaces
        for(int j=0;j<=space;j++)
            cout<<" ";

        for(int j=0;j<i;j++)
            cout<<"* ";

        cout<<endl;
        space++;

    }


#include<iostream>
using namespace std;

void display(int n)
{
    int num = 65;

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<=i;j++)
        {
            cout<<char(num)<<" ";
            num+=1;
        }
        cout<<endl;
    }


}   

*/
#include<iostream>
using namespace std;
/*
void display(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<=i;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
*/
void display(int n){

    int space = n-1;

    for(int i=0;i<n;i++){

        for(int j=0;j<space;j++){
            cout<<" ";
        }

        for(int j=0;j<=i;j++){
            cout<<"* ";
        }
        space--;
        cout<<endl;
    }
    space=0;

    for(int i=n-1;i>=0;i--){

        for(int j=0;j<space;j++){
            cout<<" ";
        }

        for(int j=0;j<=i;j++){
            cout<<"* ";
        }

        space++;
        cout<<endl;

    }

}

int main()
{
    int n;
    cout<<"Enter the number of rows";
    cin>>n;
    display(n);
    
}



