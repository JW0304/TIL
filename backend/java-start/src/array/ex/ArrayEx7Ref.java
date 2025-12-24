package array.ex;

import java.util.Scanner;

public class ArrayEx7Ref {
    public static void main(String[] args) {
        int studentNum = 4;
        int scoreNum = 3;
        int[][] scores = new int[studentNum][scoreNum];
        String[] subjects = {"국어", "영어", "수학"};
        int total;
        double avg;

        Scanner input = new Scanner(System.in);

        for (int i = 0; i < studentNum; i++) {
            System.out.println((i + 1) + "번 학생의 성적을 입력하세요:");
            for (int j = 0; j < scoreNum; j++) {
                System.out.print(subjects[j] + " 점수: ");
                scores[i][j] = input.nextInt();
            }
        }

        for (int i = 0; i < studentNum; i++) {
            total = 0;
            avg = 0;
            for (int j = 0; j < scoreNum; j++) {
                total += scores[i][j];
            }
            avg = (double) total / scoreNum;
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
