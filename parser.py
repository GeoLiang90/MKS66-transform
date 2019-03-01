from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
#Pass it the identity matrix

def parse_file( fname, points, transform, screen, color ):
    f = open(fname,'r')
    lines = f.read().splitlines()
    #print(lines)
    index = 0
    print(len(lines))
    while index != len(lines):
        print(index)
        args_used = False
        if (lines[index] == "line"):
            args_used = True
            args = lines[index + 1].split()
            args[0] = int(args[0])
            args[1] = int(args[1])
            args[2] = int(args[2])
            args[3] = int(args[3])
            args[4] = int(args[4])
            args[5] = int(args[5])
            add_edge(points,args[0],args[1],args[2],args[3],args[4],args[5])
        if (lines[index] == "ident"):
            ident(transform)
        if (lines[index] == "scale"):
            args_used = True
            args = lines[index + 1].split()
            args[0] = int(args[0])
            args[1] = int(args[1])
            args[2] = int(args[2])
            matrix_mult(make_scale(args[0],args[1],args[2]),transform)
        if (lines[index] == "translate"):
            args_used = True
            args = lines[index + 1].split()
            args[0] = int(args[0])
            args[1] = int(args[1])
            args[2] = int(args[2])
            matrix_mult(make_translate(args[0],args[1],args[2]),transform)
        if (lines[index] == "rotate"):
            args_used = True
            args = lines[index + 1].split()
            args[1] = int(args[1])
            if(args[0] == "x"):
                matrix_mult(make_rotX(args[1]),transform)
            if(args[0] == "y"):
                matrix_mult(make_rotY(args[1]),transform)
            if(args[0] == "z"):
                matrix_mult(make_rotZ(args[1]),transform)
        if (lines[index] == "apply"):
            matrix_mult(transform,points)
            for r in range(len(points)):
                for c in range(len(points[0])):
                    if (isinstance(points[r][c],float)):
                        points[r][c] = int(points[r][c])
        if (lines[index] == "display"):
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        if (lines[index] == "save"):
            args_used = True
            args = lines[index + 1].split()
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,args[0])
        if (lines[index] == "quit"):
            index = len(lines)
        if (args_used):
            index += 1
        index += 1

    pass
