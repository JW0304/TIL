package cond;

public class CondOp2 {
    public static void main(String[] args) {
        int age = 20;

        // (age가 18보다 큰가? (조건)) ? 맞으면 : 아니면 ;
        String status = (age >= 18) ? "성인" : "미성년자";
        System.out.println("age = " + age + " status = " + status);
    }
}
