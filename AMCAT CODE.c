/* You are given a list of integers of size N. Write an algorithm to sort the first K elements (from list[0] to list[K-1]) 
of the list in ascending order and the remaining (list[K] to list[N-1] elements in descending order.*/

#include<stdio.h>
#include<stdlib.h>
void swap1(int *a, int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
int partition1(int arr[], int low, int high)
{
    int pivot= arr[high];
    int i = (low-1);
    for(int j=low; j<high; j++)
    {
        if(arr[j]< pivot)
        {
            i++;
            swap1(&arr[i], &arr[j]);
        }
    }
    swap1(&arr[i+1], &arr[high]);
    return(i+1);
} 

int partition2(int arr[], int low, int high)
{
    int pivot= arr[high];
    int i = (low-1);
    for(int j=low; j<high; j++)
    {
        if(arr[j]> pivot)
        {
            i++;
            swap1(&arr[i], &arr[j]);
        }
    }
    swap1(&arr[i+1], &arr[high]);
    return(i+1);
}
void quicksort1(int arr[], int low, int high)
{
    if(low<high)    
    {
        int pi = partition1(arr,low,high);
        quicksort1(arr,low,pi-1);
        quicksort1(arr,pi+1, high);
    }
}

void quicksort2(int arr[], int low, int high)
{
    if(low<high)
    {
        int pi = partition2(arr,low,high);
        quicksort2(arr,low,pi-1);
        quicksort2(arr,pi+1, high);
    }
}
void printarray(int arr[], int num)
{
    for(int i=0; i<num;i++)
    {
        printf("%d", arr[i]);
    }
    printf("\n");
}
int main()
{
    int arr[20], inputList_size, num;
    printf("Enter the number of elements of the list:");
    scanf("%d", &inputList_size);

    for(int i=0; i<inputList_size; i++)
    {
        printf("Enter element %d:", i);
        scanf("%d", &arr[i]);
    }

    printf("Enter number of elemets to be sorted in ascending order:");
    scanf("%d", &num);

    int n= inputList_size - num;
    printarray(arr,inputList_size);

    quicksort1(arr,0,num-1);
    printf("Ascending Order Sorted Half:\n");
    printarray(arr,num);
    
    quicksort2(arr,num,inputList_size-1);
    printf("Descending Order Sorted Half:\n");
    for(int i=num; i<inputList_size; i++)
        printf("%d ", arr[i]);
    return 0;
}