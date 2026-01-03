package method;

public class Method2 {
    public static void main(String[] args) {
        printHeader();
        System.out.println("프로그램 동작");
        printFooter();

        //반환값이 없으므로 에러난다
        //String str = printFooter();
    }

    // 반환값 없음(void), 매개변수 없음()
    public static void printHeader() {
        System.out.println("===프로그램 시작===");
        return; // void인 경우에는 return 생략해도 됨 (자바 컴파일러가 자동 삽입) / return - 메서드 종료
    }

    public static void printFooter() {
        System.out.println("===프로그램 종료===");
    }
}


