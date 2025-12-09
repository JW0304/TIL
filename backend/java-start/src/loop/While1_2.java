package loop;

public class While1_2 {
    public static void main(String[] args) {
        int count = 0;

        // 참인 경우 코드 블록 내부 실행, 조건식으로 돌아옴
        while (count < 100) {
            count++;
            System.out.println("현재 숫자는: "+count);
        }
    }
}
