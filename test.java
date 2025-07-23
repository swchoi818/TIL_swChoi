// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;

public class test {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i,j,x = 0,y = 0,a = 0,b = 0;
		int sum = 0;
		int cnt = 0;
		int[][] sdk = new int[9][9];
		Scanner sc = new Scanner(System.in);
		while(true) {
			for(i = 0;i<9;i++) {
				for(j = 0;j<9;j++) {
					sdk[i][j] = sc.nextInt();
				}
			}
			for(i = 0;i<9;i++) {
				for(j = 0;j<9;j++) {
					sum += sdk[i][j];
					if(sdk[i][j]==0) {
						cnt++;
						x = i;
						y = j;
					}
				}
				if(sum!=45 && cnt == 1) {
					sdk[x][y] = 45-sum;	
				}
				sum = 0;
				cnt = 0;
			}
			for(j = 0;j<9;j++) {
				for(i = 0;i<9;i++) {
					sum += sdk[i][j];
					if(sdk[i][j]==0) {
						cnt++;
						x = i;
						y = j;
					}
				}
				if(sum!=45 && cnt == 1) {
					sdk[x][y] = 45-sum;	
				}
				sum = 0;
				cnt = 0;
			}
			for(b = 0;b<9;b+=3) {
				for(a = 0;a<9;a+=3) {
					for(i = 0;i<3;i++) {
						for(j = 0;j<3;j++) {
							sum+=sdk[i+a][j+b];
							if(sdk[i+a][j+b]==0) {
								cnt++;
								x = i+a;
								y = j+b;
							}
						}
						
						
					}
					if(sum!=45 && cnt == 1) {
							sdk[x][y] = 45-sum;	
						}
						sum = 0;
						cnt = 0;
					
				}
				
			}
			for(i = 0;i<9;i++) {
				for(j = 0;j<9;j++) {
					if(sdk[i][j]==0) {
						cnt++;
					}
				}
			}
			if(cnt == 0) {
				for(i = 0;i<9;i++) {
					for(j = 0;j<9;j++) {
						System.out.print(sdk[i][j]+" ");
					}
					System.out.print("\n");
				}
			} else {
				cnt=0;
			}
		}
		
		
		
	}

}