package operator;

public class Comp2 {
    public static void main(String[] args) {
        String str1 = "문자열1";
        String str2 = "문자열2";

        boolean result1 = "hello".equals("hello"); // 문자열 리터럴 비교
        boolean result2 = str1.equals("문자열1"); // 문자열 변수, 문자열 리터럴 비교
        boolean result3 = str1.equals(str2);

        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);

        System.out.println("hello" == "hello"); // true가 나오는데, true가 안 나올 때도 있다

        // Ctrl + Shift + Enter 누르면 Code Completion, 자동으로 코드를 마쳐준다 (괄호 닫고 세미콜론)
    }
}
