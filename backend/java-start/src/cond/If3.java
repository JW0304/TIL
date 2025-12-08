package cond;

public class If3 {
    public static void main(String[] args) {
        int age = 14;

        // 5번의 조건 검사를 매번 해야 한다
        // 1. 앞의 조건을 만족하면 뒤의 조건을 검사할 필요가 없다 (불필요한 조건 검사)
        // 2. 앞의 나이 조건문은 검사할 필요가 없다 (중복체크)
        if (age <= 7) {
            System.out.println("미취학");
        }
        if (age >= 8 && age <= 13) {
            System.out.println("초등학생");
        }
        if (age >= 14 && age <= 16) {
            System.out.println("중학생");
        }
        if (age >= 17 && age <= 19) {
            System.out.println("고등학생");
        }
        if (age >= 20) {
            System.out.println("성인");
        }
    }
}
