package loop;

public class Break3 {
    public static void main(String[] args) {
        int sum = 0;

        for (int i = 1; ; i++) {
            sum += i;
            // 중단조건(조건식)은 for문에서 생략하고 if문으로 써도 됨
            if (sum > 100000) {
                System.out.println("sum = " + sum + " i = " + i);
                break;
            }
        }
    }
}
