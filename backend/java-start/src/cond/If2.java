package cond;

public class If2 {
    public static void main(String[] args) {
        int age = 20;

        // 조건을 만족하는 경우
        if (age >= 18) {
            System.out.println("성인입니다");
        }

        // 만족하는 조건이 없는 경우
        else {
            System.out.println("미성년자입니다");
        }
    }
}
