/*


*/
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int t=sc.nextInt();
        sc.nextLine();

        int[][] arr=new int[t][10];

        for(int i=0;i<t;i++){
            for(int j=0;j<10;j++){
                arr[i][j]=sc.nextInt();
            }
        }

        for(int i=0;i<t;i++){
            int sum=0;
            for(int j=0;j<10;j++){
                if(arr[i][j]%2==1){
                    sum+=arr[i][j];
                }
            }
            System.out.print("#"+(i+1)+" "+sum+"\n") ;
        }

     } 
}
