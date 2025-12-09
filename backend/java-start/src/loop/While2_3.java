package loop;

public class While2_3 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 50;
        int endNum = 100;

        // i부터 endNum까지의 수를 넣어서 코드 반복
        while (i <= endNum) {
            sum += i;
            System.out.println("i=" + i + ",sum=" + sum);
            i++;
        }
    }
}
