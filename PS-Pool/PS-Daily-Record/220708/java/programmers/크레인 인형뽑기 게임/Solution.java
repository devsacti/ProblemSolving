import java.io.*; // BufferedReader, InputStreamReader, IOException
import java.util.*; // StringTokenizer | Arrays | List, ArrayList | Stack
// Integer, Long
// StringBuilder

class Solution {
  public int solution(int[][] board, int[] moves) {
    int answer = 0;

    Stack<Integer> stack = new Stack<>();
    stack.push(0);

    for (int move : moves) {
      for (int r = 0; r < board.length; r++) {
        if (board[r][move - 1] != 0) {
          if (stack.peek() == board[r][move - 1]) {
            stack.pop();
            answer += 2;
          } else {
           stack.push(board[r][move - 1]);
          }
          board[r][move - 1] = 0;
          break;
        }
      }
    }
    return answer;
  }

}