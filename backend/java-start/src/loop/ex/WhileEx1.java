package loop.ex;

public class WhileEx1 {
    public static void main(String[] args) {
        int count = 1;

        while (count <= 10) {
            System.out.println(count); // 여기서 후위 증감연산자를 써도 된다 (count++)
            count++;
        }
    }
}
