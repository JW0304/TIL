package array.ex;

import java.util.Scanner;

public class ArrayEx4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("입력받을 숫자의 개수를 입력하세요: ");
        int size = input.nextInt();
        int[] numbers = new int[size];
        int sum = 0;
        double average;

        System.out.println(size + "개의 정수를 입력하세요:");
        for (int i = 0; i < size; i++) {
            numbers[i] = input.nextInt();
            sum += numbers[i];
        }

        average = (double) sum / size; // sum은 int이므로 형변환이 필요함
        System.out.println("sum = " + sum);
        System.out.println("average = " + average);
    }
}
