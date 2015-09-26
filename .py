#coding=utf-8
"""
convert geometry in rhino to blocks for sketchup
written by claudemit
2015-09-26
"""

import rhinoscriptsyntax as rs
import System

def cp_filt(rhino_object, geometry, component_index):
    return rs.IsBrep(geometry) or rs.IsMesh(geometry)

def Brep2Block():
    #属性--设置图层
    layName= rs.GetString("make a new layer for blocks")
    if layName=="":
        rs.MessageBox("no layer!")
        return
    if layName in rs.LayerNames():
        rs.MessageBox("not a new layer!")
        return
    rs.AddLayer(layName,System.Drawing.Color.Gold)
    
    #选取几何体 
    go = rs.GetObjects("seltect breps",custom_filter= cp_filt)
    ObjRefs = go
    
    #生成图块
    if(ObjRefs):
        basepoint = rs.AddPoint(0,0,0)
        i= 0
        for obj in ObjRefs:
            name = 'block_%s' %i
            if rs.IsBlock(name):
                rs.MessageBox("Block definition"+ name+"already exists")
                name= name+'_1'    
            print name
            block= rs.AddBlock([obj], basepoint, name, False)
            rs.InsertBlock(name, basepoint)
            i= i+1
    
    rs.MessageBox("IN TOTAL %dBLOCKS" % i)
    
if( __name__ == "__main__" ):
  #call function defined above
  Brep2Block();
