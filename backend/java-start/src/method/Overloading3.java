package method;

public class Overloading3 {
    public static void main(String[] args) {
        System.out.println(add(1, 2));
        System.out.println(add(1.2, 3.4));
    }

    // 이거 없어도 실행됨 (add(1,2)의 반환값이 int -> double로 바뀌긴 함)
//    public static int add(int a, int b) {
//        return a + b;
//    }

    public static double add(double a, double b) {
        return a + b;
    }
}
