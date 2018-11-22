import java.util.*; 

class Solution { 
	
	
	
	public int convexHull(Point2D points[], int n) 
	{ 
int count=0;
			
		Vector<Point2D> hull = new Vector<Point2D>(); 
	
		int l = 0; 
		for (int i = 1; i < n; i++) 
			if (points[i].x < points[l].x) 
				l = i; 
		int p = l, q; 
		do
		{ 
			count++; 
			q = (p + 1) % n; 
			for (int i = 0; i < n; i++) 
			{ 
			if (((points[i].y - points[p].y) * (points[q].x - points[i].x) - 
				(points[i].x - points[p].x) * (points[q].y - points[i].y))<0) 
				q = i; 
			} 
	
			p = q; 
	
		} while (p != l);
		
		return count;
	} 
	public int solution(Point2D[] A) 	{ 

		int n = A.length; 
		return convexHull(A, n); 
        		
	} 
} 
