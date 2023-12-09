# include <iostream>
# include <vector>
# include <fstream>

using namespace std;


long long get_future(vector<long long> present){
    int z_c = 0;

    for(auto p: present)
        if(p == 0) z_c++;

    if(z_c == present.size()) return 0;

    vector<long long> past;

    for(int i=0; i<present.size()-1; i++)
        past.push_back(present[i+1]-present[i]);

    return present[present.size()-1] + get_future(past);
}

long long get_past(vector<long long> present){
    int z_c = 0;

    for(auto p: present)
        if(p == 0) z_c++;

    if(z_c == present.size()) return 0;

    vector<long long> past;

    for(int i=0; i<present.size()-1; i++)
        past.push_back(present[i+1]-present[i]);

    return present[0] - get_past(past);
}


int main(){
    std::ifstream file("day9.txt");

    vector<vector<long long> > histories;
    long long future_c = 0;

    string line;
    long long line_c=0;
    long long rank = 0;
    while(getline(file, line)){
        vector<long long> history;
        if(line.empty()) {
            break;
        }


        for(int i=0; i<line.length(); i++){
            long long num = 0;
            long long parity = 1;
            while(i < line.length() && (isdigit(line[i]) || line[i] == '-')) {
                if(line[i] == '-') parity = -1ll, i++;
                num = num * 10ll + (line[i++]-'0');
            }
            history.push_back(num * parity);
        }

        histories.push_back(history);
    }

    
    for(int i=0; i<histories.size(); i++){
        vector<long long> history = histories[i];
        
        future_c += get_past(history);
    }

    cout << "fucture count = " << future_c << endl;
}