import java.util.*;

class Solution {
    public static int n;
    public static char[] samplespace;
    public static char[] result;
    public static int[] visited;
    public static Set<Integer> primeSet = new HashSet();
    
    public int solution(String numbers) {
        int answer = 0;
        
        n=numbers.length();
        samplespace = new char[n];
        result= new char[n];
        visited = new int[n];
        
        // for(int i=0;i<n;i++){
        //     samplespace[i]=numbers.charAt(i)-'0';
        // }
        // System.out.println(Arrays.toString(samplespace));
        samplespace = numbers.toCharArray();
        // System.out.println(Arrays.toString(samplespace));
        // System.out.println();
        
        for(int r=1;r<=n;r++){
            permMakePrim(0, n, r);
            System.out.println();
        }
        
        return primeSet.size();
    }
    
    // 사전순으로 순열 구하기
    // 사용 예시: perm(arr, output, visited, 0, n, 3);
    public static void permMakePrim(int depth, int n, int r) {
        if (depth == r) {
            // System.out.println(Arrays.toString(result));
            StringBuilder sb = new StringBuilder();
            for(int i=0;i<r;i++){
                sb.append(result[i]);
            }
            // System.out.println(sb.toString());
            String numStr = sb.toString();
            // System.out.println(numStr);
            int candNum = Integer.parseInt(numStr);
            // System.out.println(candNum);
            if(isPrime(candNum)){
                primeSet.add(candNum);
            }
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                result[depth] = samplespace[i];
                permMakePrim(depth + 1, n, r);
                visited[i] = 0;
            }
        }
    }
    //
    public static boolean isPrime(int n){
        if(n < 2) return false;
        for(int i=2; i<=Math.sqrt(n); i++)
            if(n%i==0) return false;
        return true;
    }
}