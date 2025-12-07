package variable;

public class Var8 {
    public static void main(String[] args) {
        //정수
        byte b = 127; // -128 - 127
        short s = 32767; // - 32768 - 32767
        int i = 2147483647; // 약 -21억 - 21억 (대략 20억)
        long l = 9223372036854775807L; // 엄청 큰 수, long은 뒤에 대문자 또는 소문자 L 붙여야 함

        long l1 = 214748364700L; // L 안 붙이면 정수 리터럴 기본은 int이므로 integer number too large
        long l2 = 123; // 작은 수도 가능

        // 실수
        float f = 10.0f; // float은 뒤에 f 붙여야 함
        double d = 10.0; // 훨씬 더 큰 실수 범위
    }
}
