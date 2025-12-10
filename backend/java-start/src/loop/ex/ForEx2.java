package loop.ex;

public class ForEx2 {
    public static void main(String[] args) {

        // 초기식에 여러개의 변수를 선언할 수 있다 (증감식에서도 여러개의 변수를 증감할 수 있다)
        for (int num = 2, count = 1; count <= 10; count++) {
            System.out.println(num * count);
        }
    }
}
