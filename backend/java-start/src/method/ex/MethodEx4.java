package method.ex;

import java.util.Scanner;

public class MethodEx4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int balance = 0;

        // while(true) - break으로 실행, 종료
        while(true) {
            System.out.println("-------------------------------------");
            System.out.println("1. 입금 | 2. 출금 | 3. 잔액 확인 | 4. 종료");
            System.out.println("-------------------------------------");
            System.out.print("번호를 선택해주세요: ");
            int menu = input.nextInt();

            if (menu == 4) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else if (menu == 1) {
                System.out.print("입금액을 입력하세요: ");
                int amount = input.nextInt();
                balance = deposit(balance, amount);
            } else if (menu == 2) {
                System.out.print("출금액을 입력하세요: ");
                int amount = input.nextInt();
                balance = withdraw(balance, amount);
            } else if (menu == 3) {
                System.out.println("잔액을 확인합니다.");
                checkBalance(balance);
            } else {
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
