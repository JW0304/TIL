package scanner.ex;

public class ChangeVarEx {
    public static void main(String[] args) {

        int a = 10;
        int b = 20;
        System.out.println("a = " + a + ", b = " + b);

        int temp = b; // temp에 20
        b = a; // b는 10
        a = temp; // a는 20
        System.out.println("a = " + a + ", b = " + b);
    }
}
