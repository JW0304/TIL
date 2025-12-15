package scanner;

import java.util.Scanner;

public class ScannerWhile1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("문자열을 입력하세요(종료는 exit 입력): ");
            String str = scanner.nextLine();
            if (str.equals("exit")) { // String 비교는 == 가 아니라 .equals
                System.out.println("프로그램을 종료합니다.");
                break;
            }

            System.out.println("입력하신 문자열은 "+str+"입니다.");
        }
    }
}
