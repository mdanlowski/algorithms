/*
 * Basic implementation of the Simple (Stupid, Linear) Search and Binary Search algorithms
 * along with a runtime comparison
 * 
 * @author Marcin Danlowski
 * 		   https://github.com/mdanlowski/
 * 
 */
public class Search{
	
	static class SearchMethods{
		
		public static int linearSearch(int[] list, int item){
			
			for ( int i=0; i<list.length; i++ ){
				if(list[i] == item){
					return i;
				}
			}
			return -1;
		}
		
		public static int binarySearch(int[] list, int item){
			
			int low = 0;
			int hi = list.length-1;
			
			while ( low <= hi ){
				int pvt = (int) (low+hi)/2;
				if( pvt == item ) return pvt;
				if( pvt > item )  hi = pvt-1;
				else low = pvt+1;
			}
			return -1;
		}
		
	}
	
	public static void main(String[] args){
		// GENERATE DATA
		int[] data = new int[100000000];
		for(int i=0; i<data.length; i++){
			data[i] = i;
		}
		
		int item = (int) Math.round( 100000000 * Math.random() );
		long start = System.currentTimeMillis();
			System.out.println(SearchMethods.linearSearch(data, 100000000-1/*item*/));
		long stop = System.currentTimeMillis() - start;
		System.out.println("LS DONE. Worst case: " + stop + "ms");
		
		start = System.currentTimeMillis();
			System.out.println(SearchMethods.linearSearch(data, item));
		stop = System.currentTimeMillis() - start;
		System.out.println("LS DONE. Random case: " + stop + "ms");
		
		start = System.currentTimeMillis();
			System.out.println(SearchMethods.binarySearch(data, item));
		stop = System.currentTimeMillis() - start;
		System.out.println("BS DONE. Random case: " + stop + "ms");
		
		start = System.currentTimeMillis();
			System.out.println(SearchMethods.binarySearch(data, item));
		stop = System.currentTimeMillis() - start;
		System.out.println("BS DONE. Random case: " + stop + "ms");
	
	}
	
}



