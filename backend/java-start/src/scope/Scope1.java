package scope;

public class Scope1 {
    public static void main(String[] args) {
        int m = 10; // m 생존 시작
        if (true) { // 두 번 클릭하면 코드블럭 범위 지정됨
            int x = 20; // x 생존 시작
            System.out.println("if m = " + m);
            System.out.println("if x = " + x);
        } // x 생존 종료

        // System.out.println("main x = " + x);
        System.out.println("main m = " + m);
    } // m 생존 종료
}
