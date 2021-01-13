#include <bits/stdc++.h>
using namespace std;

int binary_search(vector<int> &a, int key){
	int lo = 0, hi = a.size()-1, mid;	
	
	while(lo <= hi){
		mid = (lo+hi)/2; // When dealing with large ranges to avoid overflow: use mid = lo + (hi-lo)/2;

		if(a[mid] > key)	// Current element > key, Discard right half
			hi = mid-1;
		else if(a[mid] < key)	// Current element < key, Discard left half
			lo = mid+1;
		else	// Element has been found
			return mid;
	}
	return -1;
}

int main(){
	vector<int> a = {1,2,3,4,5,6,7,8};
	int key = 1;	//cin >> key;
	int loc = binary_search(a,key);
	if(loc != -1)
		cout << "Found at: " << loc << "\n";
	else
		cout << "Requested element doesn't exist\n";
}
