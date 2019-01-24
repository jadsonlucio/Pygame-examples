import pygame
import numpy 
from math import cos,sin

ROTATE_ANGLE = 0
ROTATE_INCREASE = 0.0005

WIDTH = 400
HEIGHT = 300
POINT_SIZE = 10
POINTS = numpy.array([[50,50,50],[50,-50,50],[-50,50,50],[-50,-50,50],[50,50,-50],[50,-50,-50],[-50,50,-50],[-50,-50,-50]])
CONVERT_MATRIX = [[1,0,0],[0,1,0]]
COLORS_POINTS = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(122,122,122),(255,255,255)]
CONECTED_POINTS = [[0,2],[0,1],[0,4],[1,3],[1,5],[2,3],[2,6],[3,7],[4,6],[4,5],[5,7],[6,7]]
POLYGONS_POINTS = [[0,2,6,4],[0,1,3,2],[0,1,5,4],[1,3,7,5],[2,6,7,3],[5,7,6,4]]
POLYGONS_COLORS = [[255,0,0],[0,255,0],[0,0,255]]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False


def rotate_matriz_overx(matrix_points, angle):
    rotation_matrix = numpy.array([[1,0,0], [0,cos(angle), -sin(angle)],[0, sin(angle), cos(angle)]])
    for point in matrix_points:
        yield numpy.dot(rotation_matrix, numpy.array(point))

def rotate_matriz_overy(matrix_points, angle):
    rotation_matrix = numpy.array([[cos(angle),0, sin(angle)],[0,1,0],[-sin(angle), 0, cos(angle)]])
    for point in matrix_points:
        yield numpy.dot(rotation_matrix, numpy.array(point))

def matrix3d_to_2d(matrix_3d, convert_matrix):
    for point in matrix_3d:
        yield numpy.dot(numpy.array(convert_matrix), numpy.array(point)) 

def translate2d_point(point, widht = WIDTH/2, height = HEIGHT/2):
    return (int(point[0])+int(widht), int(point[1])+int(height))



def draw_points(surface, points, point_size):
    points = list(rotate_matriz_overx(points, ROTATE_ANGLE))
    points = list(rotate_matriz_overy(points, ROTATE_ANGLE))
    points = list(matrix3d_to_2d(points, CONVERT_MATRIX))
    points = list(map(translate2d_point, points))
    for point,color in zip(points, COLORS_POINTS):
        pygame.draw.circle(surface, color, point, point_size, 0)

    for index_1,index_2 in CONECTED_POINTS:
        pygame.draw.aaline(surface, (255,255,255), points[index_1], points[index_2])

    for polygon_points,color in zip(POLYGONS_POINTS,POLYGONS_COLORS):
        pygame.draw.polygon(surface, color, [points[point_index] for point_index in polygon_points])

    #pygame.draw.polygon(surface, (255,255,255), points)

        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            ROTATE_INCREASE = 0.0005 if ROTATE_INCREASE == 0 else 0

    screen.fill((0,0,0))            
    draw_points(screen ,POINTS, POINT_SIZE)
    pygame.display.flip()

    ROTATE_ANGLE+=ROTATE_INCREASE


pygame.quit()
