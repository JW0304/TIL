package operator;

public class Logical2 {
    public static void main(String[] args) {
        int a = 15;
        // a는 10보다 크고 20보다 작다 (예: 청소년의 나이)
        boolean result = a > 10 && a < 20; // (a > 10) && (a < 20) 비교 연산 -> 논리 연산 (상식적으로)
        boolean result2 = 10 < a && a < 20; // 이렇게 써도 된다 (가독성은 더 좋다)
        System.out.println("result = " + result);

    }
}
