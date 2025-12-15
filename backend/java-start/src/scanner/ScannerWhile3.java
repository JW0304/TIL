package scanner;

import java.util.Scanner;

public class ScannerWhile3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("입력한 정수를 모두 더합니다. 0을 입력하면 프로그램이 종료됩니다.");
        int sum = 0;

        while (true) {
            System.out.print("정수 입력: ");
            int num = scanner.nextInt();

            if (num == 0) {
                System.out.println("정수의 합: " + sum);
                System.out.println("프로그램 종료");
                break;
            }
            sum += num;
        }
        // 프로그램 종료는 while문에서 나갔을 때 작성해도 됨
    }
}
