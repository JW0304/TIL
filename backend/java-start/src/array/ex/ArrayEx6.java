package array.ex;

import java.util.Arrays;
import java.util.Scanner;

public class ArrayEx6 {
    public static void main(String[] args) {
        int size;
        int minNum, maxNum;
        int temp; // 값을 교환할 때 temp임

        Scanner input = new Scanner(System.in); // Scanner 타입의 input 변수에 System.in으로 받은 객체 Scanner를 넣음

        System.out.print("입력받을 숫자의 개수: "); // System.out 메서드의 print() 또는 println()
        size = input.nextInt();
        // System.out.println("사이즈" + size);

        // 배열은 size가 들어오고 나서 값을 넣어줘야 함!
        int[] arr = new int[size]; // 정수 배열인 arr에 size를 크기로 하는 정수 배열 객체를 넣음

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
