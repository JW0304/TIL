package class1;

public class ClassStart2 {
    public static void main(String[] args) {
        /* <배열 복습>
        1.타입 메모리 이름 - 이름 타입 메모리크기
        int[] students;
        students = new int[5];
        2.타입 메모리 이름 - 생성 타입 메모리크기
        int[] students = new int[5];
        3.중괄호 사용
        int[] students = {1, 2, 3}; */

        String[] studentNames = {"학생1", "학생2", "전학생"};
        int[] studentAges = {15, 16, 20};
        int[] studentGrades = {90, 80, 10};

        for (int i = 0; i < studentNames.length; i++) {
            System.out.println("이름: " + studentNames[i] + " 나이: " + studentAges[i] + " 성적: " + studentGrades[i]);
        }

    }
}
