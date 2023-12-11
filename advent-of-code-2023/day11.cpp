# include<iostream>
# include<vector>
# include<fstream>
# include<unordered_map>

using namespace std;

vector<vector<char> > init_universe;
vector<vector<long long> > cost;
unordered_map<long long, pair<long long, long long> > coods;
long long gal_c = 0;

void expand_universe(int expand_by){
    cost = vector<vector<long long> >(init_universe.size(), vector<long long>(init_universe[0].size(), 1));
    vector<bool> empty_row(init_universe.size(), true);
    vector<bool> empty_col(init_universe[0].size(), true);

    for(long long r=0; r < init_universe.size(); r++){
        for(long long c=0; c < init_universe[0].size(); c++){

            if(init_universe[r][c] != '.') {
                empty_row[r] = false;
                empty_col[c] = false;
            }
        }
    }   



    // vector<char> empty(init_universe[0].size(), '.');
    // int rows_inserted = 0;
    for(long long i=0; i<empty_row.size(); i++){
        bool empty_r = empty_row[i];
        if(empty_r) {
            for(long long j=0; j<init_universe[0].size(); j++){
                cost[i][j] = expand_by;
            }
        }
    }

    // int cols_inserted = 0;
    for(long long i=0; i<empty_col.size(); i++){
        bool empty_c = empty_col[i];
        if(empty_c) {
            for(long long j=0; j<init_universe.size(); j++)
                cost[j][i] = expand_by;
        }
    }
}

void fetch_coods(){
    long long count = 0;
    for(long long r=0; r<init_universe.size(); r++){
        for(long long c=0; c<init_universe[0].size(); c++){
            if(init_universe[r][c] != '.'){
                coods[count++] = make_pair(r, c);
                gal_c++;
            }
        }
    }
}

long long dist_sum(){
    long long total_dist = 0;

    for(long long i=0; i<gal_c-1; i++){
        for(long long j=i+1; j<gal_c; j++){

            pair<long long, long long> d1 = coods[i];
            pair<long long, long long> d2 = coods[j];
            long long curdist = 0;

            if(d1.second <= d2.second){
                for(long long j1 = d1.second+1; j1<=d2.second; j1++){
                    curdist += cost[d1.first][j1];
                }
            } else {
                for(long long j1 = d1.second-1; j1>=d2.second; j1--){
                    curdist += cost[d1.first][j1];
                }
            }

            if(d1.first <= d2.first){
                for(long long i1=d1.first+1; i1<=d2.first; i1++ ){
                    curdist += cost[i1][d2.second];
                }
            } else {
                for(long long i1=d1.first-1; i1>=d2.first; i1-- ){
                    curdist += cost[i1][d2.second];
                }
            }

            total_dist += curdist;
        }
    }

    return total_dist;
}

int main(){
    std::ifstream file("day11.txt");

    string line;
    long long line_c=0;
    
    while(getline(file, line)){

        if(line.empty()) {
            break;
        }
        
        vector<char> row;
        
        for(long long i=0; i<line.length(); i++){

            row.push_back(line[i]);

        }

        init_universe.push_back(row);
        line_c++;
    }


    fetch_coods();

    expand_universe(2);
    cout << "total distance for expand_by(" << 2 << ") = " << dist_sum() << endl;

    expand_universe(1000000);
    cout << "total distance for expand_by(" << 1000000 << ") = " << dist_sum() << endl;
}