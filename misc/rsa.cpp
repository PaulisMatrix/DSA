#include<iostream>
#include<math.h>
#include<cstring>
#include<string>

using namespace std;
 
int gcd(int a, int b) {
   int t;
   while(1) {
      t= a%b;
      if(t==0)
      return b;
      a = b;
      b = t;
   }
}

double mod(double value, double exponent, double base)
{
	int i=0;
	double result=1;
	for(i=0; i<exponent; i++)
	{
		result *= value;
		result = fmod(result,base);
	}
	return result;
}

int main() {

   double p = 17;
   double q = 11;
   double n=p*q;
   double track;
   double phi= (p-1)*(q-1);

   double e=2;
   while(e<phi) {
      track = gcd(e,phi);
      if(track==1)
         break;
      else
         e++;
   }



   double d;
   int i=1;
   while(d!=floor(d))
   {
      //cout<<d<<"\n";
      d=((phi*i)+1)/e;
      i++;
   }

   //input the message
   /*
   string inputmsg;
   cout<<"Enter the message";
   getline(cin,inputmsg);
   */
   char inputmsg[] = {"RushikeshYadwade"};
   int size = sizeof(inputmsg)/sizeof(inputmsg[0]);

   double encryptedmsg[size];
   char decryptedmsg[size];

   //encrypt the message
   for(int i=0;i<size;i++)
   {
      encryptedmsg[i] = mod(inputmsg[i],e,n);
   }


   //int size = sizeof(encryptedmsg)/sizeof(encryptedmsg[0]);

   //decrypt the message
   for(int j=0;j<size;j++)
   {
      decryptedmsg[j] = mod(encryptedmsg[j],d,n);
   }


   cout<<"Your initial Message";
   for(int i=0;i<size;i++)
   {
      cout<<inputmsg[i];
   }

   cout<<endl;
   cout<<"Encrypted message is:";
   for(int i=0;i<size;i++)
   {
      cout<<encryptedmsg[i];
   }
   cout<<endl;
    
   cout<<"Decrypted message is:";
   for(int j=0;j<size;j++)
   {
      cout<<decryptedmsg[j];
   }

   cout<<"\n"<<"p = "<<p;
   cout<<"\n"<<"q = "<<q;
   cout<<"\n"<<"n = pq = "<<n;
   cout<<"\n"<<"phi = "<<phi;
   cout<<"\n"<<"e = "<<e;
   cout<<"\n"<<"d = "<<d;
   cout<<"\n"<<"PUBLIC KEY ="<<"("<<e<<","<<n<<")";
   cout<<"\n"<<"PRIVATE KEY ="<<"("<<d<<","<<n<<")"<<endl;
   return 0;
}

