import static java.lang.Math.*;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[][] arr = new int[3][3];
	static int[][] num = new int[3][3];
	static boolean[] check = new boolean[10];
	public static int bt(int now, int sum) {
		if (now==9) {
			for (int i=0;i<3;i++) {
				int k=0;
				if (Arrays.stream(num[i]).sum() != 15) return 0x7fffffff;
				for (int j=0;j<3;j++) k+=num[j][i];
				if (k != 15) return 0x7fffffff;
			}
			int k=0;
			for (int i=0;i<3;i++) k+=num[i][i];
			if (k != 15) return 0x7fffffff;
			k=0;
			for (int i=0;i<3;i++) k+=num[i][2-i];
			if (k != 15) return 0x7fffffff;
			return sum;
		}
		int x=now/3, y=now%3;
		int ans=0x7fffffff;
		for (int i=1;i<=9;i++) {
			if (check[i]) continue;
			check[i]=true;
			num[x][y]=i;
			ans = min(ans, bt(now+1, sum+abs(num[x][y]-arr[x][y])));
			num[x][y]=0;
			check[i]=false;
		}
		return ans;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int i=0;i<3;i++) {
			arr[i] = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		}
		System.out.println(bt(0, 0));
	}
}