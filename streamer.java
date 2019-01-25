import java.util.Scanner;
import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.net.ProtocolException;


import javafx.scene.media.Media;



public class streamer {
    public static void main(String[] args) {
       System.out.println("Wecome to the Video Streamer!");

       ////Get Playlist File Information
       System.out.println("Enter your M3U8 File URL:");
       Scanner sc = new Scanner(System.in);
       String playlistInfo = sc.next();
       System.out.println("\n"+ "playlistInfo entered:" + playlistInfo);
       ArrayList<String> list = getPlayListArray(playlistInfo);


       //// Get Video Information
       System.out.println("Enter Video Prefix:");
       Scanner vp = new Scanner(System.in);
       String videoPrefix = vp.next();
       System.out.println("\n"+ "videoPrefix entered:" + videoPrefix);

       ArrayList<String> videosLinks = new ArrayList<String> ();

       for (String link: list){
            videosLinks.add(videoPrefix + link);
            System.out.println(videoPrefix + link);
       }

       getGUIVideo();

       
    }

   

    public static  ArrayList<String> getPlayListArray(String url) {
        ArrayList<String> list = new ArrayList<String>();
        StringBuilder result = new StringBuilder();

        try {
       
        URL urlObject = new URL(url);
        HttpURLConnection conn = (HttpURLConnection) urlObject.openConnection();
        conn.setRequestMethod("GET");
        BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String line;
        while ((line = rd.readLine()) != null) {
            if (!line.startsWith("#")){
               list.add(line); 
            }
        //    result.append("\n"+line);
        }
        rd.close();
        }
        catch (IOException io)
        {
            System.out.println("IO Exception:");
        }
      

     //   System.out.println("\n"+ "Output String:" + list.toString());


        return list;
    }

    public static void getGUIVideo(){
        // URL mediaURL = new URL("./TheTerminal.mp4");
        MediaPlayer mediaPanel = new MediaPlayer();
        mediaPanel.setMediaLocation("./TheTerminal.mp4");
    }

}