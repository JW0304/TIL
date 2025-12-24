package array.ex;

import java.util.Scanner;

public class ArrayEx8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("학생 수를 입력하세요: ");
        int studentCount = input.nextInt();

        int scoreCount = 3;
        int total;
        double avg;

        int[][] scores = new int[studentCount][scoreCount];
        String[] subjects = {"국어", "영어", "수학"};

        for (int i = 0; i < studentCount; i++) {
            System.out.println((i + 1) + "번 학생의 성적을 입력하세요:");
            for (int j = 0; j < scoreCount; j++) {
                System.out.print(subjects[j] + " 점수: ");
                scores[i][j] = input.nextInt();
            }
        }

        for (int i = 0; i < studentCount; i++) {
            total = 0;
            avg = 0;
            for (int j = 0; j < scoreCount; j++) {
                total += scores[i][j];
            }
            avg = (double) total / scoreCount;
            System.out.println((i + 1) + "번 학생의 총점: " + total + ", 평균: " + avg);
        }

//        for (int[] student : scores) {
//            total = 0;
//            for (int score : student) {
//                total += score;
//            }
//        }

    }
}
