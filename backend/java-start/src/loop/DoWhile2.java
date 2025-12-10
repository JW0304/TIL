package loop;

public class DoWhile2 {
    public static void main(String[] args) {
        int i = 0;

        // do while문은 최초 한 번은 무조건 실행, 이후에는 while 조건문 따라 실행
        do {
            System.out.println("현재 숫자: "+i);
            i++;
        } while (i < 3);
    }
}
