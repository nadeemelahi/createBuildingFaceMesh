#
# author: Nadeem Elahi
# nadeem.elahi@gmail.com
# nad@3deem.com
# license: gpl v3
# 

import bpy
import numpy



def reset() :
	#https://blenderartists.org/t/deleting-all-from-scene/1296469
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete(use_global=False)



def fullReset() :
	#https://blenderartists.org/t/deleting-all-from-scene/1296469
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete(use_global=False)

	bpy.ops.outliner.orphans_purge()
	bpy.ops.outliner.orphans_purge()
	bpy.ops.outliner.orphans_purge()



def printVerts ( vertices ) :
    idx = 0
    lim = len ( vertices ) 

    while idx < lim :

        print ( idx , ":" , vertices[idx]  )

        idx += 1



#
def printVerts ( vertices ) :
	idx = 0
	lim = len ( vertices ) 

	while idx < lim :

		print ( idx , vertices [ idx ]  )

		idx += 1



# copy verts [cnt] number of verts from src to dst 
#   with supplied start idx for each
def copyArray ( 
		vertsSrc , srcStartIdx ,
		vertsDst , dstStartIdx , 
		cnt 
		) :

	idx = 0
	while idx < cnt :

		vertsDst[dstStartIdx + idx][0] = vertsSrc[idx][0]
		vertsDst[dstStartIdx + idx][1] = vertsSrc[idx][1]
		vertsDst[dstStartIdx + idx][2] = vertsSrc[idx][2]

		idx += 1


# set the same z value on a [cnt] number of verts
# useful for extruding a given geometry
def setVertZ ( verts , startIdx, cnt , zloc ) :

	idx = 0
	while idx < cnt :

		verts[idx + startIdx][2] = zloc

		idx += 1







#fullReset()
reset()

#          buffer size 100 , 3 dimensional each
verts = numpy.zeros( ( 100 , 3 ) , dtype=float )
# 100 -> 3D arrays

verts[  0 ] = (  0.0 ,  0.0 , 0.0 ) 
verts[  1 ] = (  3.0 ,  0.0 , 0.0 ) 
verts[  2 ] = (  3.2 ,  0.0 , 0.0 ) 
verts[  3 ] = (  4.9 ,  0.0 , 0.0 ) 
verts[  4 ] = (  5.0 ,  0.0 , 0.0 ) 
verts[  5 ] = (  5.1 ,  0.0 , 0.0 ) 
verts[  6 ] = (  6.8 ,  0.0 , 0.0 ) 
verts[  7 ] = (  7.0 ,  0.0 , 0.0 ) 
verts[  8 ] = ( 10.0 ,  0.0 , 0.0 ) 

verts[  9 ] = (  3.0 ,  5.0 , 0.0 ) 
verts[ 10 ] = (  3.2 ,  5.0 , 0.0 ) 

verts[ 11 ] = (  4.9 ,  5.0 , 0.0 ) 
verts[ 12 ] = (  5.0 ,  5.0 , 0.0 ) 
verts[ 13 ] = (  5.1 ,  5.0 , 0.0 ) 

verts[ 14 ] = (  6.8 ,  5.0 , 0.0 ) 
verts[ 15 ] = (  7.0 ,  5.0 , 0.0 ) 
		 
verts[ 16 ] = (  0.0 ,  6.0 , 0.0 ) 
verts[ 17 ] = (  3.0 ,  6.0 , 0.0 ) 

verts[ 18 ] = (  7.0 ,  6.0 , 0.0 ) 
verts[ 19 ] = ( 10.0 ,  6.0 , 0.0 ) 


verts[ 20 ] = (  0.0 ,  8.0 , 0.0 ) 
verts[ 21 ] = ( 10.0 ,  8.0 , 0.0 ) 

verts[ 22 ] = (  0.0 ,  9.0 , 0.0 ) 
verts[ 23 ] = (  0.5 ,  9.0 , 0.0 ) 
verts[ 24 ] = (  2.0 ,  9.0 , 0.0 ) 
verts[ 25 ] = (  3.0 ,  9.0 , 0.0 ) 
verts[ 26 ] = (  4.5 ,  9.0 , 0.0 ) 
verts[ 27 ] = (  5.5 ,  9.0 , 0.0 ) 
verts[ 28 ] = (  7.0 ,  9.0 , 0.0 ) 
verts[ 29 ] = (  8.0 ,  9.0 , 0.0 ) 
verts[ 30 ] = (  9.5 ,  9.0 , 0.0 ) 
verts[ 31 ] = ( 10.0 ,  9.0 , 0.0 ) 


verts[ 32 ] = (  0.0 , 13.0 , 0.0 ) 
verts[ 33 ] = (  0.5 , 13.0 , 0.0 ) 
verts[ 34 ] = (  2.0 , 13.0 , 0.0 ) 
verts[ 35 ] = (  3.0 , 13.0 , 0.0 ) 
verts[ 36 ] = (  4.5 , 13.0 , 0.0 ) 
verts[ 37 ] = (  5.5 , 13.0 , 0.0 ) 
verts[ 38 ] = (  7.0 , 13.0 , 0.0 ) 
verts[ 39 ] = (  8.0 , 13.0 , 0.0 ) 
verts[ 40 ] = (  9.5 , 13.0 , 0.0 ) 
verts[ 41 ] = ( 10.0 , 13.0 , 0.0 ) 

verts[ 42 ] = (  0.0 , 14.0 , 0.0 ) 
verts[ 43 ] = ( 10.0 , 14.0 , 0.0 ) 

verts[ 44 ] = (  0.0 , 16.0 , 0.0 ) 
verts[ 45 ] = ( 10.0 , 16.0 , 0.0 ) 




faces = numpy.array( [

        (   0 ,  1 , 17  ) ,
        (   0 , 17 , 16  ) ,

        (   1 ,  2 , 10  ) ,
        (   1 , 10 ,  9  ) ,

        (   2 ,  3 , 11  ) ,
        (   2 , 11 , 10  ) ,

        (   3 ,  4 , 12  ) ,
        (   3 , 12 , 11  ) ,

        (   4 ,  5 , 13  ) ,
        (   4 , 13 , 12  ) ,

        (   5 ,  6 , 14  ) ,
        (   5 , 14 , 13  ) ,

        (   6 ,  7 , 15  ) ,
        (   6 , 15 , 14  ) ,

        (   7 ,  8 , 19  ) ,
        (   7 , 19 , 18  ) , 

        (   9 , 15 , 18  ) , 
        (   9 , 18 , 17  ) , 

        (  16 , 19 , 21  ) , 
        (  16 , 21 , 20  ) , 

        (  20 , 21 , 31  ) , 
        (  20 , 31 , 22  ) , 

        (  22 , 23 , 33  ) , 
        (  22 , 33 , 32  ) , 

        (  23 , 24 , 34  ) , 
        (  23 , 34 , 33  ) , 

        (  24 , 25 , 35  ) , 
        (  24 , 35 , 34  ) , 

        (  25 , 26 , 36  ) , 
        (  25 , 36 , 35  ) , 

        (  26 , 27 , 37  ) , 
        (  26 , 37 , 36  ) , 

        (  27 , 28 , 38  ) , 
        (  27 , 38 , 37  ) , 

        (  28 , 29 , 39  ) , 
        (  28 , 39 , 38  ) , 

        (  29 , 30 , 40  ) , 
        (  29 , 40 , 39  ) , 

        (  30 , 31 , 41  ) , 
        (  30 , 41 , 40  ) , 

        (  32 , 41 , 43  ) , 
        (  32 , 43 , 42  ) , 

        (  42 , 43 , 45  ) , 
        (  42 , 45 , 44  )   

        ] )


print( "---" )
print( verts )


print( "---" )
printVerts( verts )

name = "name"

# verts to mesh
mesh = bpy.data.meshes.new ( name )
mesh.from_pydata ( verts , [] , faces )

# mesh to obj
obj = bpy.data.objects.new ( name , mesh )

# add ojb to scene
bpy.context.scene.collection.objects.link ( obj ) 
