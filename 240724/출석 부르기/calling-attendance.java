import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();
        
        // 학생 이름을 저장하는 배열
        String[] students = { "John", "Tom", "Paul" };
        
        // 출석번호에 해당하는 학생 이름 출력
        if (number >= 1 && number <= students.length) {
            System.out.println(students[number - 1]);
        } else {
            System.out.println("Vacancy");
        }
        
        scanner.close();
    }
}