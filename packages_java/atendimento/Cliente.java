package atendimento;

public class Cliente {
    private String nome;
    private String cpf;
    
    public String getNome(){
        return this.nome;
    }
    
    public void setNome(String newNome){
        this.nome = newNome;
    } 
    
    public String getCpf(){
        return this.cpf;
    }
    
    public void setCpf(String newCpf){
        this.cpf = newCpf;
    }
}
