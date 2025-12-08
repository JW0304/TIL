package cond;

public class Switch3 {
    public static void main(String[] args) {
        int grade = 2;
        int coupon;

        // switch문은 항상 break와 함께 쓰고, 안 쓰는 경우는 많지 않다
        switch (grade) {
            case 1:
                coupon = 1000;
                break;
            case 2: // 2에서 break이 없으므로 3으로 넘어감
            case 3:
                coupon = 3000;
                break;
            default:
                coupon = 500;
        }
        System.out.println("발급받은 쿠폰 " + coupon);
    }
}
