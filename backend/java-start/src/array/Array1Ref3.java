package array;

public class Array1Ref3 {
    public static void main(String[] args) {
        //int[] students = new int[]{90, 80, 70, 60, 50}; // 배열 선언과 생성, 초기화
        int[] students = {90, 80, 70, 60, 50}; // 가장 간단한 버전, 이젠 여기만 수정하면 됨

        for (int i = 0; i < students.length; i++) {
            System.out.println("학생 "+ (i + 1) +"의 점수: " + students[i]);
        }
    }
}
