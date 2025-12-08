package cond;

public class Switch4 {
    public static void main(String[] args) {
        // 새로운 스위치문, 자바 14 이상이면 쓸 수 있다. 많이 쓰지는 않지만 한 번 쓰면 매력이 있다.
        int grade = 0;
        int coupon = switch (grade) {
            case 1 -> 1000;
            case 2 -> 2000;
            case 3 -> 3000;
            default -> 500;
        };
        System.out.println("발급받은 쿠폰 "+coupon);
    }
}
