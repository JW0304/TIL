package casting;

public class Casting1 {
    public static void main(String[] args) {
        int intValue = 10;
        long longValue;
        double doubleValue;

        // 원래는 이렇게 괄호 안에 타입을 적어줘야 한다
        longValue = (long) intValue; // int -> long 가능
        System.out.println("longValue = " + longValue); // 10

        doubleValue = (double) intValue; // int -> double
        System.out.println("doubleValue = " + doubleValue); // 10.0 (double이라 소수점 표현됨)

        doubleValue = 20000000000L; // long -> double, 100억
        System.out.println("doubleValue2 = " + doubleValue); // 2.0E10
    }
}
