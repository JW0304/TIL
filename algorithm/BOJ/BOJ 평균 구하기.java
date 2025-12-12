import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int num = sc.nextInt(); // 점수의 개수 입력
    int[] scores = new int[num]; // 점수 배열 생성

    // 점수들 입력받기
    for (int i = 0; i < num; i++) {
      scores[i] = sc.nextInt();
    }

    // 최댓값 구하기
    int maxScore = scores[0];
    for (int i = 1; i < num; i++) {
      if (scores[i] > maxScore) {
        maxScore = scores[i];
      }
    }

    // 새로운 점수 계산 및 합계
    double sum = 0;
    for (int i = 0; i < num; i++) {
      sum += (double) scores[i] / maxScore * 100;
    }

    // 평균 출력
    System.out.println(sum / num);

    sc.close();
  }
}
