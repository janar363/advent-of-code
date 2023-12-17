# include <iostream>
# include <vector>
# include <fstream>

using namespace std;

struct Key { // 1 based index
    int i;
    int j;
    int dir;
};

struct KeyHasher {
    size_t operator()(const Key& k) const {
        return hash<int>()(k.i) ^ hash<int>()(k.j) ^ hash<int>()(k.dir);    
    }
};

struct KeyEquals { 
    bool operator()(const Key& lhs, const Key& rhs) const {
    return lhs.i == rhs.i && lhs.j == rhs.j && lhs.dir == rhs.dir;
    }
};


vector<string> c;
vector<string> a_map;

vector<pair<int, int> > d;
unordered_map<Key, int, KeyHasher, KeyEquals> sdp;
unordered_map<Key, int, KeyHasher, KeyEquals> dp;

void set_a_map(){
    string line="";
    for(int i=0; i<c[0].length(); i++) line += ".";

    a_map = vector<string>(c.size(), line);
}

void fetch_data(){
    ifstream file("day16.txt");

    string line;
    
    while(getline(file, line)){
        if(line.empty()) break;

        c.push_back(line);

    } 

    // cout << "rock map\n";
    // for(auto r: c){
    //     cout << r << endl;
    // }

    
    set_a_map();
    

    // cout << "activation map\n";
    // for(auto r: a_map){
    //     cout << r << endl;
    // }

}

Key get_key(int i, int j, pair<int, int> dir){
    int kdir = 0;
    if(dir == d[0]) kdir = 0;
    else if(dir == d[1]) kdir = 1;
    else if(dir == d[2]) kdir = 2;
    else kdir = 3;

    Key k = {i, j, kdir};
    return k;
}

vector<pair<int, int> > get_dir(int i, int j, pair<int, int> dir){
    vector<pair<int, int> > dv;
    

    Key k = get_key(i, j, dir);

    sdp[k]++;
    if(sdp[k] == 2) return dv;
    
    if(c[i][j] == '.') dv.push_back(dir);
    else if(c[i][j] == '|'){
        if(dir == d[0] || dir == d[2]) dv.push_back(dir);
        else if(dir == d[1] || dir == d[3]) dv.push_back(d[0]), dv.push_back(d[2]);

    } else if(c[i][j] == '-'){
        if(dir == d[1] || dir == d[3]) dv.push_back(dir);
        else if(dir == d[0] || dir == d[2]) dv.push_back(d[1]), dv.push_back(d[3]);
    } else if(c[i][j] == '/'){
        if(dir == d[0]) dv.push_back(d[1]);
        else if(dir == d[1]) dv.push_back(d[0]);
        else if(dir == d[2]) dv.push_back(d[3]);
        else if(dir == d[3]) dv.push_back(d[2]);
    } else if(c[i][j] == '\\'){
        if(dir == d[0]) dv.push_back(d[3]);
        else if(dir == d[1]) dv.push_back(d[2]);
        else if(dir == d[2]) dv.push_back(d[1]);
        else if(dir == d[3]) dv.push_back(d[0]);
    }

    return dv;
}

long long activate_rocks(int i, int j, pair<int, int> dir){
    long long count = 0;


    Key k = get_key(i, j, dir);
    if(dp[k]) return 0;

    if(i < 0 || i  >= c.size()) {return 0; }
    if(j < 0 || j  >= c[0].size()){ return 0; }

    if(a_map[i][j] != '#') count = 1;
    a_map[i][j] = '#';

    vector<pair<int, int> > next;
    next = get_dir(i, j, dir);

    for(auto ndir: next){

        count += activate_rocks(i+ndir.first, j+ndir.second, ndir);

    }

    dp[k] = count;
    return count;

}


void process_data(){
    d.push_back(make_pair(-1, 0));
    d.push_back(make_pair(0, 1));
    d.push_back(make_pair(1, 0));
    d.push_back(make_pair(0, -1));

    long long max_a = 0;

    cout << "activation = " << activate_rocks(0, 0, d[1]) << endl;
    
    for(int j=0; j<a_map[0].size(); j++){
        for(auto curd: d){
            sdp.clear();
            dp.clear();
            set_a_map();
            long long cur_a = activate_rocks(0, j, curd);

            if(cur_a > max_a) max_a = cur_a;

            cur_a = activate_rocks(a_map.size()-1, j, curd);

            if(cur_a > max_a) max_a = cur_a;
        }
    }


    for(int i=0; i<a_map.size(); i++){
        for(auto curd: d){
            sdp.clear();
            dp.clear();
            set_a_map();
            long long cur_a = activate_rocks(i, 0, curd);

            if(cur_a > max_a) max_a = cur_a;

            cur_a = activate_rocks(i, a_map[0].size()-1, curd);

            if(cur_a > max_a) max_a = cur_a;
        }
    }
    
    cout << "max actication = " << max_a << endl;
}

int main(){

    fetch_data();

    process_data();
}