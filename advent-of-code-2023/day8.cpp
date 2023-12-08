# include<iostream>
# include<vector>
# include<fstream>
# include<algorithm>
# include<numeric>

using namespace std;

long long gcd(long long a, long long b) {
  if (b == 0)
    return a;
  return gcd(b, a % b);   
}

long long lcm(std::vector<long long>& v) {
  long long LCM = 1;
  long long GCD = 1;
  
  for(long long i : v) {
    GCD = gcd(LCM, i);
    LCM = LCM*i/GCD;
  }
  
  return LCM;
}

int main(){
    std::ifstream file("day8.txt");

    string rl;
    string line;
    unordered_map<string, pair<string, string> > directions;
    vector<string> start_nodes;

    getline(file, rl);

    // input start
    while(getline(file, line)){
        if(line == "") continue;
        
        int i=0; 

        // read key location
        string key = "";
        while(line[i] != ' ')
            key += line[i++];
        
        if(key[key.length()-1] == 'A') start_nodes.push_back(key);

        while(line[i++] != '(');

        // read left location 
        string left = "";
        while(line[i] != ',')
            left += line[i++];
        
        i += 2;

        // read right location
        string right = "";
        while(line[i] != ')')
            right += line[i++];

        directions[key] = make_pair(left, right);
    }
    // input end

    
    long long steps = 0;// total number of steps
    long long dir_idx = 0; // index pointing to current direction in LR path
    long long end_count = 0;// number of stating point that reached end(Z)
    vector<long long> end_step_c(start_nodes.size(), -1);// stores no of steps needed, for starting point at index i, to reach end(Z)

    while(end_count != start_nodes.size()){ // terminates when every starting point reaches end exactly once

        end_count = 0;

        for(int node=0; node < start_nodes.size(); node++){

            if(rl[dir_idx] == 'L')
                start_nodes[node] = directions[start_nodes[node]].first;
            else 
                start_nodes[node] = directions[start_nodes[node]].second;

            string cur = start_nodes[node];

            
            if(cur[cur.length()-1] == 'Z' && end_step_c[node] == -1)
                end_step_c[node] = steps+1;
        }   

        // counting number of starting that reached end(Z)
        for(int j=0; j<end_step_c.size(); j++){
            if(end_step_c[j] != -1) end_count++;
        }


        dir_idx++;

        // reseting LR dir_idx to start from first again
        if(dir_idx == rl.length()) dir_idx = 0;

        steps++;

    }
    
    // return lcm of number of steps needed for each starting point to reach end(Z)
    cout << "steps = " << lcm(end_step_c) << endl;
}