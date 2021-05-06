#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){
    int t, n, k;
    cin>> t >> n >> k;
    int a[n];
    int b[n];
    int growth=0;
    int parcial=0;
    int parcial2=0;
    int p1=0, p2=0, p3=0;
    int a1=0, a2=0;


    if(t==1){
        for (int i=0; i<n; i++){
            cin >> a[i];
        }
        for (int i=0; i<n; i++){
            cin >> b[i];
        }

        for (int i=0; i<n; i++){
            growth= k*b[i];
            if(i!=n-1){cout << a[i]+growth << " ";}
            else if (i==n-1){cout << a[i]+growth <<endl;}
        }

    }
    else if (t==2){
        for (int i=0; i<n; i++){
            cin >> a[i];
        }

        a1= 0;
        a2= k-1;
        for(int x=0; x<3; x++){
                parcial=0;
                parcial2=0;
        for(int i=0; i<k; i++){
            parcial2+= a[i];

        }
        parcial=parcial2;
        //cout<< "First Cout  " << parcial << endl;
        for (int i=1; i<n-k-1; i++){
            parcial2= parcial2+ a[i+k-1]- a[i-1];
            if(parcial<parcial2){
                parcial= max(parcial, parcial2);
                a1= i;
                a2= i+k-1;
            }

        }
        //cout<< "Second Cout  " << parcial << endl;
        for(int i=a1; i<=a2; i++){
            a[i]=0;

        }
        if(x==0){
            p1=parcial;
        }
        else if(x==1){
            p2=parcial;
        }
        else if(x==2){
            p3=parcial;
        }
        //cout << parcial << endl;
        }
        //cout<< p1<< " " << p2 << " " << p3;
        cout<< p1+p2+p3 << endl;
    }

    return 0;
}