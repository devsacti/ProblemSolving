import java.io.*;
import java.util.*;

class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = arr1;
        
        for(int r=0;r<arr1.length;r++){
            for(int c=0;c<arr1[0].length;c++){
                answer[r][c]+=arr2[r][c];
            }
        }
        
        return answer;
    }
}