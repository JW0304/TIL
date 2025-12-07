package operator.ex;

public class OperationEx3 {
    public static void main(String[] args) {
        int score = 95; // 79점, 101점 등 경계값으로 검증해보면 된다
        boolean result = (80 <= score) && (score <= 100);

        System.out.println(result);
    }
}
