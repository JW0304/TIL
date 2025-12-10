package loop.ex;

public class NestedEx2 {
    public static void main(String[] args) {
        int rows = 10;

        for (int i = 1; i <= rows; i++) {
            // System.out.println("*" * i); // java에선 이렇게 안 된다 (문자열과 숫자 곱하기)
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println(); // 엔터, 다음 줄로 넘어감 (개행만 됨)
        }
    }
}
