package array.ex;

import java.util.Scanner;

public class ArrayEx9 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // 배열은 정해진 개수가 있어야 함!! 얼마나 들어올지 모르는 경우 ArrayList를 써야 함
        int maxProducts = 10;
        int menu = 0;

        String[] productNames = new String[maxProducts];
        int[] productPrices = new int[maxProducts];
        int productCount = 0;

        // <조건문>
        // if, else if, else 또는 switch (조건) {case N: break & default}
        while (true) {
            System.out.println("1. 상품 등록 | 2. 상품 목록 | 3. 종료");
            System.out.print("메뉴를 선택하세요: ");
            menu = input.nextInt();
            input.nextLine();

            switch (menu) {
                case 1:
                    // 오류인지 먼저 if문으로 검증하는 게 더 깔끔함
                    if (productCount == maxProducts) {
                        System.out.println("더 이상 상품을 등록할 수 없습니다.");
                        continue;
                    }
                    System.out.print("상품 이름을 입력하세요: ");
                    productNames[productCount] = input.nextLine();
                    System.out.print("상품 가격을 입력하세요: ");
                    productPrices[productCount] = input.nextInt();
                    // input.nextLine();
                    productCount++;
                    break;

                case 2:
                    if (productCount == 0) {
                        System.out.println("등록된 상품이 없습니다");
                        continue; // 여기서 조건문 끊기(다시 while문)
                    }
                    for (int i = 0; i < productCount; i++) {
                        System.out.println(productNames[i] + ": " + productPrices[i] + "원");
                    }

                    // 배열 초기화
                    productNames = new String[maxProducts];
                    productPrices = new int[maxProducts];
                    productCount = 0; // 카운트도 초기화해야 함!!
                    break;

                case 3:
                    System.out.println("프로그램을 종료합니다.");
                    System.exit(0);

                default:
                    System.out.println("숫자를 다시 입력해주세요.");
            }
        }
    }
}
