// Day 2 - 180 Days of DSA in Java
// Arrays: sum of elements and count of even numbers

import java.util.Scanner;

public class Day2_ArraySumAndEvenCount {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("Array elements:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        int sum = 0;
        int evenCount = 0;

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            if (arr[i] % 2 == 0) {
                evenCount++;
            }
        }

        System.out.println("Sum of elements = " + sum);
        System.out.println("Count of even elements = " + evenCount);

        sc.close();
    }
}
