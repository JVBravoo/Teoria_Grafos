import java.util.List;
import java.util.ArrayList;

public class Grafo(){
    
    public class Vertice{
        String name;
        List<Aresta> adj;

        Vertice(String name){
            this.name = name;
            this.adj = new ArrayList<Aresta>();
        }

        public void addAdj(aresta a){
            adj.add(a);
        }

        void replace(name, aresta){
            this.name = name;
            this.aresta = aresta;
        }

        void getName(){
            return this.name;
        }

        void getVertice(){
            return this.Vertice;
        }
    }

    public class Aresta{
        String n;
        String end;

        Aresta(String n, String end){
            this.n = n;
            this.end = end;
        }
    }

    List<Vertice> vertices;
    List<Aresta> arestas;

    
    public Grafo(){
        vertices = new ArrayList<Vertice>();
        arestas = new ArrayList<Aresta>();
    }

    Vertice addVertice(String name){
        Vertice u = new Vertice(name);
        vertices.add(u);
        return u;
    }

    Aresta addAresta(Vertice n, end){
        Aresta a = new Aresta(n, end);
        n.addAdj(a);
        arestas.add(a);
        return a;
    }

    void getVertice(){
        return this.vertice;
    }
/*
// Incompleto
// Função de incident

    void getAresta(){
        final edge = [];
        this.getVertice().for (u : Vertice) {
            final incidentEdges = this.incidentEdges(u);
            incidentEdges.for (v : Vertice) {
                final edge1 = {}
                edge1[v.getName()] = {
                    u.getName()
                }
            }
        }
    }
*/

//  Incompleto
//  Função de opposite

/*    void opposite(n, end){
        final aresta = this.search(n, end);
        if(aresta){
            return aresta.getOpposite();
        }
        else{
            System.out.println('Erro!');
        }
    }
*/

//  Incompleto
//  Função de adajacent

/*
    void areAdajacent(v, w){
        final wname = w.getName();
        final opposite = incidentEdges.filter(a.getOpposite().getName() == wname)

        return wname;
    }
*/

    String toString(){
        String graph = "";
        
        for(Vertice one : vertices){
            graph = graph + one.name + " ---- ";
            for(Aresta a : one.adj){
                Vertice u = a.end;
                graph = graph + u.name;
            } 
        }
        return graph;
    }


    public static void main(String[] args){

        Grafo grafo = new Grafo();
        
        Vertices u = grafo.addVertice('u');
        Vertices v = grafo.addVertice('v');
        Vertices w = grafo.addVertice('w');

        Aresta a = grafo.addAresta('uv');
        Aresta b = grafo.addAresta('vw');
        Aresta c = grafo.addAresta('uw');

        System.out.println(grafo);
    }
}