package operator;

public class Operator1 {
    public static void main(String[] args) {
        // 변수 초기화
        int a = 5;
        int b = 2;

        // Shift + F10 바로 실행
        int sum = a + b;
        System.out.println("sum = " + sum);
        int diff = a - b;
        System.out.println("diff = " + diff);
        int multi = a * b;
        System.out.println("multi = " + multi);
        int div = a / b; // 자바에서 int끼리 연산하면 결과값도 int, 소수점 날아감
        System.out.println("div = " + div);
        double div2 = a / b; // 결과값 2.0
        System.out.println("div2 = " + div2);
        double div3 = (double) a / b; // 형변환, 결과값 2.5
        System.out.println("div3 = " + div3);
        int mod = a % b; // 나머지 연산자는 실무, 알고리즘 모두 종종 사용된다
        System.out.println("mod = " + mod);

        // int z = 10 / 0; // ArithmeticException: / by zero

    }
}
