import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = -1;
        
        int sum = 45;
        
        for(int num : numbers){
            sum-=num;
        }
        answer=sum;
        return answer;
    }

}