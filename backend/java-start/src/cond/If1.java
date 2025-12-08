package cond;

public class If1 {
    public static void main(String[] args) {
        int age = 20; // 사용자의 나이

        if (age >= 18) {
            // true인 경우에만 코드 블럭이 실행된다
            System.out.println("성인입니다.");
        }

        if (age < 18) {
            // false인 경우에는 코드 블럭을 실행하지 않는다
            System.out.println("미성년자입니다.");
        }
    }
}