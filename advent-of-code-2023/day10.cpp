# include<iostream>
# include<vector>
# include<fstream>
# include<unordered_map>
# include<unordered_set>
# include<queue>
#include <iomanip>

using namespace std;

unordered_map<char, unordered_set<char> > pipes;
vector<vector<char> > grid;
vector<vector<char> > grid_path;
vector<vector<int> > path_c;
int max_c = -1;
pair<int, int> start;
int start_c = 0;

// identiying starting pipe
void set_starting_pipe(){
    bool has_north = false;
    bool has_south = false;
    bool has_east = false;
    bool has_west = false;
    if(start.first != 0 && pipes['S'].find(grid[start.first-1][start.second]) != pipes['S'].end())
        has_north = true;

    if(start.first != grid.size()-1 && pipes['N'].find(grid[start.first+1][start.second]) != pipes['N'].end())
        has_south = true;

    if(start.second != 0 && pipes['E'].find(grid[start.first][start.second-1]) != pipes['E'].end())
        has_west = true;

    if(start.second != grid[start.first].size()-1 && pipes['W'].find(grid[start.first][start.second+1]) != pipes['W'].end())
        has_east = true;

    if(has_north && has_south) {grid[start.first][start.second] = '|'; return;}

    if(has_north && has_east) {grid[start.first][start.second] = 'L'; return;}

    if(has_north && has_west) {grid[start.first][start.second] = 'J'; return;}

    if(has_south && has_east) {grid[start.first][start.second] = 'F'; return;}

    if(has_south && has_west) {grid[start.first][start.second] = '7'; return;}

    if(has_east && has_west) {grid[start.first][start.second] = '-'; return;}

    
}

// retuns valid neibhoues that can connet with current pipe
vector<pair<int, int> > get_valid_neibhours(int x, int y){
    vector<pair<int, int> > neibhours;
    if(pipes['N'].find(grid[x][y]) != pipes['N'].end() && x != 0 && pipes['S'].find(grid[x-1][y]) != pipes['S'].end())
        neibhours.push_back(make_pair(-1, 0));

    if(pipes['S'].find(grid[x][y]) != pipes['S'].end() && x != grid.size()-1 && pipes['N'].find(grid[x+1][y]) != pipes['N'].end())
        neibhours.push_back(make_pair(1, 0));

    if(pipes['E'].find(grid[x][y]) != pipes['E'].end() && y != grid[x].size()-1 && pipes['W'].find(grid[x][y+1]) != pipes['W'].end())
        neibhours.push_back(make_pair(0, 1));
    
    if(pipes['W'].find(grid[x][y]) != pipes['W'].end() && y != 0 && pipes['E'].find(grid[x][y-1]) != pipes['E'].end())
        neibhours.push_back(make_pair(0, -1));

    // for(auto ne: neibhours){
    //     if(ne.first == -1) cout << "north" << endl;
    //     if(ne.first == 1) cout << "south"<< endl;
    //     if(ne.second == -1) cout << "west " << endl;
    //     if(ne.second == 1) cout << "east" << endl;
    // }
    return neibhours;
}

// return total number of steps in the loop
int get_max_dist_from_start(int x, int y){

    vector<pair<int, int> > valid_neibhours = get_valid_neibhours(x, y);

    if(valid_neibhours.size() == 0) return -1;

    int unvisited = 0;
    for(auto ne: valid_neibhours){
        grid_path[x][y] = '0';
        if(path_c[x+ne.first][y+ne.second] == -1){
            path_c[x+ne.first][y+ne.second] = path_c[x][y] + 1;
            
            max_c = max(max_c, get_max_dist_from_start(x+ne.first, y+ne.second));


            unvisited++;
        }
        
    }
    
    if(unvisited == 0) return path_c[x][y];

    return max_c;
}

bool is_inside(int x, int y){
    int tempx = x, tempy = y;
    int edge_c = 0;
    bool has_west = false, has_east = false;
    unordered_map<char, int> pipe_c;

    // check for west border
    while(tempy > 0){
        char cur_pipe = grid[tempx][tempy-1];
        if(grid_path[tempx][tempy-1] == '0' && grid[tempx][tempy-1] != '-') {
            pipe_c[cur_pipe]++;
        }
        tempy--;
    }

    // all | pipes are concidered as single wall
    // all pipe pair that can connect horizonally but has opposite verical connections are considered as 1 wall
    // count all single walls encountered 
    // if odd inside else outside
    edge_c += pipe_c['|'] + min(pipe_c['L'], pipe_c['7'])  + min(pipe_c['J'], pipe_c['F']);
    return edge_c % 2 == 1;

}

int main(){
    std::ifstream file("day10.txt");

    unordered_set<char> temp;
    temp.insert('|');
    temp.insert('J');
    temp.insert('L');
    temp.insert('S');
    pipes['N'] = temp;

    temp.clear();
    temp.insert('|');
    temp.insert('F');
    temp.insert('7');
    temp.insert('S');
    pipes['S'] = temp;

    temp.clear();
    temp.insert('-');
    temp.insert('F');
    temp.insert('L');
    temp.insert('S');
    pipes['E'] = temp;

    temp.clear();
    temp.insert('-');
    temp.insert('7');
    temp.insert('J');
    temp.insert('S');
    pipes['W'] = temp;

    temp.clear();
    pipes['.'] = temp;

    
    string line;
    long long line_c=0;
    
    // cout << "input start\n";

    while(getline(file, line)){

        if(line.empty()) {
            break;
        }
        vector<char> row;
        for(int i=0; i<line.size(); i++){
            char ch = line[i];
            if(ch == 'S') start = make_pair(line_c, i);
            row.push_back(ch);
        }

        grid.push_back(row);
        line_c++;
    }

    // cout << "input end\n";

    set_starting_pipe();
    path_c = vector<vector<int> >(grid.size(), vector<int>(grid[0].size(), -1));
    grid_path = vector<vector<char> > (grid.size(), vector<char>(grid[0].size(), '.'));
    path_c[start.first][start.second] = 0;

    max_c = get_max_dist_from_start(start.first, start.second);
    cout << "max c = " << (max_c / 2 + 1) << endl;

    int inner_c = 0;
    for(int r=0; r<grid_path.size(); r++){
        for(int c=0; c<grid_path[r].size(); c++){

            if(grid_path[r][c] == '.'){
                if(is_inside(r, c)) inner_c++;
            } 
        }
    }

    cout << "inner tile count = " << inner_c << endl;
}