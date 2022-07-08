import java.util.*;

class Solution2 {

    public int solution(int[] numbers) {
        int answer = 0;
        
        for(int num=0;num<=9;num++){
            boolean t = contains(numbers,num);
            if(!t){
                answer += num;
            }
        }
        return answer;
    }

    public static boolean contains(int[] arr, int key){
        return Arrays.stream(arr).anyMatch(item -> item == key);
    }
}