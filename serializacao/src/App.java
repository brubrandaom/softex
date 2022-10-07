import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;


public class App {

    public static void main(String[] args) throws Exception {
        criarArquivo();
        lerArquivo();
    }
    private static void criarArquivo(){
        Autor a1 = new Autor("Neil Gaiman", "Ingles", 61, 44);
        FileOutputStream fos = null; 
        ObjectOutputStream oos = null;
        try{
            fos = new FileOutputStream("file.bin");
            oos = new ObjectOutputStream(fos);
            oos.writeObject(a1);
        }catch (FileNotFoundException e){
            System.out.println("Arquivo não encontrado");
        }catch (IOException e){
            System.out.println("Erro ao criar arquivo");
        } finally {
            if (oos!=null){
                try{
                    oos.close();
                }catch (IOException e){
                    System.out.println("Erro ao fechar arquivo");
                }
            }
        }
    }

    private static void lerArquivo(){
        Autor a1 = null;
        FileInputStream fis = null;
        ObjectInputStream ois = null;
        try {
            fis = new FileInputStream("file.bin");
            ois = new ObjectInputStream(fis);
            a1 = (Autor)ois.readObject();
            System.out.printf("Nome: %s\nNacionalidade: %s\nIdade: %d\nLivros escritos: %d\n", a1.nome, a1.nacionalidade, a1.idade, a1.livrosEscritos);
        } catch (ClassNotFoundException e){
            System.out.println("Classe não encontrado");
        } catch (IOException e){
            System.out.println("Erro ao ler arquivo");
        } finally {
            if (ois!=null){
                try{
                    ois.close();
                }catch (IOException e){
                    System.out.println("Erro ao fechar arquivo");
                }
            }
        }
    }
}

