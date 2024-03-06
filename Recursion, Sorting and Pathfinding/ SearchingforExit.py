import maze_helper as mh

position = (5,0)
maze = mh.sample_maze()
explored = []
print("Printing the initial sample maze:")
mh.print_maze(maze)
print('\n')


def dfs(x,position,explored):
    explored.append(position)
    for m in x:
        if m not in explored:
            position = m
            if mh.symbol_at(maze,position) == "X":
                mh.add_walk_symbol(maze,m)
                print("Printing the maze, after solution found: ")
                mh.print_maze(maze)
                return
            mh.add_walk_symbol(maze,m)
            dfs(mh.get_adjacent_positions(maze,m),position,explored)
   
dfs(mh.get_adjacent_positions(maze,position),position,explored)