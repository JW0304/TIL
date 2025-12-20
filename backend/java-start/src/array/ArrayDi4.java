package array;

public class ArrayDi4 {
    public static void main(String[] args) {
        int[][] arr = new int[4][10];

        // 값을 넣지 않으면 모든 배열의 값은 0으로 초기화되어 있음
        int i = 1;
        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                arr[row][column] = i++; // 후위 연산자는 대입한 이후에 값 증가
            }
        }

        for (int row = 0; row < arr.length; row++) {
            for (int column = 0; column < arr[row].length; column++) {
                System.out.print(arr[row][column] + " ");
            }
            System.out.println();
        }
    }
}
