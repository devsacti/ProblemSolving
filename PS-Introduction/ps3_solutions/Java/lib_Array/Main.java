import java.util.Arrays;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


class Node {

    private int x;
    private int y;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }
    
    public int getY() {
        return this.y;
    }

    public String toCustomString(){
        return "("+this.x+","+this.y+")";
    }
}

public class Main{

    public static int[] arr = {4,23,33,15,17,19};
    public static Integer[] arrObject={4,23,33,15,17,19};
    
    public static ArrayList<Integer> list = new ArrayList<Integer>(Arrays.asList(4,23,33,15,17,19));
    public static ArrayList<Integer> list2 = new ArrayList<Integer>();

    public static void main(String[] args){
        
        // basic array print
        for (int i : arr) {
            System.out.print("["+i+"]");
        }
        System.out.println();

        // Arrays.toString print
        System.out.println(Arrays.toString(arr));

        // Arrays.sort() asc and Arrays.toString()
        Arrays.sort(arr);
        System.out.println(Arrays.toString(arr));

        // Arrays.sort() desc and Arrays.toString()
        // desc의 경우 Integer 또는 Long으로 객체 단위로 설명해야함, Long의 경우 L도 덧붙여주고
        
        Arrays.sort(arrObject,Collections.reverseOrder());
        System.out.println(Arrays.toString(arrObject));

        // 더 높은 일관성을 위해, 우선은 ArrayList<> 형태로 자료구조화
        System.out.println(list);

        list2.add(5);
        list2.clear();
    
        list2.add(4);
        list2.add(3);
        list2.remove(1);
        list2.add(2);
        list2.add(1);

        System.out.println(list2);

        // deep copy
        ArrayList<Integer> list3 = new ArrayList<Integer>();
        for(Integer item : list2){
            list3.add(item);
        }

        System.out.println(list3);
        list3.add(9);
        list2.set(1, -1);

        System.out.println(list3);
        System.out.println(list2);

        // ArrayList 정렬
        Collections.sort(list3);
        System.out.println(list3);
        Collections.sort(list3,Collections.reverseOrder());
        System.out.println(list3);

        // ArrayList object 정렬 ; 다중 정렬
        ArrayList<Node> nodeList = new ArrayList<Node>();

        nodeList.add(new Node(5, 1));
        nodeList.add(new Node(4, 2));
        nodeList.add(new Node(3, 3));
        nodeList.add(new Node(3, 9));
        nodeList.add(new Node(2, 4));
        nodeList.add(new Node(1, 5));

        for(Node item : nodeList){
            System.out.print(item.getX());
            System.out.print(" ");
            System.out.print(item.getY());
            System.out.print(" ");
            System.out.println(item.toString());
        }

        for(int i=0;i<nodeList.size();i++){
            System.out.print(nodeList.get(i).toCustomString());
            System.out.print(" ");
        }
        System.out.println();

        nodeList.sort(Comparator.comparing(Node::getX).thenComparing(Node::getY));
        for(int i=0;i<nodeList.size();i++){
            System.out.print(nodeList.get(i).toCustomString());
            System.out.print(" ");
        }

        System.out.println();
        Comparator<Node> reverse = Comparator.comparing(Node::getY).reversed();

        nodeList.sort(Comparator.comparing(Node::getX).thenComparing(reverse));
        for(int i=0;i<nodeList.size();i++){
            System.out.print(nodeList.get(i).toCustomString());
            System.out.print(" ");
        }
    }
}