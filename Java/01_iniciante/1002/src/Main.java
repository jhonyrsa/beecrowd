import java.util.Scanner;

public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       double pi = 3.14159;
       Scanner novo = new Scanner(System.in);
       double raio = novo.nextDouble();
       double area = raio*raio*pi;
       System.out.printf("A=%.4f\n", area);
    }
    
}
