import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class temp{
    public static class Node {
        long data;
        Node left = null;
        Node right = null;
        Node(long elem) {
            this.data = elem;
        }
    }
    public static long[] MergeTwoArrays(long[]arr1 , long[]arr2){
        int n = arr1.length, m = arr2.length;
        int i=0,j=0,k=0; 
        long[] merged = new long[(int)n+m];
        while(i<n && j<m){
            if(arr1[(int)i]<arr2[(int)j]){
                merged[(int)k] = arr1[(int)i];
                i++; k++;
            }
            else{
                merged[(int)k] =arr2[(int)j];
                k++;j++;
            }
        }
        if(i==n){
            while(j<m){
                merged[(int)k]= arr2[(int)j];
                j++;k++;
            }
        }
        if(j==m){
            while(i<n){
                merged[(int)k]= arr1[(int)i];
                i++;k++;
            }
        }
        return merged;
    }
    public static long[] Recursive(long[] arr, int i, int j){
        if(i>=j) {
            long[] temp = new long[1];
            temp[0] = arr[i];
            return temp;
        }
        int mid = (i+j)/2;
        long[] option1 = Recursive(arr,i,mid);
        long[] option2 = Recursive(arr,mid+1,j);
        return MergeTwoArrays(option1,option2);
    }
    public static void postorder(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");
            postorder(root.left);
            postorder(root.right);
        }
    }
    public static Node create(long post[], long start, int end) {
        if (start > end) {
            return null;
        }
        Node temp = new Node(post[end]);
        int i;
        for (i = end; i >= start; i--) {
            if (post[i] < temp.data) {
                break;
            }
        }
        temp.right = create(post, i + 1, end - 1);
        temp.left = create(post, start, i);
        return temp;
    }
    public static long sumofleaves(Node root){
        if(root==null) return 0;
        if(root.right==null && root.left==null) return root.data;
        return sumofleaves(root.left)+sumofleaves(root.right);
    }
    public static long right_sum(Node root){
        if(root==null) return 0;
        //System.out.println(root.data);
        if(root.right==null && root.left==null) return 0;
        if(root.right==null) return root.data+ right_sum(root.left);
        return root.data+right_sum(root.right);
    }
    public static long left_sum(Node root){
        if(root==null) return 0;
        //System.out.println(root.data);
        if(root.right==null && root.left==null) return 0;
        if(root.left==null) return root.data+ left_sum(root.right);
        return root.data+left_sum(root.left);
    }
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long[] arr = new long[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++) arr[i] = Long.parseLong(st.nextToken());
        //long[] inorder = Recursive(arr, 0, n-1);
        //for(int i=0;i<n;i++) System.out.println(arr[i]);
        Node answer = create(arr, 0,n-1);
        postorder(answer);
        long bottom_sum = sumofleaves(answer);
        //System.out.println(bottom_sum);
        long right_total = right_sum(answer.right);
        //System.out.println("LEFT");
        long left_total = left_sum(answer.left);
        //System.out.println(bottom_sum+" "+right_total+" "+left_total);
        if(n==1) System.out.println(bottom_sum);
        else System.out.println(bottom_sum+right_total+left_total+answer.data);   
    }
}