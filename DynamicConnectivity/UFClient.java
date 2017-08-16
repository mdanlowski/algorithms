//package com.mdski.algorithms;

public class UFClient {

    public void QuickFindTest(){
        System.out.println("Quick Find:");
        QuickFind uf = new QuickFind(10);
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
    public void QuickUnionTest(){
        System.out.println("\nQuick Union:");
        QuickUnion uf = new QuickUnion(10);
        for(int elem : uf.getId()) System.out.print(elem + " ");
        System.out.println();
        uf.union(4,3);
        uf.union(6,5);
        uf.union(6,7);

        for(int elem : uf.getId()) System.out.print(elem + " ");
        System.out.println();
        System.out.println(
                "id[0]<-->id[1]: "+uf.connected(0,1)+"\nid[6]<-->id[7]: "
                +uf.connected(6,7)+"\nid[3]<-->id[4]: "+uf.connected(3,4)+"\nid[6]<-->id[5]: "+uf.connected(6,5)
        );

    }

}
