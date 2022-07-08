import java.io.*; // BufferedReader, InputStreamReader, IOException
import java.util.*; // StringTokenizer, Arrays, List, ArrayList

class Solution {
    public void solution() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int col = Integer.parseInt(st.nextToken());
        int row = Integer.parseInt(st.nextToken());
        // System.out.println(col);System.out.println(row);
        for(int r=0;r<row;r++){
            for(int c=0;c<col;c++){
                System.out.print("*");
            }
            System.out.println();
        }
    }

}