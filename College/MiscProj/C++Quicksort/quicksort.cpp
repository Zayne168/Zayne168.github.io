#include <bits/stdc++.h>
#include <chrono>
using namespace std;
//Zayne Bonner 800756759


int partitionRandom(vector<int>& arr, int low, int last){ 
    int randomIndex = low +  rand() % (last - low + 1);//grab a random pivot < size of the last value of array to be sorted
    swap(arr[randomIndex], arr[last]);
    int pivot = arr[last]; //last item in array = pivot
  
    int i = low-1;//smaller element index

    for (int j = low; j <= last - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]); //less than pivot => move the indexed element to left
        }
    }

    swap(arr[i + 1], arr[last]); //move the pivot to be behind the smaller elements
    return i + 1;
}
int partitionMiddle(vector<int>& arr, int low, int last){
    int randomIndex;
    int midLow = low + (last - low)/4;
    int midHigh = low + 3*(last-low)/4;
    do{
        randomIndex = low + rand() % (last - low +1);
    }while(randomIndex < midLow || randomIndex > midHigh);
    
    swap(arr[randomIndex], arr[last]);
    int pivot = arr[last]; //last item in array = pivot
    int i = low-1;//smaller element index
    for (int j = low; j <= last - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]); //less than pivot => move the indexed element to left
        }
    }

    swap(arr[i + 1], arr[last]); //move the pivot to be behind the smaller elements
    return i + 1;


}


int partition(vector<int>& arr, int low, int last) {
  
    int pivot = arr[last]; //last item in array = pivot
  
    int i = low-1;//smaller element index

    for (int j = low; j <= last - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]); //less than pivot => move the indexed element to left
        }
    }

    swap(arr[i + 1], arr[last]); //move the pivot to be behind the smaller elements
    return i + 1;
}


void quickSortRandom(vector<int>& arr, int low, int last){
    if (low < last) {
      
        int pi = partitionRandom(arr, low, last);

        quickSortRandom(arr, low, pi - 1); //recursively sort left of pivot
        quickSortRandom(arr, pi + 1, last); //recursively sort right of pivot
    }
}
void quickSortMiddle(vector<int>& arr, int low, int last){
    if (low < last) {
      
        int pi = partitionMiddle(arr, low, last);

        quickSortMiddle(arr, low, pi - 1); //recursively sort left of pivot
        quickSortMiddle(arr, pi + 1, last); //recursively sort right of pivot
    }
} 

void quickSort(vector<int>& arr, int low, int last/*,int test*/) {
        /*for (int i = 0; i < test; i++) {
        cout << arr[i] << " ";
        }
        cout << endl;*/
    if (low < last) {
      
        int pi = partition(arr, low, last);//pivot index

        quickSort(arr, low, pi - 1); //recursively sort left of pivot
        quickSort(arr, pi + 1, last); //recursively sort right of pivot
    }
}

int main() {
    const int size = 131073;//131073
    const int min = 1;
    const int max = 1000000;
    srand(time(0));
    random_device rd;
    mt19937 eng(rd());
    uniform_int_distribution<> distr(min, max);

    vector<int> arr(size);
    
    for (int i = 0; i < size; i++) 
        arr[i] = distr(eng);

    int n = arr.size();
    vector<int> arr2=arr;
    vector<int> arr3=arr;
    int z;
for(z=0;z<11;z++){//calls whatever is within 11 times, since the first execution is always an outlier that involves extra initializations.
    uniform_int_distribution<> distr(min, max);

    vector<int> arr(size);
    
        for (int i = 0; i < size; i++)
            arr[i] = distr(eng);
}//put this for-loop around any quicksort call function and timer that you wish to call 10x times  
//      ################################################
//         Array Quicksort Calls:

//Standard Quicksort
    auto start = chrono::high_resolution_clock::now();
        quickSort(arr, 0, n-1);
    
    auto stop = chrono::high_resolution_clock::now();
    chrono::duration<double,milli> elapsed = stop-start;
        cout << elapsed.count()<<" milliseconds - Unsorted Quicksort"<<endl;

    start = chrono::high_resolution_clock::now();
       //quickSort(arr, 0, n-1);
  
    stop = chrono::high_resolution_clock::now();
    elapsed = stop-start;
        cout << elapsed.count()<<" milliseconds - sorted Quicksort"<<endl;
//Middle Quicksort       
    start = chrono::high_resolution_clock::now();
        quickSortMiddle(arr2, 0, n-1);
  
    stop = chrono::high_resolution_clock::now();
    elapsed = stop-start;
        cout << elapsed.count()<<" milliseconds - Unsorted Quicksort with mid-range pivot"<<endl;


    start = chrono::high_resolution_clock::now();
        quickSortMiddle(arr2, 0, n-1);

    stop = chrono::high_resolution_clock::now();
    elapsed = stop-start;
       cout << elapsed.count()<<" milliseconds - sorted Quicksort with mid-range pivot"<<endl;

//Random Quicksort
    start = chrono::high_resolution_clock::now();
        quickSortRandom(arr3, 0, n-1);
    
    stop = chrono::high_resolution_clock::now();
        elapsed = stop-start;

        cout << elapsed.count()<<" milliseconds - Unsorted Quicksort with random  pivot"<<endl;
    start = chrono::high_resolution_clock::now();
        quickSortRandom(arr3, 0, n-1);
    
    stop = chrono::high_resolution_clock::now();
    elapsed = stop-start;    
        cout << elapsed.count()<<" milliseconds - sorted Quicksort with random  pivot"<<endl;



/*
    for(z=0;z<10;z++){
    uniform_int_distribution<> distr(min, max);

    vector<int> arr(size);
    
        for (int i = 0; i < size; i++)
            arr[i] = distr(eng);
           
    }
    cout << "Sorted Array" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << arr2[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << arr3[i] << " ";
    }
    cout << endl;
*/
    return 0;
}