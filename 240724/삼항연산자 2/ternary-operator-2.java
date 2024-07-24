import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();

        // 삼항 연산자를 사용하여 t와 f를 결정
        String result = (a == 1) ? "t" : "f";
        
        // 결과 출력
        System.out.println(result);
        
        scanner.close();
    }
}