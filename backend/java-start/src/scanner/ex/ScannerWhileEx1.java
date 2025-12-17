package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.print("이름을 입력하세요 (종료는 '종료' 입력): ");
            String name = input.nextLine();

            if (name.equals("종료")) {
                System.out.println("프로그램 종료");
                break;
            }

            System.out.print("나이를 입력하세요 (종료는 '종료' 입력): ");
            int age = input.nextInt(); // 10\n 인데 nextInt는 10만 가져가서 \n이 남고, 2번째 name=""(빈 문자열)으로 입력되어버림
            input.nextLine(); // 오류를 고치기 위한 한 줄 없애기(\n 은 빈 문자열+개행임)

            System.out.println("이름: "+name+", 나이: "+age);
        }

        /*
        *오류문구*
        이름을 입력하세요 (종료는 '종료' 입력): 재원
        나이를 입력하세요 (종료는 '종료' 입력): 20
        이름: 재원, 나이: 20
        이름을 입력하세요 (종료는 '종료' 입력): 나이를 입력하세요 (종료는 '종료' 입력): 안녕
        Exception in thread "main" java.util.InputMismatchException
            at java.base/java.util.Scanner.throwFor(Scanner.java:977)
            at java.base/java.util.Scanner.next(Scanner.java:1632)
            at java.base/java.util.Scanner.nextInt(Scanner.java:2297)
            at java.base/java.util.Scanner.nextInt(Scanner.java:2251)
            at scanner.ex.ScannerWhileEx1.main(ScannerWhileEx1.java:22)

        *또는*
        이름을 입력하세요 (종료는 '종료' 입력): 재원
        나이를 입력하세요 (종료는 '종료' 입력): 20
        이름: 재원, 나이: 20
        이름을 입력하세요 (종료는 '종료' 입력): 나이를 입력하세요 (종료는 '종료' 입력): 10
        이름: , 나이: 10
         */

    }
}
