// #include <iostream>
// using namespace std;

// int main()
// {
//     int n, num = 1;
//     cout << "Enter a number ";
//     cin >> n;
//     for (int i = 0; i <n; i++)
//     {
//         for (int k = 0; k <i; k++)
//         {
//             cout << " ";
//         }
//         for (int j = 0; j < n-i; j++)
//         {
//                 cout << i+1;
                
//         }
//          cout << endl;   
//     }

    // int n,num=1;
    // cout<<"Enter a number";
    // cin>>n;
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 1; j < n-i; j++)
    //     {
    //         cout<<" ";
    //     }
    //     for (int k = 1; k < i+2; k++)
    //     {
    //         cout<<k;
            
    //     }
        
    //     for (int w = i; w >0; w--)
    //     {
    //         cout<<w;
            
    //     }
    //     cout<<endl;
    // }
    //     int n,num=1;
    // cout<<"Enter a number";
    // cin>>n;
    // // top
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j<=i; j++)
    //     {
    //         cout<<"*";
    //     }
        
    //     for (int k = 1; k <n-i; k++)
    //     {
    //         cout<<" ";
    //     }
        
    //     for (int k = 1; k <n-i; k++)
    //     {
    //         cout<<" ";
    //     }
    //     for (int j = 0; j<=i; j++)
    //     {
    //         cout<<"*";
    //     }
    //     cout<<endl;
    // }
    // // bottom
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = n-i; j > 0; j--)
    //     {
    //         cout<<"*";
    //     }
    //     for (int k = 0; k < i; k++)
    //     {
    //         cout<<" ";
    //     }
    //     for (int m = 0; m <i; m++)
    //     {
    //         cout<<" ";
    //     }
    //     for (int t = i; t <n; t++)
    //     {
    //         cout<<"*";
    //     }
    //     cout<<endl;
    // }

    // long long int n,num=0;
    // cout<<"Enter a number :"<<endl;
    // cin>>n;
    // while (n!=0)
    // {
    //     num=num*10+n%10;
    //     n/=10;
    // }
    // cout<<"Required reverse number is :"<<num;
//     return 0;
// }
// #include <iostream>
// using namespace std;

// int prod(int arr[],int n,int l){
//     for (int i = 0; i < n; i++)
//     {
//         l*=(arr[i]);
        
//     }
//     return l;
// }
// int main(){
//     int a[]={1,2,3,4,5,3,4,5};
//     int k=sizeof(a)/sizeof(int);
//     int s=1;
//     cout<<prod(a,k,s);

// int arr[]={1,2,3,2,3,3,3,4,4,4,4,4}, n[]={2,3,2,3,3,2,5,4,4,3,3,2,2}, l=sizeof(arr)/sizeof(int),k=sizeof(n)/sizeof(int),count=0;
//     for (int i = 0; i < l; i++)
//     {
//         for (int j = 0; j < k; j++)
//         {
//             if (arr[i]=n[j])
//             {
//                 count+=1;
//             }
//             else{
//                 count+=0;
//             }
//         }
//     }
//     cout<<count;
//     return 0; 
// }

// int recbinary(vector<int> arr,int tar){
//     int st=0,end=arr.size()-1;
//     if (st<=end){
//         int mid=st+(end-st)/2;
//         if (tar>arr[mid])
//         {
//             return recbinary(arr, tar);
//         }
//         else if (tar<arr[mid])
//         {
//             return recbinary(arr, tar);
//         }
//         else
//         {
//             return mid;
//         }
//     }
//     return -1;
// }
//     vector<int> arr1={1,6,4,7,5,0,2};
//     int tar1=2;
//     // cout<<recbinary(arr1,tar1)<<endl;
//     vector<int> arr2={1,6,4,7,5,0,2};
//     int tar2=2;
//     cout<<recbinary(arr2,tar2)<<endl;

