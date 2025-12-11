package scope;

public class Scope2 {
    public static void main(String[] args) {
        int m = 10;
        for (int i = 0; i < 2; i++) {
            System.out.println("for m = " + m); // 블록 외부의 변수는 for문에서 사용 가능
            System.out.println("for i = "  + i);
        } // for문의 i는 생존 종료

        // System.out.println("main i = "  + i);
        System.out.println("main m = " + m);
    }
}
