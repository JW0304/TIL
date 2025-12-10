package loop;

public class Continue1 {
    public static void main(String[] args) {
        int i = 1;
        
        while (i <= 5) {
            if (i == 3) { // false일 때는 실행되지 않음(1,2,4,5)
                i ++; // 더해주지 않으면 3에서 멈춤
                continue; // 아래의 코드 블럭을 무시하고 조건문으로 돌아감
            }
            System.out.println("i = " + i);
            i ++;
        }
    }
}
