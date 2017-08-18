package com.mdski.algorithms;

public class QuickUnionWeighted extends QuickUnion {
    private int[] sz;
    public int[] getSize() {
        return sz;
    }
    QuickUnionWeighted(){ // Default constructor
        id = new int[10];
        sz = new int[id.length];
        for(int i = 0; i < id.length; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }
    QuickUnionWeighted(int size){
        id = new int[size];
        sz = new int[id.length];
        for(int i = 0; i < id.length; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }
    public void union(int p, int q){
        int x = root(p); // root of object with index p
        int y = root(q); // root of object with index q
        if(sz[x] >= sz[y]){ // LINK THE ROOT OF SMALLER THREE TO THE ROOT OF LARGER TREE
            id[y] = x;       // to union two objects, set root of one equal to root of another - therefore connecting two _connected components_
            sz[x] += sz[y];
        }
        else {
            id[x] = y;       // to union two objects, set root of one equal to root of another - therefore connecting two _connected components_
            sz[y] += sz[x];
        }


    }


}
