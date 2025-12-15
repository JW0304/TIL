package scanner;

import java.util.Scanner;

public class ScannerWhile2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("두 정수 모두 0이면 프로그램 종료");
        while (true) {
            System.out.print("정수 1: ");
            int int1 = scanner.nextInt();
            System.out.print("정수 2: ");
            int int2 = scanner.nextInt();

            if (int1 == 0 && int2 == 0) {
                System.out.println("프로그램 종료");
                break;
            }

            System.out.println("정수 1 + 정수 2 = " + (int1 + int2));
        }
    }
}
