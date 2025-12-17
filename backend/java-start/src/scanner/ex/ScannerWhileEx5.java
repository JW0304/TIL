package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String productName;
        int productPrice;
        int productQuantity;
        int totalPrice = 0;

        while (true) {
            System.out.println("1번을 입력하면 상품 입력, 2번은 결제, 3번은 프로그램 종료");
            int option = input.nextInt();
            input.nextLine();

            // switch문은 case마다 break이 필요함
            switch (option) {
                case 1:
                    System.out.print("상품명 입력: ");
                    productName = input.nextLine();

                    System.out.print("상품 가격 입력: ");
                    productPrice = input.nextInt();

                    System.out.print("구매 수량 입력: ");
                    productQuantity = input.nextInt();

                    int tempPrice = productPrice * productQuantity;
                    System.out.println("상품명: " + productName + ", 상품 가격: " + productPrice + ", 구매 수량: "
                            + productQuantity + ", 합계: " + tempPrice);

                    totalPrice += tempPrice;
                    break;

                case 2:
                    System.out.println("총 구매 비용: " + totalPrice);
                    totalPrice = 0;
                    break;

                case 3:
                    System.out.println("프로그램 종료");
                    return; // return 있어서 break 필요없음

                default:
                    System.out.println("숫자를 다시 입력해주세요.");

            }
        }
    }
}
