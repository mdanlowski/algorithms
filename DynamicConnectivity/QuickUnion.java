//package com.mdski.algorithms;

public class QuickUnion extends UF{

    QuickUnion(){ // Default constructor
        id = new int[10];
        for(int i = 0; i < id.length; i++) id[i] = i;
    }
    QuickUnion(int size){
        id = new int[size];
        for(int i = 0; i < id.length; i++) id[i] = i;
    }
    private int root(int examinedObjectIndex){
        while(examinedObjectIndex != id[examinedObjectIndex]) examinedObjectIndex = id[examinedObjectIndex];
        return examinedObjectIndex;
    }
    public void union(int p, int q){
        int x = root(p); // root of object with index p
        int y = root(q); // root of object with index q
        id[x] = y;       // to union two objects, set root of one equal to root of another - therefore connecting two _connected components_
    }
    public boolean connected(int p, int q){
        return root(p) == root(q);
    }


}
