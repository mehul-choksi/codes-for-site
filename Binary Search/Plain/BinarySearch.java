import java.util.Scanner;
import java.util.Arrays;

public class BinarySearch{

	public int a[];
	public int n;
	
	public BinarySearch(){
		n = 8;		
		a = new int[8];
		for(int i = 0; i < n; i++)
			a[i] = i+1;
	}

	public int binary_search(int key){

		int lo = 0, hi = n-1, mid;
		
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

	public static void main(String args[]){
		BinarySearch b = new BinarySearch();
		int key = 6;
		int loc = b.binary_search(key);
		if(loc != -1)
			System.out.println("Found at location: " + loc);	
		else
			System.out.println("Found at location: " + loc);
	}
}

