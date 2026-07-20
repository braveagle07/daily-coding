import java.util.Scanner;

class vasanth {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);

        int t = read.nextInt();

        for (int i = 0; i < t; i++) {
            int a = read.nextInt();
            int b = read.nextInt();

            int sum = a + b;
            int product = a * b;

            System.out.println(sum + " " + product);
        }

        read.close();
    }
}
