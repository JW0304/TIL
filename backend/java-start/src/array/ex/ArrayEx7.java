package array.ex;

import java.util.Scanner;

public class ArrayEx7 {
    public static void main(String[] args) {
        int studentNum = 4;
        int scoreNum = 3;
        int[][] students = new int[studentNum][scoreNum];
        int total;
        double avg;

        Scanner input = new Scanner(System.in);

        for (int i = 0; i < studentNum; i++) {
            System.out.println((i + 1) + "번 학생의 성적을 입력하세요:");
            System.out.print("국어 점수: ");
            students[i][0] = input.nextInt();
            System.out.print("영어 점수: ");
            students[i][1] = input.nextInt();
            System.out.print("수학 점수: ");
            students[i][2] = input.nextInt();

//            for (int j = 0; j < scoreNum; i++) {
//                students[i][j] = input.nextInt();
//            }
        }

        for (int i = 0; i < studentNum; i++) {
            total = 0;
            avg = 0;
            for (int j = 0; j < scoreNum; j++) {
                total += students[i][j];
            }
            avg = (double) total / scoreNum;
            System.out.println((i + 1) + "번 학생의 총점: " + total + ", 평균: " + avg);
        }

//        for (int[] student : students) {
//            total = 0;
//            for (int score : student) {
//                total += score;
//            }
//        }

    }
}
