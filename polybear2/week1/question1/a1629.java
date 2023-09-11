import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long c = Long.parseLong(st.nextToken());

        bw.write(Long.toString(cal(a,b,c)));
        bw.close();

    }
    public static long cal(long a, long b, long c){
        if (b==1) return a%c;

        long ans = cal(a, b/2, c);
        if(b%2 == 0){
            return  ans*ans%c;
        }
        else{
            return ans*ans%c*a%c;
        }
    }
}
