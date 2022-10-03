import atendimento.Cliente;
import estoque.Produto;

public class Empresa {

    public static void main(String[] args) {
        Cliente cliente1 = new Cliente();
        cliente1.setNome("Alice");
        cliente1.setCpf("12345678910");
        
        Produto produto1 = new Produto();
        produto1.setNome("Caneta");
        produto1.setCodigo("1234");
        produto1.setQuantidade(20);
    }
    
}
