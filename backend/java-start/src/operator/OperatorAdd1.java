package operator;

public class OperatorAdd1 {
    public static void main(String[] args) {
        int a = 0;

        a = a + 1; // 산술 연산자 -> 대입 연산자이기 때문에 a = 0 + 1, a = 1 이다
        System.out.println("a = " + a);
        a = a + 1; // 2
        System.out.println("a = " + a);

        // 증감 연산자: 값을 하나 증가시키는 연산을 너무 많이 써서 만들어졌다.
        ++a;
        System.out.println("a = " + a);
        
        --a;
        System.out.println("a = " + a);
    }
}
