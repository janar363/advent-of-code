# include <iostream>
# include <fstream>
# include <vector>
# include <unordered_map>

using namespace std;

int main(){
    ifstream file("../input");

    vector<int> l, r;
    int ln, rn;
    unordered_map<int, int> rc;

    while(file >> ln >> rn){
        l.push_back(ln);
        r.push_back(rn);

        rc[rn]++;
    }

    sort(l.begin(), l.end());
    sort(r.begin(), r.end());

    long long part1 = 0;
    long long part2 = 0;
    for(int i=0; i<l.size(); i++){
        part1 += abs(l[i]-r[i]);
        part2 += l[i] * rc[l[i]];
    }


    cout << "part1 : " << part1 << endl;
    cout << "part2 : " << part2 << endl;
}