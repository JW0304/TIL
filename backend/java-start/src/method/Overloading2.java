package method;

public class Overloading2 {
    public static void main(String[] args) {
        myMethod(1, 2.0);
        myMethod(1.0, 2);
    }

    public static void myMethod(int a, double b) {
        System.out.println("int, double: " + a + ", " + b);
    }

    public static void myMethod(double a, int b) {
        System.out.println("double, int: " + a + ", " + b);
    }
}
