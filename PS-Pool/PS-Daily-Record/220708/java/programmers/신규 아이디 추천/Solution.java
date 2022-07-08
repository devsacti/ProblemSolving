import java.io.*; // BufferedReader, InputStreamReader, IOException
import java.util.*;// StringTokenizer, Arrays, List, ArrayList 
// Integer

class Solution {
    public String solution(String new_id) {
        String answer = "";
        
        answer=new_id.toLowerCase();
        // [^xy] : x 또는 y를 제외한 한 문자
        answer=answer.replaceAll("[^-_.a-z0-9]", ""); // 2단계
        // [] 후보 리스트
        //x{m,n} : x의 m번 이상 n번 이하 반복
        answer = answer.replaceAll("[.]{2,}", "."); // 3단계
        // ^x : 문자열이 x로 시작, x$ : 문자열이 x로 끝남
        answer = answer.replaceAll("^[.]|[.]$", "");    // 4단계
        
        if (answer.equals("")) {    // 5단계
            answer += "a";
        }

        if (answer.length() >= 16) {     // 6단계
            answer = answer.substring(0, 15);
            answer = answer.replaceAll("[.]$","");
        }
        
        if (answer.length() <= 2) {  // 7단계
            while (answer.length() < 3) {
                answer += answer.charAt(answer.length()-1);
            }
        }
        return answer;
    }
    
    public static boolean valid(String[] std, char charVal){
        return Arrays.stream(std).anyMatch(item -> item.equals(charVal));
    }
}