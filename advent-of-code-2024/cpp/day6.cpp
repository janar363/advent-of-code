# include <iostream>
# include <fstream>
# include <sstream>
# include <vector>
# include <unordered_map>
# include <unordered_set>

using namespace std;

// set hasher and equals
struct pairHasher {
    size_t operator()(const pair<int, int>& ele) const {
        return hash<int>()(ele.first) ^ hash<int>()(ele.second);
    }
};

struct pairEquals {
    bool operator()(const pair<int, int>& lhs, const pair<int, int> & rhs){
        return lhs.first == rhs.first && lhs.second == rhs.second;
    }
};

struct visitedHasher {
    size_t operator()(const pair<pair<int, int>, char>& ele) const {
        return hash<int>()(ele.first.first) ^ hash<int>()(ele.first.second) ^ hash<char>()(ele.second);
    }
};

struct visitedEquals {
    bool operator()(const pair<pair<int, int>, char>& lhs, const pair<pair<int, int>, char> & rhs){
        return lhs.first.first == rhs.first.first && lhs.first.second == rhs.first.second && lhs.second == rhs.second;
    }
};

// string operations
vector<string> split(string str, char at){
    vector<string> tokens;
    string token;
    istringstream ss(str);

    while(getline(ss, token, at)) tokens.push_back(token);

    return tokens;
}

vector<string> getGrid(){
    vector<string> grid;
    string line;

    ifstream file("../input");

    while(file >> line) grid.push_back(line);

    return grid;   
}

bool checkInBounds(vector<string> & grid, int x, int y){
    return x >= 0 && x < grid.size() && y >= 0 && y < grid[0].size();
}

int main(){
    vector<string> grid = getGrid();

    unordered_map<char, pair<pair<int, int>, char> > dir;
    dir['^'] = make_pair(make_pair(-1, 0), '>');
    dir['>'] = make_pair(make_pair(0, 1), 'V');
    dir['V'] = make_pair(make_pair(1, 0), '<');
    dir['<'] = make_pair(make_pair(0, -1), '^');

    unordered_map<char, int> dmap;
    dmap['^'] = 0;
    dmap['>'] = 1;
    dmap['V'] = 2;
    dmap['<'] = 3;


    int pos[2], start[2];

    for(int i=0; i<grid.size(); i++)
        for(int j=0; j<grid[0].size(); j++)
            if(grid[i][j] == '^') pos[0] = i, pos[1] = j, start[0] = i, start[1] = j;

    bool inBounds = true;
    unordered_set<pair<int, int>, pairHasher, pairEquals> part1;
    while(inBounds) {
        int nx = pos[0]+dir[grid[pos[0]][pos[1]]].first.first, ny = pos[1]+dir[grid[pos[0]][pos[1]]].first.second;
        
        part1.insert(make_pair(pos[0], pos[1]));

        if(checkInBounds(grid, nx, ny)){
            if(grid[nx][ny] == '.') grid[nx][ny] = grid[pos[0]][pos[1]], grid[pos[0]][pos[1]] = '.', pos[0] = nx, pos[1] = ny;
            else if(grid[nx][ny] == '#') grid[pos[0]][pos[1]] = dir[grid[pos[0]][pos[1]]].second;
        } else inBounds = false;
    }

    cout << "part 1 : " << part1.size() << endl;
    
    
    long long part2 = 0;
    int i=0;
    for(auto ppos: part1) {
        if(ppos.first == start[0] && ppos.second == start[1]) continue;

        grid[ppos.first][ppos.second] = '#';
        grid[pos[0]][pos[1]] = '.';

        pos[0] = start[0], pos[1] = start[1];
        grid[start[0]][start[1]] = '^';

        bool inBounds = true;
        vector<vector<vector<bool> > > visited(grid.size(), vector<vector<bool> >(grid[0].size(), vector<bool>(4, false)));

        while(inBounds) {
            
            int nx = pos[0]+dir[grid[pos[0]][pos[1]]].first.first, ny = pos[1]+dir[grid[pos[0]][pos[1]]].first.second;

            if(visited[pos[0]][pos[1]][dmap[grid[pos[0]][pos[1]]]]) {
               part2 += 1;
               break;
            }
            visited[pos[0]][pos[1]][dmap[grid[pos[0]][pos[1]]]] = true;

            if(checkInBounds(grid, nx, ny)){
                if(grid[nx][ny] == '.') grid[nx][ny] = grid[pos[0]][pos[1]], grid[pos[0]][pos[1]] = '.', pos[0] = nx, pos[1] = ny;
                else if(grid[nx][ny] == '#') grid[pos[0]][pos[1]] = dir[grid[pos[0]][pos[1]]].second;
            } else { 
                inBounds = false;
            }
        }
        
        grid[ppos.first][ppos.second] = '.';
    }

    cout << "part2 : " << part2 << endl;
}