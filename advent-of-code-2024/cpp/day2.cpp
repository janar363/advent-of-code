# include <iostream>
# include <fstream>
# include <sstream>
# include <vector>

using namespace std;

bool check(vector<int> & report){
    bool change = report[0] > report[1];
    for(int i=0; i<report.size()-1; i++){
        if((report[i] > report[i+1]) != change || abs(report[i] - report[i+1]) < 1 || abs(report[i] - report[i+1]) > 3) return false;
    }

    return true;
}

bool check2(vector<int> & report){
    bool change = report[0] > report[1];
    
    if(!check(report)){
        for(int i=0; i<report.size(); i++){
            vector<int> temp = report;
            temp.erase(temp.begin() + i);
            if (check(temp)) return true;

        }
        return false;
    }
    
    return true;
}

int main(){
    ifstream file("../input");


    string line;
    long long part1 = 0;
    long long part2 = 0;
    while(getline(file, line)){
        istringstream iss(line);
        int level;
        vector<int> report;
        while(iss >> level)
            report.push_back(level);

        if(check(report)) part1 += 1;
        if(check2(report)) part2 += 1;

    }

    cout << "part 1 : " << part1 << endl;
    cout << "part 2 : " << part2 << endl;


}