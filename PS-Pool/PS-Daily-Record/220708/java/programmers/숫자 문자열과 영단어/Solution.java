import java.io.*;// BufferedReader, InputStreamReader, IOException
import java.util.*;// StringTokenizer, Arrays, List, ArrayList
// Integer, StringBuilder

class Solution {
    public int solution(String s) {
        
        String[] nums= {"0","1","2","3","4","5","6","7","8","9"};
        String[] words= {"zero" , "one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine"};
        for (int i = 0 ; i <10 ; i++){
            s = s.replace(words[i] , nums[i]);
        }
        Long temp = Long.parseLong(s);
        return temp.intValue();
    }
}