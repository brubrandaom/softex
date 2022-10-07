import java.io.Serializable;


public class Autor implements Serializable{
    public String nome;
    public String nacionalidade;
    public int idade;
    public int livrosEscritos;

    public Autor(String nome, String nacionalidade, int idade, int livrosEscritos){
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.idade = idade;
        this.livrosEscritos = livrosEscritos;
    }
}
    




