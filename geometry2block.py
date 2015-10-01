#coding=utf-8
"""
convert geometry in rhino to block for sketchup
written by claudemit
2015-09-26
"""
from time import clock
import Rhino
import rhinoscriptsyntax as rs
import System

def cp_filt(rhino_object, geometry, component_index):
    return rs.IsBrep(geometry) | rs.IsMesh(geometry)

def Geo2Block():
    Rhino.RhinoApp.RunScript("_Purge Enter",False)
    #属性--设置图层
    layName= rs.GetString("Add a New Layer to put Blocks")
    if layName in rs.LayerNames():
        rs.MessageBox("This LayerName already exist!")
        return
    layId= rs.AddLayer(layName,System.Drawing.Color.Gold)
    preLayer= rs.CurrentLayer(layId)
    
    #选取几何体     
    ObjIds= rs.GetObjects("Select Geometry",custom_filter= cp_filt)
    
    #生成图块
    start= clock()
    basepoint = rs.AddPoint(0,0,0)
    if(ObjIds):        
        i= 0
        for obj in ObjIds:
            name = 'block_%s' %i
            if rs.IsBlock(name):
                rs.MessageBox("Block Definition"+ name+"Already Exists")
                name= name+'_1'    
            block= rs.AddBlock([obj], basepoint, name, False)            
            rs.InsertBlock(block, basepoint)
            i= i+1
        print clock()-start
        rs.MessageBox("IN TOTAL %d BLOCKS" % i)        
    else:        
        rs.DeleteLayer(layId)
        rs.MessageBox("No Geometry Selected!")   
    rs.CurrentLayer(preLayer)
    rs.DeleteObject(basepoint)
    
if( __name__ == "__main__" ):
  #call function defined above
  Geo2Block();
