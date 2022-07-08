import java.io.*; // BufferedReader, InputStreamReader, IOException
import java.util.*; // StringTokenizer, Arrays, List,ArrayList, HashSet

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        int rank = 7;
        int zeroCnt= 0;
        for(int lotto : lottos){
            boolean t = contains(win_nums,lotto);
            if(t){
                rank-=1; // 최소랭크
            }
            
            if(lotto==0){
                zeroCnt+=1;
            }
        }
        answer[0]=rank-zeroCnt;
        answer[1]=rank;
        // 7 그리고 7 0 예외처리 필요
        if(rank == 7){
            if(zeroCnt==0){
                answer[0]-=1;
                answer[1]-=1;
            }else{
                answer[1]-=1;    
            }
        }else{

        }
        
        return answer;
    }
    
    public static boolean contains(int[] std, int num){
        return Arrays.stream(std).anyMatch(item -> item == num);
    }
}