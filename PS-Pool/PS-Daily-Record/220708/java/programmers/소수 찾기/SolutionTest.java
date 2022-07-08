public class SolutionTest {
    public static void main(String[] args) {
        int n = 3;
        int[] arr = {1, 2, 3};
        int[] output = new int[n];
        boolean[] visited = new boolean[n];

        Perm perm = new Perm();
        perm.perm(arr,output,visited,0, n, 3);

    }
}
