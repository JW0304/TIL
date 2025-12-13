package casting;

public class Casting4 {
    public static void main(String[] args) {
        int div1 = 3 / 2; // int / int -> (int) int; 결과 1
        System.out.println("div1 = " + div1);

        double div2 = 3 / 2; // int / int -> (double) int; 결과 1.0
        System.out.println("div2 = " + div2);

        double div3 = 3.0 / 2; // double / int -> double / double -> (double) double; 결과 1.5
        System.out.println("div3 = " + div3);

        double div4 = (double) 3 / 2; // 명시적 형변환! double / int -> 위와 같음; 결과 1.5
        System.out.println("div4 = " + div4);
        // int끼리 나눗셈할 때 double로 구하고 싶다면 명시적 형변환을 사용하면 된다

        int a = 3;
        int b = 2;
        double result = (double) a / b; // double / int -> 위와 같음; 결과 1.5
        System.out.println("result = " + result);
    }
}