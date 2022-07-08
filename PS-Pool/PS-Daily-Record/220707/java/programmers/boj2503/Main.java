// java.io ; BufferReader , IOException, InputStreamReader
// util ; ArrayList, List, StringTokenizer
import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static String[] game;
    static int[] strike;
    static int[] ball;
    static int[] samplespace = {1,2,3,4,5,6,7,8,9};
    static int cnt;
    static int set[];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        game = new String[n];
        strike = new int[n];
        ball = new int[n];

        for(int tc = 0 ; tc<n ; tc++){
            StringTokenizer st  = new StringTokenizer(br.readLine());
            game[tc] = st.nextToken();
            strike[tc] = Integer.parseInt(st.nextToken());
            ball[tc] = Integer.parseInt(st.nextToken());
        }

        System.out.println(Arrays.toString(game));
        System.out.println(Arrays.toString(strike));
        System.out.println(Arrays.toString(ball));

        set = new int[9];

        for(int i = 0 ; i <9;i++){
            set[i]=i;
        }


    }

}