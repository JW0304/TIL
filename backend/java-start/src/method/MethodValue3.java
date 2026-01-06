package method;

public class MethodValue3 {
    public static void main(String[] args) {
        int num1 = 5;
        System.out.println("1. changeNumber 호출 전, num1 = " + num1);
        //return한 값을 다시 대입해주면 됨
        num1 = changeNumber(num1);
        System.out.println("2. changeNumber 호출 후, num1 = " + num1);
    }

    // 매개변수에 원래의 변수값을 복사해서 전달
    public static int changeNumber(int num2) {
        num2 = num2 * 2;
        return num2;
    }
}
