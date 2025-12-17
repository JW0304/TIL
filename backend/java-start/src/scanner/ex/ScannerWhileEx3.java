package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Scanner 클래스의 input 객체 생성, System.in으로 받아옴

        int sum = 0;
        int count = 0;
        int num;

        System.out.println("숫자를 입력하세요. (-1 입력시 중단):");

        // 반복문 안에는 반복문 관련된 것만
        /*
        while (true) {
            num = input.nextInt();

            if (num == -1) {
                break;
            }

            sum += num;
            count++;
        }
         */

        // 더 축약형으로 가능 (입력받은 숫자가 -1이 아닌 경우 참, 먼저 괄호 안의 (num=input..) 이 부분이 연산된다고 보면 됨)
        while ((num = input.nextInt()) != -1) {
            sum += num;
            count++;
        }

        // 반복문이 끝나면 평균 구하고 출력하고 끝
        double average = (double) sum / count;

        System.out.println("입력한 숫자들의 합계: " + sum);
        System.out.println("입력한 숫자들의 평균: " + average);
    }
}