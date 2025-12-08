package cond.ex;

public class CondEx4 {
    public static void main(String[] args) {
        double rating = 8;

        // 독립적 if문을 쓰면 된다
        if (rating <= 9) {
            System.out.println("'어바웃 타임'을 추천합니다.");
        }
        if (rating <= 8) {
            System.out.println("'토이 스토리'를 추천합니다.");
        }
        if (rating <= 7) {
            System.out.println("'고질라'를 추천합니다.");
        }

        /*
        switch (rating) {
            case 7:
                System.out.println("'고질라'를 추천합니다.");
            case 8:
                System.out.println("'토이 스토리'를 추천합니다.");
            case 9:
                System.out.println("'어바웃 타임'을 추천합니다.");
        }
        */
    }
}
