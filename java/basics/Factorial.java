import java.util.Scanner;

public class Factorial {
    // 20! is the largest factorial that fits in a long; 13! already overflows int.
    private static final int MAX_N = 20;

    static long factorial(int n) {
        long fact = 1;
        for (int i = 2; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        if (n < 0 || n > MAX_N) {
            System.out.println("Enter a number between 0 and " + MAX_N);
            return;
        }
        System.out.println("Factorial: " + factorial(n));
    }
}
