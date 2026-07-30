// Day 1 - 180 Days of DSA in Java
// Topic: Super easy array + input/output warmup

import java.util.Scanner;

public class Day1_EasyWarmup {

    public static void main(String[] args) {
        // Create a Scanner object to read input from the keyboard
        Scanner sc = new Scanner(System.in);

        // Ask user for the size of the array
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();  // read array size

        // Create an integer array of size n
        int[] arr = new int[n];

        // Read n integers from the user
        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++) {
            // store each input value in the array
            arr[i] = sc.nextInt();
        }

        // Print the elements of the array
        System.out.println("You entered:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }

        // Move to the next line after printing all elements
        System.out.println();

        // Always close the Scanner when done (good practice)
        sc.close();
    }
}
