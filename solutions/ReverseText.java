import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class ReverseText {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
        ReverseText.reverseSpell(line);
    }
  }

  public static void reverseSpell(String input) {
    // Write your code here.
    String reversed = "";
    for (int i = input.length() - 1; i>=0; i--){
      reversed = reversed + input.charAt(i);
    }
    System.out.println(reversed);    
  }
}