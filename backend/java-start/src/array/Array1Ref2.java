package array;

public class Array1Ref2 {
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

        // 배열과 for 반복문 (여기선 for문을 쓰는 게 좋음, 배열 사이즈가 정해져 있기 때문)
        for (int i = 0; i < students.length; i++) {
            // 여기서 (i + 1) 의 괄호를 빼면 "학생 " + i + 1의 앞부분에서 문자로 변환이 되기 때문에 학생21 과 같이 이상하게 나온다
            System.out.println("학생 "+ (i + 1) +"의 점수: "+students[i]);
        }
    }
}
