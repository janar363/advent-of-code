# include <iostream>
# include <vector>
# include <fstream>

using namespace std;

vector<string> inp;
vector<string> inp_c;
vector<vector<long long> > steps;
unordered_map<string, int> hash_map;

void fetch_data(){
    ifstream file("day14.txt");

    string line;
    // int lc= 0;
    while(getline(file, line)){
        if(line.empty()) break;

        inp.push_back(line);
    }

    inp_c = inp;
}

void rotate_inp(int f=0){
    vector<string> rotated_inp;
    if(f == 0){
        for(int j=0; j<inp[0].size(); j++){
            string str = "";
            for(int i=inp.size()-1; i>=0; i--){
                str += inp[i][j];
            }
            rotated_inp.push_back(str);
        }

        inp = rotated_inp;
    } else {
        for(int j=0; j<inp_c[0].size(); j++){
            string str = "";
            for(int i=inp_c.size()-1; i>=0; i--){
                str += inp_c[i][j];
            }
            rotated_inp.push_back(str);
        }

        inp_c = rotated_inp;
    }
    
}

void move_inp(int f=0){
    if(f == 0){
        steps = vector<vector<long long> >(inp.size(), vector<long long>(inp[0].size(), 0));
    

        for(int i=0; i<inp[0].size(); i++){
            if(inp[0][i] == '.') steps[0][i] = 1;
            else steps[0][i] = 0;

        }


        for(int i=1; i<inp.size(); i++){
            for(int j=0; j<inp[0].length(); j++){
                // cout << inp[i][j];
                if(inp[i][j] == '.') steps[i][j] = steps[i-1][j]  + 1;
                else if(inp[i][j] == 'O') steps[i][j] = steps[i-1][j];
                else steps[i][j] = 0;

                if(inp[i][j] == 'O') {
                    inp[i][j] = '.';
                    inp[i - steps[i][j]][j] = 'O';
                    
                }
                

            }

            
        }
  
    }else {
        steps = vector<vector<long long> >(inp_c.size(), vector<long long>(inp_c[0].size(), 0));
    

        for(int i=0; i<inp_c[0].size(); i++){
            if(inp_c[0][i] == '.') steps[0][i] = 1;
            else steps[0][i] = 0;

        }


        for(int i=1; i<inp_c.size(); i++){
            for(int j=0; j<inp_c[0].length(); j++){
                // cout << inp[i][j];
                if(inp_c[i][j] == '.') steps[i][j] = steps[i-1][j]  + 1;
                else if(inp_c[i][j] == 'O') steps[i][j] = steps[i-1][j];
                else steps[i][j] = 0;

                if(inp_c[i][j] == 'O') {
                    inp_c[i][j] = '.';
                    inp_c[i - steps[i][j]][j] = 'O';
                    
                }
                

            }

            
        }
    }
    
    
}

long long calculate_load(int f=0){
    if(f==0){
        long long tl = 0;
        long long rl = 0;
        for(int i=0; i<inp.size(); i++){
            long long rc = 0;
            for(int j=0; j<inp.size(); j++){


                if(inp[i][j] == 'O') rc++;
            }
            tl += rc * (inp.size()-i);

        }

        return tl;
    }else {
        long long tl = 0;
        long long rl = 0;
        for(int i=0; i<inp_c.size(); i++){
            long long rc = 0;
            for(int j=0; j<inp_c.size(); j++){


                if(inp_c[i][j] == 'O') rc++;
            }
            tl += rc * (inp_c.size()-i);

        }

        return tl;
    }
    
}

string get_hash(){
    string hash="";
    for(auto r: inp){
        hash += r;
    }

    return hash;
}

void process_data(long long c=1){
    long long tfl = 0;
    long long cycle=0;
    long long repeate_start = 0;

    for(; cycle<c; cycle++){
        long long lfc = 0;
        for(int i=0; i<4; i++){
            
            move_inp();
            
            rotate_inp();

        }

        string hash = get_hash();
        hash_map[hash]++;

        if(hash_map[hash] == 2 && repeate_start == 0) repeate_start = cycle;
        if(hash_map[hash] == 3) break;
        
    }


   long long rem_cycle = repeate_start + (c - repeate_start) % (cycle-repeate_start); 

   for(int i=0; i<rem_cycle; i++){
        for(int i=0; i<4; i++){
                
                move_inp(1);
                
                rotate_inp(1);

            }
   }
    
    tfl = calculate_load(1);

    cout << "load after " << c << "  cycles = " << tfl << endl;

}

int main(){

    fetch_data();

    process_data(1000000000);
}