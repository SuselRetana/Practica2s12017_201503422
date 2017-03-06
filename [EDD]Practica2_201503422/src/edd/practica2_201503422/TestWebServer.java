/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edd.practica2_201503422;


import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

/**
 *
 * @author freni_000
 */
public class TestWebServer {

    public static OkHttpClient webClient = new OkHttpClient();
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String nombre = "Marco";
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", nombre)
                .add("dato2", "4")
                .build();
        String r = getString("metodoWeb", formBody); 
        System.out.println(r + "---");
    }
    public static void nombre(String nombre)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", nombre)
                .add("dato2", "4")
                .build();
        String r = getString("metodoWeb", formBody); 
        System.out.println(r + "---");
    }
    
    public static void insertarLista(String Valor)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", Valor)
                .build();
        String r = getString("agregarLista", formBody); 
        System.out.println(r);
    }
    public static void buscarLista(String Valor)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", Valor)
                .build();
        String r = getString("BuscarLista", formBody); 
        System.out.println(r);
    }
    public static void EliminarLista(String Valor)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", Valor)
                .build();
        String r = getString("EliminarLista", formBody); 
        System.out.println(r);
    }
       public static void Push(String Valor)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", Valor)
                .build();
        String r = getString("Push", formBody); 
        System.out.println(r);
    }
          public static void Queue(String Valor)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", Valor)
                .build();
        String r = getString("Queue", formBody); 
        System.out.println(r);
    }
          public static void Pop(String Valor)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", Valor)
                .build();
        String r = getString("Pop", formBody); 
        System.out.println(r);
    }          
     
          public static void Dequeue(String Valor)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", Valor)
                .build();
        String r = getString("Dequeue", formBody); 
        System.out.println(r);
    }       
     public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}