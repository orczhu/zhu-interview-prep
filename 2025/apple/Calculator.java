// 让你实现几个method
// Num add(Num n1, Num n2)
// Num subtract(Num n1, Num n2)
// Num multiply(Num n1, Num n2)
// Num divide(Num n1, Num n2)

public class Num {
    private int prev();
    private int next();
}
public class Calculator {
    public Num add(Num n1, Num n2) {
        Num rest = n1;
        for (int i = 0; i < n2; i++) {
            rest = rest.next();
        }
        return rest;
    }

    public Num subtract(Num n1, Num n2) {
        Num rest = n1;
        for (int i = 0; i < n2; i++) {
            rest = rest.prev();
        }
        return rest;
    }

    public Num multiply(Num n1, Num n2) {
        Num rest = 0;
        for (int i = 0; i < n2; i++) {
            rest = add(rest, n1);
        }
        return rest;
    }

    public Num divide(Num n1, Num n2) {
        Num temp = n1;
        Num rest = 0;
        while (temp > n2) {
            temp = subtract(temp, n2);
            rest.next();
        }
        return rest;
    }

}