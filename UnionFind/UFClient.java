// package com.mdski.algorithms;

public class UFClient {

    public void QuickFind(){
        UnionFind uf = new UnionFind(10);
        for(int elem : uf.getId()) System.out.print(elem + " ");
        System.out.println();
        uf.union(0,1);
        uf.union(3,4);

        for(int elem : uf.getId()) System.out.print(elem + " ");
        System.out.println();
        System.out.println(
                "id[0]<-->id[1]: "+uf.connected(0,1)+"\nid[1]<-->id[2]: "+uf.connected(1,2)+"\nid[3]<-->id[4]: "+uf.connected(3,4)
                );
    }

}
