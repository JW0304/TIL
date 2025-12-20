package array;

public class EnhancedFor1 {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};

        // iter 단축키를 치면 자동으로 생성됨!!

        // 일반 for문, 인덱스 변수 i를 선언하고 조건문, 증가식이 필요함
        for (int i = 0; i < numbers.length; i++) {
            int number = numbers[i];
            System.out.print(number + " ");
        }
        System.out.println(); // 개행

        // 향상된 for문, for-each문
        for (int number : numbers) {
            System.out.print(number + " ");
        }
        System.out.println();

        // for-each문을 사용할 수 없는 경우, index 값이 직접 필요할 때
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("number" + i + "번의 결과는 " + numbers[i]);
        }
    }
}
