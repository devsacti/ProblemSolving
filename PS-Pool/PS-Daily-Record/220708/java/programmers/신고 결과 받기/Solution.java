import java.io.*; // BufferedReader, InputStreamReader, IOException
import java.util.*; // StringTokenizer, Arrays,List,ArrayList

class Solution {
    static HashSet<String> reportSet = new HashSet<String>();
    
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        int[] idReportedCnt = new int[id_list.length];
        List<String> idList = Arrays.asList(id_list);
        // System.out.println(Arrays.toString(id_list));
        
        for(String r : report){
            reportSet.add(r);
        }
        
        for(String r : reportSet){
            String[] rContents = r.split(" ");
            String reporter = rContents[0];
            String reported = rContents[1];
            
            int idxReporter = idList.indexOf(reporter);
            int idxReported = idList.indexOf(reported);
            
            idReportedCnt[idxReported]+=1;
        }
        
        for(String r : reportSet){
            String[] rContents = r.split(" ");
            String reporter = rContents[0];
            String reported = rContents[1];
            
            int idxReporter = idList.indexOf(reporter);
            int idxReported = idList.indexOf(reported);
            
            if(idReportedCnt[idxReported] >= k){
                answer[idxReporter]+=1;
            }
        }
        
        return answer;
    }
}