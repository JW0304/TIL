package method;

public class MethodValue1 {
    public static void main(String[] args) {
        int num1 = 5;
        System.out.println("1. changeNumber 호출 전, num1 = " + num1);
        changeNumber(num1);
        System.out.println("4. changeNumber 호출 후, num1 = " + num1);
    }

    // 매개변수에도 값을 복사해서 전달한다 (num2 = num1 과 같이 복사해서 전달함)
    public static void changeNumber(int num2) {
        System.out.println("2. changeNumber 변경 전, num2 = " + num2);
        num2 = num2 * 2;
        System.out.println("3. changeNumber 변경 후, num2 = " + num2);

    }
}
