package method;

public class MethodCasting1 {
    public static void main(String[] args) {
        double number = 1.5;
        // printNumber(number); // double 인수를 int 매개변수에 전달할 수 없음, 컴파일 오류
        printNumber((int) number); // 명시적 형변환
    }

    // double을 int에 넣을 수 없다 (큰 걸 작은 것에 넣을 수 없다, int < long < double)
    public static void printNumber(int n) {
        System.out.println("숫자: " + n);
    }
}
