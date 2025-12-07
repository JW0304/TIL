package operator;

public class Operator2 {
    public static void main(String[] args) {
        String result1 = "hello " + "world";
        System.out.println(result1);
        String s1 = "string1";
        String s2 = "string2";
        String result2 = s1 + " " + s2;
        System.out.println(result2);
        String result3 = "출력: " + 10; // 숫자가 문자로 변환
        System.out.println(result3);
        int num = 20;
        String str = "출력: ";
        String result4 = str + num;
        System.out.println(result4);
        // 자바는 String 타입에 다른 타입을 더하면 다 문자열이 된다
    }
}
