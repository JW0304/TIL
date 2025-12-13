package scanner;

import java.util.Scanner; // 자바가 제공하는 라이브러리 java.util

public class Scanner1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Scanner를 쓰려면 먼저 Scanner를 생성해야 한다

        System.out.print("문자열을 입력하세요: ");
        String str = scanner.nextLine(); // 엔터(\n) 입력할 때까지의 문자
        System.out.println("입력한 문자열: " + str);

        System.out.print("정수를 입력하세요: ");
        int intValue = scanner.nextInt(); // int로 입력을 가져옴
        System.out.println("입력한 정수: " + intValue);

        System.out.print("실수를 입력하세요: ");
        double doubleValue = scanner.nextDouble(); // double로 입력을 가져옴
        System.out.println("입력한 실수: " + doubleValue);
    }
}
