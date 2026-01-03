package method;

public class Method1Ref {
    public static void main(String[] args) {
        // 메서드 호출: 결과값(반환값)으로 치환, 메서드 호출이 끝나면 메모리의 a, b, sum 값도 제거됨 (초기화)
        int sum1 = add(1, 2);
        int sum2 = add(10, 20);
    }

    // 메서드 선언: 반환 타입, 메서드 이름, 파라미터(= 매개변수, 들어가는 값, 메서드 안에서만 사용됨)
    // public은 다른 클래스에서도 사용 가능, static은 객체 생성하지 않고 호출 가능하다는 뜻
    public static int add(int a, int b) {
        // 메서드 본문: 블랙박스, 호출하는 입장에선 메서드 선언만 알 수 있다. (따라서 return문으로 값을 산출해줘야 함)
        int sum = a + b;
        System.out.println(a + "와 " + b + "(을)를 더합니다.");
        System.out.println("결과: " + sum);
        return sum; // 결과값(반환값) 산출, 변수의 타입 안 맞으면 컴파일 오류 남
    }
}
