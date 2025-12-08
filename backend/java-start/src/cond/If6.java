package cond;

public class If6 {
    public static void main(String[] args) {
        int price = 10000;
        int age = 10;
        int discount = 0;

        // 웬만하면 중괄호는 생략하지 말고 쓰는 게 가독성, 유지보수성 차원에서 좋다!

        if (price >= 10000) {
            discount += 1000;
            System.out.println("10000원 이상 구매, 1000원 할인");
        } else if (age <= 10) {
            discount += 1000;
            System.out.println("10살 이하 어린이, 1000원 할인");
        } else {
            System.out.println("할인 없음");
        }
        System.out.println("총 할인 금액: " + discount + "원");
    }
}