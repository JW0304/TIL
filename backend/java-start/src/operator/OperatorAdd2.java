package operator;

public class OperatorAdd2 {
    public static void main(String[] args) {
        int a = 1;
        int b = 0;

        b = ++a; // 증감 연산자 -> 대입 연산자: a = a + 1, b = a
        System.out.println("a = "+ a + ", b = "+ b); // a = 2, b = 2

        a = 1;
        b = 0; // 다시 원래 값으로 돌린다

        b = a++; // 대입 연산자 -> 증감 연산자: b = a, a = a + 1
        System.out.println("a = "+ a + ", b = "+ b); // a = 2, b = 1

        // 증감 연산자: 앞에 있으면 먼저 증감, 뒤에 있으면 마지막에 증감한다
        // ++a 는 a = a + 1 과 같다. 1 증가시키는 것!

        ++a;
        System.out.println("a = " + a);
        a++;
        System.out.println("a = " + a);
        // 단독으로 사용하는 경우에는 전위, 후위 둘 다 결과는 같다 (1 증가)
    }
}
