import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] cnt = new int[4];
		int n = Integer.parseInt(sc.nextLine());
		for (int i=0;i<n;i++) {
			String[] arr = sc.nextLine().split(" ");
			String f = arr[0];
			int j = switch(f) {
				case "STRAWBERRY" -> 0;
				case "BANANA" -> 1;
				case "LIME" -> 2;
				case "PLUM" -> 3;
				default -> -1;
			};
			int m = Integer.parseInt(arr[1]);
			cnt[j]+=m;
		}
		System.out.println(Arrays.stream(cnt).anyMatch(i -> i == 5) ? "YES" : "NO");
	}
}