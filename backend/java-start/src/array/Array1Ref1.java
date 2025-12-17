package array;

public class Array1Ref1 {
    public static void main(String[] args) {
        int[] students; // 배열 변수 선언
        students = new int[5]; // 배열 생성

        System.out.println(students);

        // 변수 값 대입
        students[0] = 90;
        students[1] = 80;
        students[2] = 70;
        students[3] = 60;
        students[4] = 50;

        System.out.println("학생 5의 점수: "+students[0]);
        System.out.println("학생 1의 점수: "+students[1]);
        System.out.println("학생 2의 점수: "+students[2]);
        System.out.println("학생 3의 점수: "+students[3]);
        System.out.println("학생 4의 점수: "+students[4]);


    }
}
