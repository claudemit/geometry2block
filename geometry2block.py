#coding=utf-8
"""
convert geometry in rhino to block for sketchup
written by claudemit
2015-09-26
"""

import rhinoscriptsyntax as rs
import System

def cp_filt(rhino_object, geometry, component_index):
    return rs.IsBrep(geometry) | rs.IsMesh(geometry)

def Geo2Block():
    #属性--设置图层
    layName= rs.GetString("Add a New Layer to put Blocks")
    if layName in rs.LayerNames():
        rs.MessageBox("This LayerName already exist!")
        return
    rs.AddLayer(layName,System.Drawing.Color.Gold)
    
    #选取几何体 
    go = rs.GetObjects("Select Geometry",custom_filter= cp_filt)
    ObjRefs = go
    
    #生成图块
    if(ObjRefs):
        basepoint = rs.AddPoint(0,0,0)
        i= 0
        for obj in ObjRefs:
            name = 'block_%s' %i
            if rs.IsBlock(name):
                rs.MessageBox("Block Definition"+ name+"Already Exists")
                name= name+'_1'    
            block= rs.AddBlock([obj], basepoint, name, False)            
            rs.ObjectLayer(rs.InsertBlock(block, basepoint), layName)
            i= i+1
        rs.MessageBox("IN TOTAL %d BLOCKS" % i)
    else:
        rs.DeleteLayer(layName)
        rs.MessageBox("No Geometry Selected!")
        return
    
if( __name__ == "__main__" ):
  #call function defined above
  Geo2Block();
