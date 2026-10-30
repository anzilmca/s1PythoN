#include<stdio.h>
int main(){
  
  int arra[10],arrb[10],arrc[20];
  int sizea,sizeb;
  int k=0;
  
  printf("Enter size of arr!:");
  scanf("%d",&sizea);
  
  printf("Enter the size of second array:");
  scanf("%d",&sizeb);
  
  printf("Enter elements of array 1:");
  for(int i=0;i<sizea;i++){
   scanf("%d",&arra[i]);
  }
  
  printf("Enter elements of array 2:");
  for(int i=0;i<sizeb;i++){
   scanf("%d",&arrb[i]);
  }
  
  printf("Merged array");
  for(int i=0;i<sizea;i++){
   arrc[i] = arra[i];
   k++;
  }
  
  for(int i=0;i<sizeb;i++){
   arrc[k] = arrb[i];
   k++;
  }
  
  for(int i=0;i<sizea+sizeb;i++){
   printf("%d ",arrc[i]);
  }
  
  
  
  return 0;
}
