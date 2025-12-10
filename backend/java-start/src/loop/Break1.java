package loop;

public class Break1 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;

        // while (true)는 무한 반복, break으로 종료 (안 그러면 컴퓨터 끄기 전 / 프로그램 종료 전까지 무한 실행)
        while (true) {
            sum += i;
            if (sum > 100000) {
                System.out.println("sum = " + sum + " i = " + i);
                break;
            }
            i++;
        }
    }
}
