#Import maya module

#Create Cubes and move them

#Create group of cubes

#Duplicate cubes and offset them in y axis

import maya.cmds as cmd
#creates a group of cubes
#lines up the cubes in a row and creates a group
cmd.polyCube( w=20, d=10, h=5, n='cube1')
cmd.polyCube( w=20, d=10, h=5, n='cube2')
cmd.move( 20, 0, 0 )
cmd.polyCube( w=20, d=10, h=5, n='cube3')
cmd.move( 40, 0, 0 )
cmd.polyCube( w=20, d=10, h=5, n='cube4')
cmd.move( 60, 0, 0 )
cmd.polyCube( w=20, d=10, h=5, n='cube5')
cmd.move( 80, 0, 0 )
cmd.polyCube( w=20, d=10, h=5, n='cube6')
cmd.move( 100, 0, 0 )
cmd.group('cube1', 'cube2', 'cube3', 'cube4', 'cube5', 'cube6')

#duplicate group and move up in y axis
cmd.duplicate( 'group1' )
cmd.move( 0,5,0)
cmd.duplicate( 'group2' )
cmd.move( 0,10,0)
cmd.duplicate( 'group3' )
cmd.move( 0,15,0)
cmd.duplicate( 'group4' )
cmd.move( 0,20,0)




