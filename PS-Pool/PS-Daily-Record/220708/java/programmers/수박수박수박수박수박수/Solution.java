class Solution {
    public String solution(int n) {
        String answer = "";
        
        String[] samplespace={"수","박"};
        
        StringBuilder sb = new StringBuilder();
        
        int idxRotate=0;
        for(int i=0;i<n;i++){
            idxRotate=i%2;
            sb.append(samplespace[idxRotate]);
        }
        answer = sb.toString();
        
        return answer;
    }
}