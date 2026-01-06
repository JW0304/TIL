package method;

public class Overloading1 {
    public static void main(String[] args) {
        System.out.println(add(1, 2));
        System.out.println(add(1, 2, 3));
    }

    public static int add(int a, int b) {
        System.out.print("두 정수의 합: ");
        return a + b;
    }

    public static int add(int a, int b, int c) {
        System.out.print("세 정수의 합: ");
        return a + b + c;
    }
}
