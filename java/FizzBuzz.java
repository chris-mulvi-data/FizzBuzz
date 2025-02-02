/**
 * fizzbuzz
 */
public class FizzBuzz {

    public void normalFizzBuzz(int maxNumber) {
        for (int i = 0; i < maxNumber; i++) {
            String output = "";
            if ((i + 1) % 3 == 0) {
                output += "Fizz";
            }
            if ((i + 1) % 5 == 0) {
                output += "Buzz";
            }
            if (!output.isEmpty()) {
                System.out.println(output);
            } else {
                System.out.println(i + 1);
            }
        }
    }
}
