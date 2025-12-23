package array.ex;

import java.util.Arrays;
import java.util.Scanner;

public class ArrayEx6 {
    public static void main(String[] args) {
        int size;
        int minNum, maxNum;

        Scanner input = new Scanner(System.in);
        System.out.print("입력받을 숫자의 개수: ");
        size = input.nextInt();

        int[] arr = new int[size];
        System.out.println(size + "개의 정수를 입력: ");
        for (int i = 0; i < size; i++) {
            arr[i] = input.nextInt();
        }

        // 배열 중 최솟값, 최대값을 하나하나 비교하며 찾기
        minNum = maxNum = arr[0];
        for (int i = 0; i < size; i++) {
            if (minNum > arr[i]) {
                minNum = arr[i];
            }
            if (maxNum < arr[i]) {
                maxNum = arr[i];
            }
        }

        System.out.println("최소값: " + minNum);
        System.out.println("최대값: " + maxNum);
    }
}
