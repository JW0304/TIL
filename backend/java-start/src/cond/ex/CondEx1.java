package cond.ex;

public class CondEx1 {
    public static void main(String[] args) {
        int score = 95;
        String grade;

        // 복붙을 잘 쓰자
        if (score >= 90) {
            grade = "A";
        } else if (score >= 80) {
            grade = "B";
        } else if (score >= 70) {
            grade = "C";
        } else if (score >= 60) {
            grade = "D";
        } else {
            grade = "F";
        }
        System.out.println("학점은 "+grade+"입니다.");
    }
}
