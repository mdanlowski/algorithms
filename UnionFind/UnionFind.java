package com.mdski.algorithms;

public class UnionFind{
    private int[] id;
    public int[] getId() {
        return id;
    }
    UnionFind(int size){
        id = new int[size];
        for(int i = 0; i < id.length; i++) id[i] = i;
    }
    void union(int p, int q){
        int pid = id[p];
        int qid = id[q];
        for(int i = 0; i < id.length; i++){
            if(id[i] == qid) id[i] = pid;
        }
    }
    boolean connected(int p, int q){
        return (id[p] == id[q]) ? true : false;
    }
}