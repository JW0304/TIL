package method;

public class MethodValue0 {
    public static void main(String[] args) {
        int num1 = 5;
        int num2 = num1; // num1이라는 변수가 복사되는 게 아니라, 5라는 값이 복사되어 대입되는 것이다.
        num2 = 10;

        System.out.println("num1 = " + num1);
        System.out.println("num2 = " + num2);
    }
}
