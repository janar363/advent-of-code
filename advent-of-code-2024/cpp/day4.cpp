# include <iostream>
# include <fstream>
# include <vector>

using namespace std;

int main(){
    ifstream file("../input");

    vector<string> grid;
    string str;

    while(file >> str){
        grid.push_back(str);
    }

    int part1 = 0;
    int dir[8][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

    for(int i=0; i<grid.size(); i++){
        for(int j=0; j<grid[0].length(); j++){
            if(grid[i][j] == 'X'){
                if(j + 3 < grid[0].length() && grid[i].substr(j, 4) == "XMAS") part1++;
                if(j - 3 >= 0 && grid[i].substr(j-3, 4) == "SAMX") part1++;
                if(i + 3 < grid.size() && grid[i+1][j] == 'M' && grid[i+2][j] == 'A' && grid[i+3][j] == 'S') part1++;
                if(i - 3 >= 0 && grid[i-1][j] == 'M' && grid[i-2][j] == 'A' && grid[i-3][j] == 'S') part1++;

                if(i - 3 >= 0 && j - 3 >= 0 && grid[i-1][j-1] == 'M' && grid[i-2][j-2] == 'A' && grid[i-3][j-3] == 'S') part1++;
                if(i - 3 >= 0 && j + 3 < grid[0].length() && grid[i-1][j+1] == 'M' && grid[i-2][j+2] == 'A' && grid[i-3][j+3] == 'S') part1++;
                if(i + 3 < grid.size() && j - 3 >= 0 && grid[i+1][j-1] == 'M' && grid[i+2][j-2] == 'A' && grid[i+3][j-3] == 'S') part1++;
                if(i + 3 < grid.size() && j + 3 < grid[0].length() && grid[i+1][j+1] == 'M' && grid[i+2][j+2] == 'A' && grid[i+3][j+3] == 'S') part1++;

            }
        }
    }

    int part2 = 0;
    for(int i=1; i<grid.size()-1; i++){
        for(int j=1; j<grid[0].length()-1; j++){
            if(grid[i][j] == 'A'){
                if(grid[i-1][j-1] == 'M' && grid[i-1][j+1] == 'M' && grid[i+1][j-1] == 'S' && grid[i+1][j+1] == 'S') part2++;
                if(grid[i-1][j-1] == 'S' && grid[i-1][j+1] == 'S' && grid[i+1][j-1] == 'M' && grid[i+1][j+1] == 'M') part2++;
                if(grid[i-1][j-1] == 'M' && grid[i-1][j+1] == 'S' && grid[i+1][j-1] == 'M' && grid[i+1][j+1] == 'S') part2++;
                if(grid[i-1][j-1] == 'S' && grid[i-1][j+1] == 'M' && grid[i+1][j-1] == 'S' && grid[i+1][j+1] == 'M') part2++;
            }
        }
    }

    cout << "part 1: " << part1 << endl;
    cout << "part 2: " << part2 << endl;
}
