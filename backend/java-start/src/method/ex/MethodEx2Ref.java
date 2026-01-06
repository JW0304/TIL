package method.ex;

public class MethodEx2Ref {
    public static void main(String[] args) {
        String msg = "Hello World";

//        printMsg(msg, 1);
//        printMsg(msg, 3);
//        printMsg(msg, 5);

        //String 변수 직접 넣어도 됨
        printMsg("hi", 1);
        printMsg("java", 2);
        printMsg("method", 3);
    }

    public static void printMsg(String msg, int n) {
        System.out.println(n + "회 출력");
        for (int i = 0; i < n; i++) {
            System.out.println(msg);
        }
    }
}
