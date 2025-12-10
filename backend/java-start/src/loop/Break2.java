package loop;

public class Break2 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;

        for (; ; ) { // for (int i =1; ; )로 적어도 됨, 조건식/증감식이 없으므로 무한반복
            sum += i;
            if (sum > 100000) {
                System.out.println("sum = " + sum + " i = " + i);
                break;
            }
            i++;
        }
    }
}
