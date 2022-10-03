
package estoque;

public class Produto {
    public String nome;
    public String codigo;
    private int quantidade;
    
    public String getNome(){
        return this.nome;
    }
    
    public void setNome(String newNome){
        this.nome = newNome;
    }
    
    public String getCodigo(){
        return this.codigo;
    }
    
    public void setCodigo(String newCodigo){
        this.codigo = newCodigo;
    }
    
    public int getQuantidade(){
        return this.quantidade;
    }
    
    public void setQuantidade(int newQuantidade){
        this.quantidade = newQuantidade;
    }
}
