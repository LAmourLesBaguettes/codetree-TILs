import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = scanner.nextInt();

        String result = (score == 100) ? "pass" : "failure";

        System.out.println(result);

        scanner.close();
    }
}