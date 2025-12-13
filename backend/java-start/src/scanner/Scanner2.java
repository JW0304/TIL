package scanner;

import java.util.Scanner;

public class Scanner2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫번째 숫자: ");
        int num1 = scanner.nextInt();

        System.out.print("두번째 숫자: ");
        int num2 = scanner.nextInt();

        // int sum = num1 + num2;
        System.out.println("두 숫자의 합: " + (num1 + num2));
    }
}
