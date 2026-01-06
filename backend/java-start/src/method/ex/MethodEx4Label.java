package method.ex;

import java.util.Scanner;

public class MethodEx4Label {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int balance = 0;

        // 라벨 붙은 곳까지 break
        exitAll:
        while(true) {
            System.out.println("-------------------------------------");
            System.out.println("1. 입금 | 2. 출금 | 3. 잔액 확인 | 4. 종료");
            System.out.println("-------------------------------------");
            System.out.print("번호를 선택해주세요: ");
            int menu = input.nextInt();
            int amount;

            // switch - break / return 으로 실행 - 중단점 / 종료 (break은 switch조건문/반복문 종료, return은 메서드 종료)
            switch (menu) {
                case 1:
                    System.out.print("입금액을 입력하세요: ");
                    amount = input.nextInt();
                    balance = deposit(balance, amount);
                    break;
                case 2:
                    System.out.print("출금액을 입력하세요: ");
                    amount = input.nextInt();
                    balance = withdraw(balance, amount);
                    break;
                case 3:
                    System.out.println("잔액을 확인합니다.");
                    checkBalance(balance);
                    break;
                case 4:
                    System.out.println("프로그램을 종료합니다.");
                    break exitAll;
                // 올바른 번호가 아닌 경우 (기본값)
                default:
                    System.out.println("올바른 숫자를 입력해주세요.");
            }
        }
    }

    public static int deposit(int balance, int amount) {
        balance += amount;
        System.out.println(amount + "원 입금, 잔액은 " + balance + "원입니다.");
        return balance;
    }

    public static int withdraw(int balance, int amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println(amount + "원 출금, 잔액은 " + balance + "원입니다.");
        } else {
            System.out.println("잔액이 부족해 출금할 수 없습니다. 잔액은 " + balance + "원입니다.");
        }
        return balance;
    }

    public static void checkBalance(int balance) {
        System.out.println("현재 잔액은 " + balance + "원입니다.");
    }
}
