package array.ex;

import java.util.Scanner;

public class ArrayEx9 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int menu = 0;
        // 배열은 정해진 개수가 있어야 함!! 얼마나 들어올지 모르는 경우 ArrayList를 써야 함
        String[] productNames = new String[10];
        int[] productPrices = new int[10];
        int productCount = 0;

        // <조건문>
        // if-else if 또는 switch (조건) {case N: break & default}
        while (menu != 3) {
            System.out.println("1. 상품 등록 | 2. 상품 목록 | 3. 종료");
            System.out.print("메뉴를 선택하세요: ");
            menu = input.nextInt();
            input.nextLine();
            switch (menu) {
                case 1:
                    if (productCount < 10) {
                        System.out.print("상품 이름을 입력하세요: ");
                        String productName = input.nextLine();
                        System.out.print("상품 가격을 입력하세요: ");
                        int productPrice = input.nextInt();
                        productCount += 1;
                    }
                    else {
                        menu = 3;//종료
                    }
                    break;
                case 2:
                    for (int i = 0; i <= 10; i++) {
                        if (productNames[i] != "") {
                            System.out.println(productNames + "" + productPrices);
                        }
                    }
                    // 배열 초기화
                    productNames = new String[10];
                    productPrices = new int[10];
                    break;
                case 3:
                    System.out.println("프로그램을 종료합니다.");
                    break;
                default:
                    System.out.println("숫자를 다시 입력해주세요.");
            }
        }
    }
}
