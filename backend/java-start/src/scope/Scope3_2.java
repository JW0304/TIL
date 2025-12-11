package scope;

public class Scope3_2 {
    public static void main(String[] args) {
        int m = 10;
        if (m > 0) {
            int temp = m * 2; // 범위를 한정함으로서 효율적 메모리 사용 + 코드 복잡성 감소
            System.out.println("temp = " + temp);
        }
        // System.out.println(temp); 접근 불가
        System.out.println("m = " + m);
    }
}
