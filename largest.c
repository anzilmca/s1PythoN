#include<stdio.h>
int main(){
 
 int arr[10];
 int size;

 
 printf("Enter the size of array:");
 scanf("%d",&size);
 
 printf("Enter the elements:");
 for(int i=0;i<size;i++){
  scanf("%d",&arr[i]);
 }
 
 int largest = arr[0];
 
 for(int i=0;i<size;i++){
  if(arr[i]>largest){
    largest = arr[i];
  }
 }
 
  printf("Largest element:%d",largest);
 
}
