package scanner.ex;

import java.util.Scanner;

public class ScannerEx5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("첫 번째 숫자 입력: ");
        int num1 = input.nextInt();

        System.out.print("두 번째 숫자 입력: ");
        int num2 = input.nextInt();

        if (num1 > num2) {
            int temp;
            temp = num1;
            num1 = num2;
            num2 = temp;
        }

        for (int i = num1; i <= num2; i++) {
            if (i < num2) {
                System.out.print(i + ", ");
            } else {
                System.out.print(i);
            }
            // if (i != num2), i가 num2가 아닌 경우로 해도 마찬가지
        }
    }
}
